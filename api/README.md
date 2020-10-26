# Banco de México

This microservice is in charge to make api request and save data into mysql database.

This project contains the following functionalities:

1. Get UDIS value
2. Get USD value

## Project Structure

```
Integrations-Microservice/
    models/
        external.py                         // Model with the external requests handling
    common/
        utils.py                            // The utilities that can be shared between a lot of files
    decorators/
        auth.py                             // Decorator for authenticated routes
        dataType.py                         // Decorator for matching json structures
    .env.example                            // Environment variables example
    application.py                          // The file with the context of the FlaskAPI
    config.py                               // File which loads all environment
    dev_requirements.txt                    // Requirements for development
    Dockerfile                              // File with the logic for Docker
    manage.py                               // Server manager
    README.md                               // Instructions file
    requirements.txt                        // Requirements for the application
```

## Running Locally

### Install Dependencies/Requirements

1. Python `>= 3.8.6`
2. pip `>=20.2.4`
3. virtualenv
4. MySQL instance runninng

First, create a virtualenv in order to install the requirements.

`virtualenv -p python3.7.3 venv`

Then run

`source venv/bin/activate`
`pip install -r requirements.txt`

### Run project
1. Run `pip install -r dev_requirements.txt` when the virtual environment is activated
3. Create `.env` file from the `.env.example` template
3. Run `FLASK_APP=manage.py FLASK_ENV=development DEBUG=True flask run -p 5000 ` in the terminal
