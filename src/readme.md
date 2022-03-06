## This is a simple Blockchain example develop with Python

## Python version used for this project. 
    Python 3.9.7    
    
## Install virtualenv tool (global). 
    pip install virtualenv   

## Go to blockchain folder and create and activate environment. 
    python -m venv venv 
    cd venv/bin source activate

## Install requirements needed for this project 
    pip install -r requirements.txt

### Go to blockchain/src and run server with below line
    uvicorn main:app --reload


### As response, the previous execution will generate a localhost url, Copy and paste that url in your browser
    
## Finally you can test how a blockchain works