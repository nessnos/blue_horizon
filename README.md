# `Water Quality Explorer for Europe`

This project is a web application developed for a university assignment aimed at analyzing and visualizing public data on water quality in Europe. It leverages data science techniques to provide dynamic exploration and visual representation of water quality metrics, using data from the European Environment Agency (EEA).

## Project Goals

The application enables users to:

- Explore and analyze data related to water quality across various ecosystems in Europe.
- Perform temporal analysis of water quality metrics.

Data is sourced from the European Environment Agency (EEA) databases, available at [eea.europa.eu](https://www.eea.europa.eu).

## Dependencies installation

The dependencies installation is handled in [launching the project](#launching-the-project).

## Setup

### Docker

You now need to launch the `postgres` and `redis` containers with Docker.

> To install Docker, check [https://www.docker.com/](https://www.docker.com/)

After having installed Docker, run the container via dockeer-compose:

```bash
docker compose up -d
```

This created and ran two containers : 
1. `postgres` : the postgres sql server with a database named `waterdata` with POSTGRES_PASSWROD `waterize`
2. `redis`: the message broker to queue and distribute background tasks used by `Celery`

If you want to stop or start the containers use the following commands:

```bash
docker compose down   # Stop the container
docker compose up -d  # Start the container again
```

## Restoring Database

### Postgres SQL

You are going to restore the database with all the water quality data and some others tables/views.

>To install Postgres, check https://www.postgresql.org/download/macosx/

> [!NOTE]  
> MacOS
>  ```bash
> brew install postgresql
>```

Run `init.sh` or `init.ps1`
```bash
./init.sh #MacOs & Linux
./init.ps1 #Windows
```

## Launching the project

To start all app components and restoring the database backup : `Django`, `Vue.js` and `Celery` 

> [!WARNING]  
> Make sure to have a `.env` file containing the `OpenAI` API Key & the parameters for the `Django` database settings in the root folder.


```bash
./launch.sh #MacOs & Linux
./launch.ps1 #Windows
```

> Your backend server will run on port `8000`, you can try to open it on [http://localhost:8000](http://localhost:8000).

> The server typically runs on port `5173`, you can access it from folling link: [http://localhost:5173](http://localhost:5173).

> The celery server will be running in the background for task management.