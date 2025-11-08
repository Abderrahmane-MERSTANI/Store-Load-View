Password Manager — README

Simple, sécurisé (au repos) et pédagogique — un gestionnaire de mots de passe local en Python utilisant cryptography.Fernet.

🧾 Description

Ce petit projet est un gestionnaire de mots de passe en ligne de commande.
Il permet d’enregistrer, charger et consulter des mots de passe pour différents sites. Les mots de passe sont chiffrés localement avec Fernet et stockés dans un fichier binaire (passwords.bin). La clé de chiffrement est générée une seule fois et conservée dans key.key.

Ce dépôt est conçu pour les débutants qui veulent apprendre :

la lecture/écriture de fichiers (texte & binaire),

la sérialisation JSON,

les bases du chiffrement symétrique,

l’architecture d’un programme Python simple (fonctions + boucle principale).

✅ Fonctionnalités

Génération unique d’une clé de chiffrement (key.key).

Sauvegarde des mots de passe chiffrés (passwords.bin).

Ajout d’un mot de passe pour un site.

Consultation d’un mot de passe existant.

Liste de tous les sites enregistrés.

Interface console simple et lisible.

⚠️ Limitations et sécurité

Clé stockée localement (key.key) en clair — si quelqu’un accède à ce fichier il pourra déchiffrer passwords.bin.

Pas de mot de passe maître : toute personne ayant accès à votre compte système peut utiliser l’outil.

Les mots de passe sont présents en mémoire pendant l’exécution.

Convient pour un usage pédagogique ou personnel local, pas pour une utilisation en production sans améliorations supplémentaires.

🚀 Prérequis

Python 3.8+ (recommandé)

Pip

Installer la dépendance nécessaire :

pip install cryptography

📁 Fichiers générés

key.key — la clé de chiffrement (conserver en lieu sûr ; si perdue, les mots de passe seront irrécupérables).

passwords.bin — le coffre chiffré contenant les mots de passe.

▶️ Utilisation

Sauvegarder le script (par exemple password_manager.py).

Lancer le script :

python password_manager.py


Choisir une option dans le menu :

1 : Ajouter un mot de passe (site + mot de passe).

2 : Voir le mot de passe d’un site.

3 : Lister tous les sites enregistrés.

4 : Quitter.

🛠️ Exemple d’utilisation
=== Gestionnaire de mots de passe ===
1️⃣  Ajouter un mot de passe
2️⃣  Voir un mot de passe
3️⃣  Voir tous les sites enregistrés
4️⃣  Quitter
Choisis une option : 1
Nom du site : github
Mot de passe : mysecretpassword
✅ Mot de passe enregistré avec succès.

💡 Améliorations conseillées (idées)

Master password : dériver la clé via PBKDF2 à partir d’un mot de passe maître (évite de stocker key.key en clair).

Masquer la saisie des mots de passe avec getpass.

Générateur de mot de passe pour créer des mots de passe aléatoires et forts.

Interface graphique (Tkinter) ou une interface web locale.

Fonction de suppression d’entrées et d’export/import chiffré.

Protéger la clé : chiffrer key.key avec une clé dérivée d’un mot de passe maître.

🧩 Architecture (fichier password_manager.py résumé)

generate_key() — crée key.key si absent.

load_key() — lit la clé depuis key.key.

save_passwords(passwords) — sérialise, chiffre et sauvegarde les mots de passe.

load_passwords() — lit et déchiffre passwords.bin.

main() — boucle d’interaction utilisateur (menu).

📜 Licence

Choisis la licence que tu préfères pour ton projet (MIT est simple et permissive). Exemple court :

MIT License


(ajoute un fichier LICENSE si tu veux partager publiquement.)
