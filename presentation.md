---
marp: true
theme: gaia
footer: Jonny Saykosy - 2022
---

# Presentation

##### Struture et processus métier

- Clients protentiels
- Conversion du client
- Clients existants
- Signature des contrats
- Évènement créé
- Équipe de support affectée à l'évènement

---

- Gérer l'évènement
- Évènement terminé
- Signature d'un nouveau contrat

---

##### Diagramme fonctionnelle

---

#### Exigences techniques

- Django avec site d'administration Django
- Django REST Framework
- PostreSQL

---

- Python 3
- Protection contre SQL injection avec Django ORM
- Authentification
- Permissions
- Logging et surveillance avec Sentry

---

##### Fonctionnalités de haut niveau

1. Admin et management:

- Accès et modifications de tous les clients, contracts et évènements, ainsi que des utilisateurs (employés)

2. Vente

- Accès et modifications des clients, contracts et évènements dont ils sont responsables

---

3. Support

- Accès à tous les clients, contracts et évènements dont ils sont responsables
- Modifications des évènements dont ils sont responsables
