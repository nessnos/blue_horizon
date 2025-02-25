# `Water Quality Explorer for Europe`

This project is a web application developed for a university assignment aimed at analyzing and visualizing public data on water quality in Europe. It leverages data science techniques to provide dynamic exploration and visual representation of water quality metrics, using data from the European Environment Agency (EEA).

## Project Goals

The application enables users to:

- Explore and analyze data related to water quality across various ecosystems in Europe.
- Perform temporal analysis of water quality metrics.

Data is sourced from the European Environment Agency (EEA) databases, available at [eea.europa.eu](https://www.eea.europa.eu).

## Dependencies installation

### Python

> We use Poetry to manage Python dependencies. If you don't have Poetry installed, you can follow the instructions in the [official documentation](https://python-poetry.org/).

To install all the necessary backend dependencies, run:
 
```bash
poetry install
```

### NPM

> Make sure NPM and Node.js is installed, use NVM to make it easier https://github.com/nvm-sh/nvm

To install frontend dependencies run:

```bash
npm --prefix webapp install
```
# Setup

### Docker

You now need to launch the `postgres` container with Docker.

> To install Docker, check [https://www.docker.com/](https://www.docker.com/)

After having installed Docker, start the container:

```bash
docker run --name waterdb -d -p 5422:5432 -e POSTGRES_PASSWORD=waterize postgres:15-bullseye
```

This created and ran a container named `waterdb` and set the `POSTGRES_PASSWORD` to `waterize`.

### Postgres

To create the `waterdata` database in your container, open a shell in your container and log in as a `postgres` user:

```bash
docker exec -it waterdb  psql -h localhost -U postgres 
```

Create the database:

```postgresql
CREATE DATABASE waterdata;
```

To leave the shell use this command:
```postgresql
\q
```
Your PostgreSQL database is now running inside the Docker container. You can connect to it from your host machine using:

```bash
psql -h localhost -p 5422 -U postgres -d waterdata
```
(You'll be prompted for the password: `waterize`.)

If you want to stop or start the container use the following commands:

```bash
docker stop waterdb   # Stop the container
docker start waterdb  # Start the container again
```

# Running the project

### Django

To start the backend server:

```bash
poetry run python manage.py runserver
```

> Your web server will run on port `8000`, you can try to open it on [http://localhost:8000](http://localhost:8000).

### Webapp

> Before starting Vue.js server, move to webapp directory.

```bash
npm run dev
```

> The server typically runs on port `5173`, you can access it from folling link: [http://localhost:5173](http://localhost:5173).
