# Recherche

- On peut trouver en bas de la page d'accueil un bouton **LEAVE A FEEDBACK** qui nous amène sur une page où l'on peut rentrer un nom et un message. Les messages sont ensuite affichés sur la page.

- Les feedback ont une **limite imposée** de 10 charactères pour le nom et de 50 charactères pour le message.

# Exploit

- Les **limite imposée** sur la longueur des champs sont modifiables en **modifiant les attributs** `maxlength` des champs `txtName` et `mtxtMessage`.

- On peut exploiter une **faille XSS** en inserant du code **JavaScript** dans le champ **Message** : `<script>alert(1)</script>`. Lorsque le message est affiché, le code **JavaScript est executé**.

- Cette faille permet **d'executer du code JavaScript** sur la page de l'utilisateur. On peut donc **voler des cookies**, **rediriger l'utilisateur** vers un site malveillant, etc...

# Fix

- Échapper les **caractères spéciaux** dans les **entrées utilisateur**.

```PHP
echo htmlspecialchars($_POST['message'], ENT_QUOTES, 'UTF-8');
```

- Valider les **entrées utilisateur** pour s'assurer qu'elles **respectent le format attendu**.

```PHP
if (strlen($_POST['name']) > 50 || strlen($_POST['message']) > 500) {
    die('Input is too long');
}
```

- Utiliser une **bibliothèque de désinfection** pour nettoyer les entrées utilisateur des **éléments potentiellement malveillants**.

```PHP
require_once 'HTMLPurifier.auto.php';

$config = HTMLPurifier_Config::createDefault();
$purifier = new HTMLPurifier($config);
$clean_html = $purifier->purify($_POST['message']);
```
