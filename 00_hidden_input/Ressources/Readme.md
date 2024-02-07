# Recherche

- On peut trouver sur la page d'accueil un bouton **SIGN IN** qui nous amène sur une page de connexion.

- Si l'on va sur **I forgot my password** il n'y a aucun champs pour rentrer son adresse mail.

- En appuyant sur le bouton **Submit** on peut voir qu'une requête POST est envoyée avec comme paramètre `mail` qui contient l'adresse mail de l'admin.

- En inspectant le code source de la page on peut voir qu'il y a un champ `<input>` caché qui contient l'adresse mail de l'admin.

# Exploit

- Le champ **mail** contient une adresse e-mail qui est exposée dans le code source de la page et visible par tout utilisateur malveillant. Cela peut conduire à des attaques de type **spam** ou **phishing**.

- Dans le cas d'un site réel, appuyer sur le bouton **submit** enverrait l'e-mail contenant le mot de passe **en clair** à l'adresse e-mail spécifiée dans le champ caché `mail`. En enlevant `type="hidden"` du champ, l'utilisateur malveillant pourrait envoyer le **mot de passe de l'administrateur** à une adresse e-mail de son choix.

- En l'absence de mesures d'assainissement adéquates, un utilisateur malveillant pourrait injecter du code dans le champ `mail` en modifiant la requête `POST` pour tenter de **compromettre** le serveur au niveau du traitement de la requête.


# Fix

###### Ne pas exposer d'informations sensibles dans le code source de la page visible par les utilisateurs. Si l'adresse e-mail doit être utilisée côté serveur, elle devrait être stockée côté serveur et non transmise via le formulaire.

- Stocker l'adresse e-mail dans une variable côté serveur et ne pas l'exposer dans le code source de la page.

```PHP
// Sur le serveur
$mail = "webmaster@borntosec.com";
```


###### Proteger le traitement des requêtes coté serveur pour eviter les potentiels injections de code malveillant.

- Traitement des requêtes côté serveur pour éviter les injections de code malveillant.

```PHP
// Sur le serveur
if (isset($_POST['mail'])) {
    $mail = $_POST['mail'];
    if (strlen($mail) > 15) {
        die('Invalid input');
    }
    // Autres validations...
}
```

- Et/Ou

```PHP
// Sur le serveur
$mail = filter_var($_POST['mail'], FILTER_SANITIZE_EMAIL);
```
