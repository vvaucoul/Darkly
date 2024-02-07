# Recherche

- Sur la page d'accueil, on peut cliquer sur le lien `BornToSec` en bas de la page.

- On est **redirigé** sur une **nouvelle page** avec une image de goéland et une musique se lance. Lorsque l'on **inspecte le code source de la page**, on peut voir:

```HTML
<!-- ... -->

<!--
You must come from : "https://www.nsa.gov/".
-->

<!-- ... -->

<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->

<!-- ... -->
```

# Exploit

- Nous devons donc utiliser le navigateur `ft_bornToSec` et venir de la page `https://www.nsa.gov/`... ou alors utiliser `curl` pour changer le `User-Agent` et `Referer` de la **requête**.

```bash
curl -A "ft_bornToSec" -e "https://www.nsa.gov/" "http://127.0.0.1:8080//?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep flag""
```

# Fix

- On est ici sur une faille de `Referent Validation`, ou `Contrôle d’accès insuffisant`.

- Ne pas faire confiance aux **données d'entrée**, car les attaquants peuvent **contrôler toutes les données envoyées à l'application**.

- S'assurer que l'application web a des mécanismes **d'authentification** et **d'autorisation** robustes en place comme des **sessions**, des **tokens**, de **roles** etc...

```PHP
session_start();
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header("location: login.php");
    exit;
}
```

```PHP
if ($_SESSION['role'] !== 'admin') {
    die('Access denied');
}
```
