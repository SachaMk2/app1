# Plan du projet 

## Problème: 
Créer un programmme qui lit un code HTML afin de repérer les erreurs. De plus ce programme doit fournir un rapport avec l'emplacement des erreurs présentent dans le fichier donné.

## Entrées / Sorties 
- **Entrée** : Le code HTML source, manipulé sous forme de fichier texte.
- **Sortie** : Un rapport d'erreur clair et compréhensible, indiquant les emplacements précis des erreurs de structure dans le code source.

## Liste des tâches 
-Programmer en langage Python les routines de bases permettant de manipuler des fichiers texte.
-Traduire et implémenter des machines abstraites de type File et de type Pile dans le langage Python.
-Analyser le code HTML pour identifier les balises, les attributs et leur structure globale.
-Exprimer et développer l'algorithme de vérification en utilisant les structures de données de type File et Pile pour repérer les erreurs.
-Concevoir la génération du rapport d'erreur pointant les problèmes de balisage.
-Tester le bon fonctionnement de l'algorithme final.

## Cas limites à gérer 

Les balises auto-fermantes : Contrairement aux balises classiques, elles n'ont pas de balise de fermeture distincte et se terminent par /> (exemple : <img src="image.jpg" alt="Image" />). Le programme ne doit pas les considérer comme des erreurs de "balise non fermée".

La gestion des attributs : Les balises peuvent contenir des informations supplémentaires à l'intérieur de la balise d'ouverture. L'algorithme doit être capable d'isoler le nom de la balise (ex: meta dans <meta charset="utf-8" />) sans être bloqué par les attributs qui l'accompagnent.

