# Recherche

#### Suite de [07_Hidden_directory_Crawler](../../07_Hidden_directory_Crawler/Ressources/Readme.md).

- Le second dossier indiqué dans `robots.txt` est `whatever` qui contient un fichier `htpasswd`.

- On peut **télécharger** ce fichier `htpasswd` qui contient un **identifiant et un mot de passe hashé**:

```plaintext
root:437394baff5aa33daa618be47b75cb49
```

# Exploit

- On peut utiliser un site comme [crackstation](https://crackstation.net/) pour tenter de **déchiffrer** le mot de passe hashé. La plupart des hashages sont **irréversibles** mais certains algorithmes de hashage sont **faibles** et peuvent être **cassés**.

```plaintext
Hash	                            Type    Result
437394baff5aa33daa618be47b75cb49    md5     qwerty123@
```

- Dans notre cas, le mot de passe est hashé en utilisant **MD5**, qui est considéré comme un **algorithme de hashage faible** en raison de sa 
**facilité à être décrypter** par **brute force** ou par **collision**.

- Dans le contexte des applications web, l'URL `/admin` est souvent utilisée pour désigner **l'interface d'administration du site**. C'est généralement dans cette section que les utilisateurs avec des **privilèges élevés**, comme **l'utilisateur root dans ce cas**, peuvent accéder à des **fonctionnalités avancées**, gérer le site, les utilisateurs, les contenus, etc.

- On peut alors se **connecter** avec les identifiants `root:qwerty123@`.

# Fix

- **Ne pas stocker des fichiers sensibles coté client**. Les **mots de passe administrateurs** sont parmi les informations **les plus sensibles** d'un site web car leur acquisition permet de prendre le **contrôle total du site**.

- **Hasher** les mots de passe en utilisant un **algorithme de hashage fort** comme **bcrypt**. Ces algorithmes sont **résistants** aux attaques par **brute force** et par **collision**.

- Configurer le serveur web pour **restreindre l'accès aux fichiers sensibles** tels que `htpasswd` ou `htaccess` en utilisant `<Files>` pour **bloquer** ou **rediriger** les requêtes vers ce chemins.

```apache
<Files ".ht*">
    Require all denied
</Files>
```

- Utiliser un **service d'authentification** dédié comme **OAuth** ou **OpenID Connect**.
