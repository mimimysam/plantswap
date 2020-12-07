Plant Swap facilitates local plant swaps.

# Requirements:
## Pip or pip3 

The macOS comes with Python installed. But to make sure that you have Python installed open the terminal and run the following command.
`python --version`

To upgrade: 

`pip3 install --upgrade pip --user`

## Django 
`pip3 install django==3.1.4`

# Optional 
If using virtual environment,
`pip3 install venv`

`source venv/bin/activate`

to deactivate:
`deactivate`

# Run DB migrations:
`python manage.py migrate`

# Start Server:
`python manage.py runserver`

The server will be running on http://127.0.0.1:8000 for development.
