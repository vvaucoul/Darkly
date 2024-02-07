# Recherche

- On peut trouver dans le menu de la page d'accueil un bouton **Survey** qui nous amène sur une page avec un formulaire où l'on peut choisir des valeurs.

- En modifiant la valeur de la **liste déroulante**, on peut voir qu'une rèquete **POST** est envoyée avec comme paramètre `valeur` qui contient la **valeur de la liste déroulante**.

# Exploit

- Dans le formulaire, on peut modifier la valeur d'un des membres du `<select>` et selectionner cet element pour **envoyer une valeur qui n'est pas dans la liste déroulante**.

```HTML
<option value="100000">100000</option>
```

- Les repercussions de cette faille peuvent être: **l'altération des données**, **l'exécution de code malveillant**, **l'obtention d'informations sensibles**.

# Fix

- Valider toutes les données reçues côté **serveur** pour s'assurer qu'elles **correspondent aux attentes** en termes de **type**, de **taille**, de **format**, et de **plage de valeurs**.

```PHP
$value = $_POST['field_name'];
if (!in_array($value, [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10])) {  // whitelist des valeurs autorisées
    die('Invalid input');
}
```

- Valider toutes les données reçues côté **client** peut offrir une **première ligne de défense**.

```JS
document.getElementById('form').addEventListener('submit', function(e) {
    var value = document.getElementById('field').value;
    if (![1, 2, 3, 4, 5, 6, 7, 8, 9, 10].includes(parseInt(value))) {
        alert('Invalid input');
        e.preventDefault();
    }
});
```
