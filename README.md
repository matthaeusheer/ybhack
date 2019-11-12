[![Build Status](https://travis-ci.org/matthaeusheer/ybhack.svg?branch=master)](https://travis-ci.org/matthaeusheer/ybhack)

# ybhack
Code repository for the 2019 YB Hackathon.

## Getting Started

### Installation
#### Local
0) Install pyenv: https://github.com/pyenv/pyenv.
1) Install pipenv: ```sudo apt install python-pip``` and ```pip install pipenv```  
    Note: When you started a new VM on Azure, you need to do ```export LC_ALL=C``` before.
2) Go to project root and do ```pipenv install``` and ```pipenv shell```
2) Install an ipykernel for jupyter notebook use  
    ```python -m ipykernel install --user --name ybhack --display-name "ybhack_env"```

#### Cloud VM
##### Create a VM
On Azure -> Virtual Machines -> Create new VM.
##### Basic Installation
- SSH into the machine ```ssh <username>@<public_vm_ip>```.
- Run installation.
```
cd ~
https://github.com/matthaeusheer/ybhack.git
cd ybhack
bash setup_vm.sh
```
##### How to run and access a Jupyter Notebook running on the VM
https://github.com/rgl/azure-content/blob/master/articles/virtual-machines/virtual-machines-linux-jupyter-notebook.md  
Basically (more precise in the link above):
- In the network security group of your vm create a new inbound security role for your jupyter notebook (I chose port 8080)
- Generate am openssl certificate (note the sha1 hash)
- Generate password protection for jupyter notebooks (use python inside your pipenv instead of anaconda in the tutorial)
- Create a jupyter config (you must edit the "azureuser" in the path in the config and password hash and set the port)
- Run the jupyter notebook on your VM
- Get the public IP adress from your VM overview and access the notebook via the port.
- Enjoy.
##### Transferring local data to VM
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