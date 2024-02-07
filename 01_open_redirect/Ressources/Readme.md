# Recherche

- Dans le footer de la page, on trouve 3 liens pour accéder aux réseaux sociaux du site : Facebook, Twitter et Instagram.

- Lorsque l'on inspecte le code source de la page, on peut voir que les liens sont écrits en dur.

# Exploit

- C'est une faille de type **Open Redirect Vulnerability**.

- Les liens vers les réseaux sociaux sont exposés dans le code source de la page, ce qui peut être exploité par des utilisateurs malveillants ou des malwares afin de pieger les utilisateurs locaux et de les rediriger vers des sites malveillants.

- Le risque peut alors être une attaque de type **phishing** à l'aide d'une fausse page de connexion à un réseau social afin de récuperer ses informations.

# Fix

- Ne pas exposer de **redirection ouvertes** dans le code source de la page visible par les utilisateurs. Ne pas permettre aux utilisateurs d'entrer une URL comme destination.

- Utiliser des systemes de redirections sécurisés avec un nom court, un jeton/token ou un identifiant **mappé coté serveur** à l'URL complète.

- Utiliser une **whitelist** pour les URL. Cela permet de s'assurer que les liens ne pointent que vers des sites autorisés.

```PHP
<?php
// Whitelist des sites autorisés pour la redirection
$whitelist = [
    'facebook' => 'https://www.facebook.com',
    'twitter' => 'https://www.twitter.com',
    'instagram' => 'https://www.instagram.com'
];

// Récupération du paramètre site
$siteKey = $_GET['site'];

// Vérification que le site est dans la whitelist avant la redirection
if (array_key_exists($siteKey, $whitelist)) {
    header('Location: ' . $whitelist[$siteKey]);
} else {
    die('Redirection non autorisée');
}
?>
```
