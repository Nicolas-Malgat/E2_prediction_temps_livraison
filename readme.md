- # Contexte

Je suis en formation professionnelle auprès de Simplon. Afin de valider mon titre, je créé un projet qui valide les compétences suivantes:

- Création d'un algorithme de machine learning
- Amélioration d'une IA

Les compétences suivantes ne sont pas concernées par ce projet mais elle sont tout de même présentes:

- Création d'une base de données
- Requêtage d'une base de données
- Creation d'un front end

# Objectif: Prévision du temps de livraison

Il existe de nombreuses informations pour chaque commande, notamment la date d'achat du produit et le lieu d'achat.

<span style="color:#9F9">
Liste des tables utilisées:

- olist_customers_dataset.csv
- olist_geolocation_dataset.csv
- olist_orders_dataset.csv
- olist_order_items_dataset.csv
- olist_products_dataset.csv
- olist_sellers_dataset.csv

</span>

<span style="color:#F99">
Liste des tables inutilisées:

- olist_products_dataset.csv
- olist_order_reviews_dataset.csv
- olist_order_payments_dataset.csv
- product_category_name_translation.csv

</span>


|![Schéma des tables du dataset](documentation/data_schema.png)|
|:--:| 
|*Schéma des tables du dataset*|

## Les améliorations que je souhaite apporter:

- Calcul du temps de trajet (distance de manhattan) à l'aide d'une API
- Ajout de la distance avec la grande ville la plus proche

## Source

Le projet se base sur une base de données du [E-commerce Brésilien](https://www.kaggle.com/olistbr/brazilian-ecommerce).

Un paragraphe présente plusieurs utilisations possible de ce dataset:

    Here are some inspiration for possible outcomes from this dataset.

    - NLP: This dataset offers a supreme environment to parse out the reviews text through its multiple dimensions.
    
    - Clustering: Some customers didn't write a review. But why are they happy or mad?

    - Sales Prediction: With purchase date information you'll be able to predict future sales.

    - Delivery Performance: You will also be able to work through delivery performance and find ways to optimize delivery times.

    - Product Quality: Enjoy yourself discovering the products categories that are more prone to customer insatisfaction.

    - Feature Engineering: Create features from this rich dataset or attach some external public information to it.