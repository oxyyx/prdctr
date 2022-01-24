# PRDCTR

Exploring the realms of product information management.

PRDCTR (product-er, but _hip_) is an application written to test FastAPI and it's features, in the realm
of [product information management](https://en.wikipedia.org/wiki/Product_information_management). It is - and most
like _always will be_ - an experimental application that is unsafe for production use.

## Getting started

### Bash

```bash
git clone git@github.com:oxyyx/prdctr.git
cd prdctr
poetry install


cp .env.example .env
# Edit the .env file to your desired configuration

bash scripts/run-app.sh
```

### Docker Compose

Alternatively you can run this application using [docker compose](https://docs.docker.com/compose/):

```bash
docker-compose up -d
```