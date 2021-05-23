# UUID API
![example workflow](https://github.com/iamr0b0tx/uuid-api/actions/workflows/main.yml/badge.svg) <br>
Generate and return all UUIDs generated

### Database Specifications
- UUID file fields:
    - ID – (mandatory, integer, unique)
    - UUID – (mandatory, string, cannot be larger than 128
    characters)
    - timestamp – (mandatory, Datetime, cannot be in the past)

## API specifications
- UUID API:
    - The route `UUID` will return the specific all UUIDs including a new one generated when the api was called

## Project setup
Before going through the steps make sure you have the following pre-installed

### Tools and Resources
1. Python 3.6+
2. Virtualenv
3. Postgresql 
    1. Download the application [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). 
    2. Install Postgresql and set up root (postgres). [link](https://www.postgresqltutorial.com/install-postgresql/)
    3. Set up two databases namely __uuid_db__ and __uuid_test_db__.
    

Make sure to download/clone this repository and navigate to the folder in your terminal. Now follow the instructions below

1. Create the virtual environment.
```
    virtualenv /path/to/venv --python=/path/to/python3
```
You can find out the path to your `python3` interpreter with the command `which python3`.

2. Set up `.env` file by duplicating the `.example.env` file(and editing if required).

3. Activate the environment and install dependencies.
    - #### Linux
    ```
        source /path/to/venv/bin/activate
        pip install -r requirements\dev.linux.txt
    ```

    - #### Windows
    ```
        ./path/to/venv/bin/activate
        pip install -r requirements\dev.windows.txt
    ```

4. Launch the service
```
    uvicorn main:app --workers 1 --host 0.0.0.0 --port 8008
```

## Posting requests locally
When the service is running, try this link in your browser/Postman. send a GET request
```
    127.0.0.1:8008/uuid
```

You can test the project with pytest by running the command. You can check Github Actions for the status of tests [here](https://github.com/iamr0b0tx/uuid-api/actions) 
```
    pytest
```

This project id based heavily on this setup [Audio Files API](https://github.com/iamr0b0tx/audio_files_api)

# Refrences
1. deploy_DL_project Repository. [link](https://github.com/Semicolon-Tech/deploy_DL_project_with_fastapi)
2. FastAPI Documentation. [link](https://fastapi.tiangolo.com/)
3. Requests Documentation. [link](https://requests.readthedocs.io/en/master/)
4. Pytest Documentation. [link](https://docs.pytest.org/en/stable/contents.html)
5. Flask Documentation. [link](https://flask.palletsprojects.com/en/1.1.x/)
