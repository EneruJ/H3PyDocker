# H3PyDocker

Cheat Sheet Docker ::

docker images : liste les images de Docker disponibles (avec l'id de l'image, son tag, son nom et sa date de création)

docker ps : liste les images de Docker en cours d'execution (avec l'id du conteneur, l'image, la commande pour l'executer, ses ports etc...)

docker --version : donne la version de Docker installée sur le PC

docker run -it -d <nom_de_l'image> : lance l'execution d'un conteneur Docker

docker stop <id_conteneur> : arrête l'execution d'un conteneur

docker kill <id_conteneur> : arrête directement l'execution d'un conteneur, tandis que docker stop arrête l'execution lorsque le conteneur a fini d'executer ses taches 

docker login : permet de se connecter au repository docker hub

docker build <path_dockerfile> : créer une image docker à partir d'un dockerfile
