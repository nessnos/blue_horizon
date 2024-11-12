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
