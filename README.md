# 
Contexte du projet
L’objectif étant de prouver les compétences techniques de notre start-up et de faire adhérer le corps médical au projet DATA Health HUB. 
Dans un souci d’accessibilité aux données, le POC se fera avec les données publiques du dataset MedNist.

Nous partons d’une application existante développée par les équipes du CHRU, un algorithme développé via Pytorch qui propose déjà de beaux résultats ,
L'application sera développée en flask et permet de classifier sa radiographie.

Voici les missions attendues :

-Implémenter un modèle de classification ( Transfert Learning) avec Keras /TensorFlow

-Amélioration du modèle MedNet ( Pytorch) : Un modèle de DeepLearning a été élaboré. Il utilise un réseau de neurones afin de pouvoir classer les images médicales
dans ces 6 catégories. Le modèle a obtenu un taux de 99% de prédictions correctes ce qui est un bon score.

-Création d'une interface et Evolution fonctionnelle : * L’application comprend 2 pages. L’application permet de sélectionner un fichier image et de le télécharger :
Puis elle permet d’obtenir sa classification. Les informations affichées sont « ID » qui correspond au numéro allant de 1 à 6 de la classe et « Class » qui
correspond au nom de la classe. L'application sera déployée via AzureWebapp. L'interface pourra se faire avec Flask et /ou Streamlit

BONUS Il vous est demandé de pouvoir sélectionner un, plusieurs ou tous les fichiers d’un dossier, de le ou les télécharger et de prédire la classification.

Amélioration de l'IA : 

Pour améliorer l'IA j'ai suivir les conseils de la fin du notebook et testé de manière empirique de changer le batchsize ainsi que le training. En quelques essai,
je suis arrivé a une accuracy de 99.8% qui m'a semblé très bon pour le temps passé à l'optimiser.

App Web :

Application web créer avec flask qui permet à l'utilisateur d'upload une image et d'avoir la prédiction de son image par l'IA. 
Application créer avec flask
