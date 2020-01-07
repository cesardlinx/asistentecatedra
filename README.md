# Asistente de Cátedra Website

## About

This is the repository for the new [Software Asistente de Cátedra Website](https://www.asistentedecatedra.com).
Please submit additions and fixes as pull requests to [our GitHub repository](https://github.com/cesardlinx/asistentecatedra).

## Setup Instructions
1. Create a .env file based in .env.example
2. Install node dependencies
    ```sh
    $ npm install
    ```
3. Create a virtual environment
    ```sh
    $ virtualenv --python=/usr/bin/python3.7 venv
    ```
4. Activate environment
    ```sh
    $ soruce venv/bin/activate
    ```
5. Install python dependencies
    ```sh
    (venv)$ pip install -r requirements/base.txt
    ```
6. Collect static files
    ```sh
    (venv)$ python manage.py collectstatic
    ```
7. Migrate database
    ```sh
    (venv)$ python manage.py migrate
    ```

## Styles

The style files are in the `static/css/sass` directory and control the complete appearance of this site.
