# Punch Clock App

### A punch clock webapp that performs CRUD operations in a Postgres database using SQLAlchemy, FastAPI and Pydantic, hosted on Streamlit and containerized in Docker.

## What is it

The main idea for this project was to build a Punch Clock web application, designed to manage employee check-in and check-out times. The app supports CRUD (Create, Read, Update and Delete) operations and was created following the instructions from [Jornada de Dados - Bootcamp - Python para Dados - Aula 20](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula20), lectured by [Luciano Galvão](https://github.com/lvgalvao).

## Tech stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **Frontend:** Streamlit
- **Containerization:** Docker

## How it works

gif - mermaid - excalidraw

## Folder structure
```
├── backend
│   ├── crud.py
│   ├── database.py
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── router.py
│   └── schemas.py
├── frontend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── .gitignore
├── docker-compose.yaml
└── README.md
```

## Running this project locally with Docker

0. **Before you start, make sure you have the following installed:**

- Docker
- Docker Compose

1. **Create a folder where you want to run this project from:**
```bash
mkdir punch-clock-crud
```

2. **Clone the repository:**

```bash
git clone https://github.com/RStremel/punch-clock-crud.git
```

3. **Access the project folder:**
```bash
cd punch-clock-crud
```

4. **Build the Docker image:**
```bash
docker-compose build
```

5. **Run the Docker container:**
```bash
docker-compose up
```

6. **Access the web app:**
The app will be host in port 8501, so you can access it using the following: 

    http://localhost:8501

## API Endpoints

When running this project, FastAPI will create the following key API endpoints:

- GET "/records/" and "/records/{record_id}": retrieve all or a specific record.
- POST "/records/": create a new record.
- PUT "/records/{record_id}": update an existing record.
- DELETE "/records/{record_id}": delete an existing record.

If you want a more detailed API documentation, you can access it using http://localhost:8000/docs when the app is running.

## Contributing

Contributions to this code are always welcome!



