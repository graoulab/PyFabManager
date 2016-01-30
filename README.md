Gerer tout votre FabLab grace a un seul site web !
==================================================
Article , projet, machine, evenement , tout peut etre gerer sur le même site


Todo :
------
-Mail list

Installation :
--------------

 1. Clone du depot
 2. editer le fichier FabManager/setting.py par rapport a vos besoin
 3. Installer python 3 / Django / Pillow 
 4. dans la racine du dossier executer , pour generer la base de donnée:
 python3 manage.py makemigrations
 python manage.py migrate
 5. Pour lancer l'application en utilisans le serveur integrer a django :
	 python3 manage.py runserver 0.0.0.0:< VotrePort >
	 
 6. Creer votre premier utilisateur qui seras automatiquement admin
 7. ajouter des categorie/licence/matiere/machine
 8. Comuniquer l'addresse a vos membre pour qu'il puisse referencer leur projet 
 9. Pour les utilisateur non francophone vous pouvez generer des fichier de traduction en utilisant cette commande :
        python3 manage.py makemessages -l < VotreLangageCode > -e html -e py
    puis :
        python3 manage.py compilemessages
10. Profiter :)

Commande :
----------
Linux :

Installer dependance :                  pip3 install -r requirements.txt
Recuperer tout les fichier static :     python3 manage.py collectstatic --noinput
Generer fichier locale :                python3 manage.py makemessages -l < VotreLangageCode > -e html -e py
Compiler les fichier locaux :           python3 manage.py compilemessages
Creation fichier de base de donnée :    python3 manage.py makemigrations
Creer la base de donnée :               python3 manage.py migrate
demarer le serveur :                    python3 manage.py runserver

Windows :

Installer dependance :                  pip install -r requirements.txt
Recuperer tout les fichier static :     python manage.py collectstatic --noinput
Generer fichier locale :                python manage.py makemessages -l < VotreLangageCode > -e html -e py
Compiler les fichier locaux :           python manage.py compilemessages
Creation fichier de base de donnée :    python manage.py makemigrations
Creer la base de donnée :               python manage.py migrate
demarer le serveur :                    python manage.py runserver

