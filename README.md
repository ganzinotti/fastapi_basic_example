# Basic Data Sciende Model API with fastapi

This repository is mainly made for my personal learning journey.

Sources:

- <https://github.com/tiangolo/fastapi>
- <https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html>
- <https://www.youtube.com/watch?v=mkDxuRvKUL8>

## setup Python environment

- pip install -r requirements-dev.txt

## launch API in docker

- docker build -t fastapi .
- docker run -p 8000:8000 fastapi
- test endpoints
  - <http://localhost:8000/docs>
