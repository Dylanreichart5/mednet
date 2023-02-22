from flask import Flask, render_template, request
from PIL import Image
import io
import numpy as np
import torch
from med import MedNet
import torchvision as tv
import torch
import numpy as np
import base64
import re
from flask import redirect, url_for
from werkzeug.utils import secure_filename
import os 

app = Flask(__name__)
app.config['images'] = 'static/images'


def label_predict(predicted_class):
    label = ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']
    predicted_class = str(predicted_class)
    if predicted_class == "tensor([0])":
        predicted_class = label[0]
    elif predicted_class == "tensor([1])":
        predicted_class = label[1]
    elif predicted_class == "tensor([2])":
        predicted_class = label[2]   
    elif predicted_class == "tensor([3])":
        predicted_class = label[3]
    elif predicted_class == "tensor([4])":
        predicted_class = label[4]
    elif predicted_class == "tensor([5])":
        predicted_class = label[5]
    return predicted_class

toTensor = tv.transforms.ToTensor()
def scaleImage(x):          # Pass a PIL image, return a tensor
    y = toTensor(x)
    if(y.min() < y.max()):  # Assuming the image isn't empty, rescale so its values run from 0 to 1
        y = (y - y.min())/(y.max() - y.min()) 
    z = y - y.mean()        # Subtract the mean value of the image
    return z

model = torch.load('saved_model', map_location=torch.device('cpu'))
# Page d'accueil pour l'upload de l'image
@app.route('/')
def upload():
    return render_template('upload.html')

# Page de résultat pour la prédiction du modèle
@app.route('/predict', methods=['POST'])
def predict():
    # Récupération de l'image téléchargée depuis le formulaire
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
        # Check if the file is empty
    if file.filename == '':
        return redirect(request.url)
        # Save the file to the uploads directory
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['images'], filename)
    file.save(filepath)
        # Return the image URL to be displayed on the webpage
    image_url = url_for('static', filename='../static/images/' + filename)
    # If the method is GET, simply return the upload page


    imageTensor = torch.stack([scaleImage(Image.open(file))])
    # Traitement de l'image pour la passer au modèle

    # Chargement du modèle pré-entrainé

    # Prédiction du modèle sur l'image
    prediction = model(imageTensor)

    # Récupération de la classe prédite
    predicted_class =  torch.max(prediction, dim=1)[1]

    predicted_class = label_predict(predicted_class)
    # print(predicted_class)
    # Retour de la page de résultat avec la classe prédite
    return render_template('predict.html', predicted_class=predicted_class, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)


