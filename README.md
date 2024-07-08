# Fake User Profiles API

This project is a FastAPI application that provides a RESTful API for managing fake user profiles. It uses SQLAlchemy for ORM, Alembic for database migrations, and PostgreSQL as the database.

## Features

- Create, read, update, and delete user profiles
- Upload profile pictures
- Database migrations with Alembic
- Fully documented API with Swagger and ReDoc

## Swagger API Documentation

![Swagger API Documentation](https://github.com/Nandhukriss/fakeUserAPI-Fastapi/assets/103727372/b130d0b3-ada5-48cc-8849-31d535c25f96)


## Requirements

- Python 3.8+
- PostgreSQL
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Nandhukriss/fake-user-profiles-api-Fastapi.git
    cd fake-user-profiles-api
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**

    Create a `.env` file in the project root and add the following variables:

    ```env
    DATABASE_URL=postgresql://user:password@localhost/dbname
    ```

    Replace `user`, `password`, `localhost`, and `dbname` with your PostgreSQL credentials and database name.

## Database Setup

**Initialize the database:**

    Make sure your PostgreSQL server is running and then create the database specified in your `.env` file.

## Running the Application

1. **Start the FastAPI application:**

    ```bash
    fastapi dev main.py
    ```

    The API will be available at `http://127.0.0.1:8000`.

2. **Access the API documentation:**

    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Alembic Commands

- **Create a new migration:**

    ```bash
    alembic revision --autogenerate -m "Description of the migration"
    ```

- **Apply migrations:**

    ```bash
    alembic upgrade head
    ```

- **Downgrade migrations:**

    ```bash
    alembic downgrade -1
    ```

