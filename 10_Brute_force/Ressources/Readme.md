# Recherche

- Sur la **page d'accueil**, nous avons un bouton `SIGN IN` qui nous **redirige** vers une **page de connexion**.

# Exploit

- On peut essayer une attaque **brute force** pour se connecter. Il existe de **nombreux utilitaires** pour ça, notamment:
  - `hydra`
  - `patator`.
  - `Medusa`,
  - `Ncrack`,
  - `Crowbar`,
  - `Brutus`,
  - `Wfuzz`,
  - `John the Ripper`,
  - ...

- Utiliser un **dictionnaire de mots de passe** permet de réduire la durée de **brute force**. La liste `rockyou` est une liste de **mots de passe** qui est **souvent utilisée** pour ce genre d'attaque.

- On peux alors lancer **hydra** avec le dictionnaire `rockyou` et
utilise le login `admin` puisque c'est un des **identifiants les plus courants**.

```bash
hydra -l admin -P rockyou.txt -F 127.0.0.1 http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif' -s 8080'
# ...
[80][http-get-form] host: 127.0.0.1   login: admin   password: shadow
```

- Si `admin` n'avait **pas** été le bon login, on aurait également pu utiliser **hydra** avec un **autre dictionnaire** pour **casser le login**.


# Fix

- **Ralentir** les attaques  :

  - Exiger que les utilisateurs créent des **mots de passe forts** qui sont **difficiles** à casser. Cela inclut l'utilisation d'une combinaison de lettres **majuscules** et **minuscules**, de **chiffres** et de **caractères spéciaux**.

  - S'assurer que les mots de passe sont **correctement hashés et salés** dans la base de données.

  - Introduire un **délai d'attente** entre les tentatives de connexion ou une **nombre maximal de tentatives de connexions** dans un certain **laps de temps**.

- **Interrompre** les attaques :

  - Implémenter un **système de verrouillage** de compte qui **bloque** un compte utilisateur après un **certain nombre de tentatives de connexion** et qui nécessite une **réinitialisation du mot de passe** pour déverrouiller le compte via une **authentification à deux facteurs**.

  - Utiliser un système de **captcha**.

  - Utiliser un **Pare-feu d'Application Web** pour **bloquer** les tentatives de **brute force** et autres **attaques communes**.
