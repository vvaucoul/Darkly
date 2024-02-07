# Recherche

- Lorsque l'on inspecte les **cookies** (Application, Storage, Cookies), on peut voir la clef `I_am_admin` avec la valeur `68934a3e9455fa72420237eb05902327`.

# Exploit

- La chaine de caractère `68934a3e9455fa72420237eb05902327` est un hash **md5**. En [decrytant ce hash](https://md5decrypt.net/), on trouve que la valeur correspondante à `68934a3e9455fa72420237eb05902327` est `false`.

- On peut donc **changer la valeur** du cookie à `true` en remplacent la valeur par `b326b5062b2f0e69046810717534cb09`

# Fix

- Évitez d'utiliser des cookies pour stocker des **informations sensibles** ou **contrôler des privilèges**. Les cookies sont facilement modifiables par l'utilisateur.

- Implémenter une **authentification côté serveur robuste** pour vérifier l'identité des utilisateurs avant d'autoriser l'accès aux **fonctionnalités administratives**.

```PHP
session_start();
if (!isset($_SESSION['admin']) || !$_SESSION['admin']) {
    die('Access denied');
}
```

- Utiliser des **contrôles d'accès basés** sur les rôles pour s'assurer que seuls les utilisateurs autorisés peuvent accéder aux **fonctionnalités administratives**.

- Utiliser les attributs `secure` et `httponly` pour sécuriser les cookies qui permettent de **n'envoyer les cookies que sur HTTPS** (Man-in-the-Middle) et de ne **pas les rendre accessibles via JavaScript** (XSS).

```PHP
setcookie('cookie_name', 'cookie_value', [
    'secure' => true,  // cookie is only sent over HTTPS
    'httponly' => true,  // cookie is not accessible via JavaScript
]);
```
