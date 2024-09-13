# WEIGHTLIFTINGPROJECT

This is the new API for a club of weightlifting. 
## Branch
1. develop ->
2. prod -> 
## Project Structure

- 📂 *my_project/*
  - 📂 *app/*
    - 📂 *api/*
      - 📂 *routers/*
    - 📂 *models/*
    - 📂 *dependencies/*
    - 📂 *utilities/*
 
  - 📂 *tests/*
    - 📂 *api/*
    - 📂 *services/*
  - 📄 *main.py*
  - 📄 *.env*
  - 📄 *requirements.txt*


### Directory Descriptions

- *alembic/*: Contains Alembic configurations and migration scripts.
- *app/*: The main application code.
  - *api/routes/*: Defines all API endpoints, organized by resource or entity.
  - *services/*: Houses the business logic and handles database communication.
  - *models/*: Contains SQLAlchemy models, representing the database tables.
  - *dependencies/*: Dependencies that get injected into the routes, such as database sessions.
  - *utilities/*: Helper functions and classes used throughout the project
- *tests/*: Unit and integration tests for the application.
- *main.py*: The main entry point where the FastAPI application is instantiated.
- *.env*: Environment variables and secret configurations.
- *requirements.txt*: List of project dependencies.

## Main Libraries

- *FastAPI*: A modern, fast web framework for building APIs with Python.

- *SQLAlchemy*: ORM to handle database operations.


- *decouple (optional)*: Library for handling secrets and environment variables.

## Initial Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies using pip install -r requirements.txt.
4. Set up environment variables in .env.

For more instructions on how to use and deploy the project, (add pertinent instructions).

## Contributing

Instructions on how other developers can contribute to the project, coding rules, etc.

## License

Licensing information for the project, if any.

## Start up 

python -m venv venv
source venv/bin/activate