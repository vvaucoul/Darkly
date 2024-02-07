# Recherche

- Sur la page d'accueil, le **logo NSA bleu** est cliquable et redirige vers : `"index.php?page=media&src=nsa"`.

- Dans le code source de cette nouvelle page, l'image est générée par la balise `<object>` qui va recuperer la valeur de `src` dans **l'URL**.

# Exploit

- C'est une faille de type **XSS (Cross-Site Scripting)**.

- Les attaques XSS permettent à un utilisateur malveillant **d'exécuter du code JavaScript** arbitraire dans le navigateur de la victime.

- On peut alors modifier la valeur de `src` pour y mettre du code JavaScript en base64.

- On utilise ici une alerte comme un **exemple simple**. Lorsqu'on teste pour des vulnérabilités XSS, une alerte JavaScript est souvent utilisée car elle est facile à voir et à comprendre. Si le code JavaScript `alert(1)` s'exécute et qu'une boîte d'alerte apparaît, cela signifie que le site est **vulnérable** aux attaques XSS.

- Cependant, dans une attaque réelle, **un attaquant pourrait injecter n'importe quel code JavaScript malveillant**, pas seulement une alerte.

- On peut ainsi afficher une **alerte en HTML** avec: `<script>alert(1)</script>`

- Pour l'inclure, il faut **encoder** le code HTML en **base64**, ce qui donne: `PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`

- On peut ainsi modifier la valeur de `src` dans **l'URL** et mettre : `data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`

# Fix

- Utiliser des balises plus **sûres** comme `<img>` pour afficher des images, plutôt que `<object>` qui peut charger différents types de contenu.

```HTML
<img src="image_url_here" alt="Image">
```
- Valider toutes les **entrées utilisateur** pour s'assurer qu'elles respectent le **format attendu**, notamment pour les **URL**.

```PHP
$src = filter_var($_GET['src'], FILTER_VALIDATE_URL);
if (!$src) {
    die('Invalid URL');
}
```

- Verifier que les **caractères spéciaux** sont traités comme **du texte et non comme du code**.

```PHP
echo '<object data="' . htmlspecialchars($src, ENT_QUOTES, 'UTF-8') . '"></object>';
```
