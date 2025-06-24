# HA2Munin

![Munin Logo](custom_components/ha2munin/icon.png)

![Munin Logo](https://raw.githubusercontent.com/Erreur32/ha2munin/main/custom_components/ha2munin/icon.png)


Expose facilement les statistiques de Home Assistant (CPU, RAM, températures, etc) au format compatible Munin, via une simple endpoint HTTP.

---

## Fonctionnalités

- Endpoint `/api/munin` prêt pour interrogation par un plugin Munin externe
- Permet de superviser les données Home Assistant avec Munin
- Installation facile via HACS ou en custom_components

---

## Installation

Ajout dans HACS

-   Ouvre HACS → “Intégrations” → “Dépôts personnalisés”
-   Ajoute : https://github.com/Erreur32/ha2munin
-   Installe l’intégration depuis HACS

## Utilisation

L’intégration expose les valeurs sur :

```bash
http://<homeassistant>:8123/api/munin

```

## TODO

-   Détection automatique des capteurs
-   Paramétrage dynamique des sensors à exporter
-   Documentation améliorée


## Auteur

Erreur32

## Licence

MIT
