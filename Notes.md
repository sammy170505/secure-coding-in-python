# Personal Notes on the Project

> Before installing any software, check for vulenrablities at *synk Advisor*.

## 01_02_Begin

- Pipfile = To keep track of dependencies
- Pipfile.lock = use hashes to ensure the integrity of the project's dependencies
- ``` python3 -m pipenv graph ``` = Show currently installed dependencies in graph

## 01_03

- ``` python3 -m pipenv check ``` 
  - Found 5 Vulenrablities in Flask and Setup tools
  - **DO NOT** ``` python3 -m pipenv update ``` = Updates all dependencies to the latest version
    - This can break the project if the latest version is not compatible with the code, or if the latest version has a new vulnerability.

  - Checked Flask Installation
    - Noticed pip show flask showed different versions inside and outside the Pipenv shell.
    - Realized Flask was not installed in the Pipenv environment, even though it was listed in the Pipfile.
    - ``` python3 -m pipenv install flask ``` = Install Flask in the Pipenv environment
    > This will also update the Pipfile.lock with the correct version of Flask.
    - ``` python3 -m pipenv run flask --version ``` = Check Flask version in the Pipenv environment 
  
  - Similar process for setuptools
    - ``` python3 -m pipenv install --upgrade setuptools ``` = Install Setuptools in the Pipenv environment
    - ``` python3 -m pipenv run python3 -m pip show setuptools ``` = Check Setuptools version in the Pipenv environment
