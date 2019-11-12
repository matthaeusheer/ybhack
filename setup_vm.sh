YBHACK_DIR=$(realpath "$(dirname "${BASH_SOURCE[0]}")")

# Set colors for console output
red=$'\e[1;31m'
green=$'\e[1;32m'
cyan=$'\e[96m'
end=$'\e[0m'

printf "[${red} ========== INSTALLATION SCRIPT FOR VM SETUP ==========${end}]\n"

# Fix locale thing on VM
export LC_ALL=C

# Install pip
printf "[${red}Installing pip...${end}]\n"
sudo apt install python-pip -y
pip install --upgrade pip

# Install pipenv
printf "[${red}Installing pipenv...${end}]\n"

pip install pipenv

# Install pyenv
printf "[${red}Installing pyenv...${end}]\n"

git clone https://github.com/pyenv/pyenv.git ~/.pyenv

printf " -----> ${cyan}Do you want to add pyenv stuff to ~/.bashrc [y/n]?...${end}\n"
printf "${cyan}Note: If you ran this script once already press [n/N] (since it's already in you ~/.bashrc)?${end}\n"
read ADD_PYENV_SOURCE
if [[ ADD_PYENV_SOURCE == "Y" || ADD_PYENV_SOURCE == "y" ]]; then
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
fi

# The following will resolve common build issues with newer python versions when using pyenv install 3.7.5 for example
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl
source ~/.bashrc

# Install python
printf "[${red}Installing python 3.7.5 using pyenv...${end}]\n"
sudo apt install zlib1g-dev
pyenv install 3.7.5

# Setup virtualenv stuff
printf "[${red}Installing pipenv dependencies and initializing pipenv sub shell...${end}]\n"
pipenv install
pipenv shell
python -m ipykernel install --user --name ybhack --display-name "ybhack_env"

printf "[${green}[YBHACK INSTALLTION] Congratulations. Everything is setup and ready to go.!${end}]\n"
