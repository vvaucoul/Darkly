# Recherche

- **Nmap (Network Mapper)** est un outil pour **l'exploration du réseau et l'audit de sécurité**. Il est très utile pour la **recherche de vulnérabilités** dans un site web. Il permet de scanner les **ports ouverts**, les **services actifs** et les **informations sur l'hôte distant**.

```bash
> nmap -v -A $IP
# ...
| http-robots.txt: 2 disallowed entries 
|_/whatever /.hidden
# ...
```

- On peut voir que le site dispose de deux dossiers **normalement inaccessible** référencé dans `robots.txt`. `robots.txt` est un fichier texte placé à la **racine d'un site Web** qui indique aux robots d'indexation des moteurs de recherche **les parties du site qu'ils sont autorisés à explorer**. C'est un fichier public **accessible à tout utilisateur**.

- On peux lire le contenu de `robots.txt` en ajoutant `/robots.txt` à l'URL du site.

```txt
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

- Les deux dossiers indiqués sont `/whatever` et `/.hidden`. Ici, on s’intéresse au dossier `/.hidden`.

# Exploit

- On peut acceder au dossier `/.hidden` en ajoutant `/.hidden` a l'URL.

- Ce dossier contient des **liens qui pointent vers d'autres liens** etc... Après plusieurs redirections on arrive sur un fichiers **README** qui contient du **texte inutile** ou pour le **flag**. Manuellement, il est **impossible de parcourir tous ces liens** pour trouver le flag à cause du nombre de redirections possibles.

- Pour parcourir tous les liens et **trouver le flag**, on va utiliser un **crawler python** qui va parcourir les liens de la pages de manière **automatique** et **méthodique**. Après une minute, le **crawler** trouve le flag dans un des fichiers `README` et l'affiche.

```bash
> python3 crawler.py
# ...
Found 'flag' on page: http://127.0.0.1:8080/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README
Flag: Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```

- Ce dossier `/.hidden` est une façon **très naive** de cacher des informations. La page web étant **entièrement publique**, il est très facile de trouver le dossier `/.hidden`` et même une **structure complexe de liens imbriqués** ne **protège pas** du tout les fichiers qu'elle contient.

# Fix

- **Ne pas stocker des fichiers sensibles coté client**. 

- Restreindre l'accès aux **dossiers sensibles** comme `/.hidden` en configurant le serveur web pour **bloquer** ou **rediriger** les requêtes vers ce chemins.

```apache
<DirectoryMatch "^/.hidden">
    Order Deny,Allow
    Deny from all
</DirectoryMatch>
```
