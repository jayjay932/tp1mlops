# TP MLOps — Déploiement d'un modèle ML

**Auteur :** Jason Mampouya

## Objectif

Déployer un modèle de prédiction de prix de maisons, en local puis dans le cloud, avec Streamlit, FastAPI et Docker.

## Étapes réalisées

### 1. Entraînement du modèle
`train_model.py` charge `houses.csv`, entraîne une régression linéaire (taille, chambres, jardin → prix) et sauvegarde le modèle dans `regression.joblib`.

```bash
python train_model.py
```

### 2. App Streamlit
`model_app.py` charge le modèle et affiche un formulaire (taille, chambres, jardin) pour prédire un prix en direct.

```bash
streamlit run model_app.py
```

### 3. API FastAPI
`main.py` expose le modèle via un endpoint `/predict` (GET et POST), avec les paramètres `size`, `nb_rooms`, `garden`.

```bash
uvicorn main:app --reload
```

Test : `http://127.0.0.1:8000/predict?size=100&nb_rooms=2&garden=0`

### 4. Déploiement sur machine distante (SSH)
Connexion SSH à la VM du formateur, envoi des fichiers avec `scp`, puis lancement du serveur avec `--host 0.0.0.0` pour le rendre accessible depuis l'extérieur.

```bash
scp main.py regression.joblib houses.csv ubuntu@<IP>:/home/ubuntu/<initiales>/
ssh ubuntu@<IP>
uvicorn main:app --host 0.0.0.0 --port <port>
```

### 5. Dockerisation en local
Un `Dockerfile` package l'API dans une image Docker.

```bash
docker build -t model-api .
docker run -p 8000:8000 model-api
```

### 6. Déploiement Docker sur la VM cloud
Mêmes fichiers envoyés sur la VM, puis build et run de l'image directement là-bas.

```bash
sudo docker build -t model-api .
sudo docker run -d -p <port>:8000 model-api
```

## Fichiers du projet

| Fichier | Rôle |
|---|---|
| `train_model.py` | Entraîne et sauvegarde le modèle |
| `houses.csv` | Données d'entraînement |
| `regression.joblib` | Modèle entraîné |
| `model_app.py` | Interface Streamlit |
| `main.py` | API FastAPI |
| `Dockerfile` | Instructions pour construire l'image Docker |
| `requirements.txt` | Dépendances Python |

## Ce que j'ai retenu

- Un service web (FastAPI) permet des prédictions en temps réel, contrairement au batch processing.
- Docker permet d'emballer l'app avec ses dépendances pour qu'elle tourne pareil partout.
- L'option `-p` de `docker run` et `--host 0.0.0.0` sont nécessaires pour rendre un service accessible depuis l'extérieur.