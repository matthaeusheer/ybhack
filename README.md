[![Build Status](https://travis-ci.org/matthaeusheer/ybhack.svg?branch=master)](https://travis-ci.org/matthaeusheer/ybhack)

# ybhack
Code repository for the 2019 YB Hackathon.

## Getting Started

### Installation
#### Local
0) Install pyenv: https://github.com/pyenv/pyenv.
1) Install pipenv: ```sudo apt install python-pip``` and ```pip install pipenv```  
2) Go to project root and do ```pipenv install``` and ```pipenv shell```
    For newer python versions there seems to be an issue with automatic pythonv version install via pyenv,
    check pyenv common build issues and install the stuff suggested, it'll work.
2) Install an ipykernel for jupyter notebook use  
    ```python -m ipykernel install --user --name ybhack --display-name "ybhack_env"```

#### Cloud VM
##### Create a VM
On Azure -> Virtual Machines -> Create new VM.
#### Basic Installation
- SSH into the machine ```ssh <username>@<public_vm_ip>```.
- Run installation.
```
cd ~
https://github.com/matthaeusheer/ybhack.git
cd ybhack
bash setup_vm.sh
```
#### How to run and access a Jupyter Notebook running on the VM
https://github.com/rgl/azure-content/blob/master/articles/virtual-machines/virtual-machines-linux-jupyter-notebook.md  
Basically (more precise in the link above):
- In the network security group of your vm create a new inbound security role for your jupyter notebook (I chose port 8080)
- Generate am openssl certificate (note the sha1 hash)
- Generate password protection for jupyter notebooks (use python inside your pipenv instead of anaconda in the tutorial)
- Create a jupyter config (you must edit the "azureuser" in the path in the config and password hash and set the port)
- Run the jupyter notebook on your VM ```jupyter notebook notebooks```
- Get the public IP adress from your VM overview and access the notebook via the port <public_ip:port>.
- Enjoy.
#### Transferring local data to VM
```scp -r my_local_data_folder <username>@<public_vm_ip>:/path/to/destination```

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
#### Cloud Storage
TODO: We might want to have data stored in cloud buckets for AI stuff later on and to quickly 
load stuff from the buckets when running on the VM's.

## Tests
### Running manually
Within the pipenv shell run ```python -m unittest discover``` to run tests locally.
### CI
Upon pushing to a branch, CI will trigger a build and run all tests.

## Contributors
Matthäus Heer, ETH Zurich  
Pétur Helgi Einarsson, ETH Zurich    
Frederik Jensen, Second Spectrum  
