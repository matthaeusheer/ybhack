# ybhack
Code repository for the 2019 YB Hackathon.

## Getting Started

### Installation
0) Install pyenv: https://github.com/pyenv/pyenv.
1) Install pipenv: ```sudo apt install python-pip``` and ```pip install pipenv```
2) Go to project root and do ```pipenv install``` and ```pipenv shell```
2) Install an ipykernel for jupyter notebook use  
    ```python -m ipykernel install --user --name ybhack --display-name "ybhack_env"```

### How To Use
#### YB Hack datasets
The datasets for the challenges are hosted at: https://github.com/fiddi/yb-hackathon-2019-datasets.  
Clone this repo into the <YBHACK_ROOT_REPO>/data, so we can work from a common ground.  
Starting from the repo this README file is located, do:
```
cd data
git clone git@github.com:fiddi/yb-hackathon-2019-datasets.git
```
Everything in the data folder except the the placeholder.txt file is being ignored from git.  
TODO: We might want to have this data stored in cloud buckets for AI stuff later on.

## Contributors
Matthäus Heer, ETH Zurich  
Pétur Helgi Einarsson, ETH Zurich    
Frederik Jensen, Second Spectrum  

## Tests
### CI
Travis setup.

### Running manually
How to run those little buggers.