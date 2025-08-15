# My008

docker compose pull && docker compose up -d && docker compose exec inventree-server invoke update


Show one enviroment variable: echo $INVENTREE_CONFIG_FILE

Show all environment variables: env

A short description of the project

## Installation

Add to inventree/src/backend/InvenTree/setttings.py

INSTALLED_APPS += [

    'my008',
    
]

>>> from my008.core import My008App

>>> print(My008App.name)
### InvenTree Plugin Manager

... todo ...

### Command Line 

To install manually via the command line, run the following command:

```bash
pip install my008
```

## Configuration

... todo ...

## Usage

... todo ...
