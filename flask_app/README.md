# Flask Classification App
> Daniel Conway and Alex Powers

## Running the app
It is as easy as:
```bash
cd path-to/thee-flying-chicken/flask_app/
source ./venv/bin/activate
python app.py
```


## Setup venv (virtual python environment)

Move to the flask_app directory
```bash
cd path-to/thee-flying-chicken/flask_app
```

If you do not have virtualenv, do the following:
```bash
pip install virtualenv
```

Create the venv file (only needs to be done the first time)
```bash
virtualenv -p python3 venv
```

Activate virtual environment
```bash
source ./venv/bin/activate
```

Install the required packages
```bash
pip install -r requirements.txt
```

Any additional packages should be installed in the virtual environment and you should update the requirements.txt using
```bash
source ./venv/bin/activate
pip freeze > requirements.txt
```