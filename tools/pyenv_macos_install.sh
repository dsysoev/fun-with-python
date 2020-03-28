# example:
# bash pyenv_macos_install.sh my-awesome-project 3.5.3 requirements.txt

ENV_NAME=$1
PYTHON_VERSION=$2
PYTHON_REQUIREMENTS_FILE=$3

# chech os type
if ! [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Tested only on Mac OS 10.15"
  exit 1
fi

# install homebrew
if ! [ -x "$(command -v brew)" ]; then
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

# install pyenv + python specific (PYTHON_VERSION) version
if ! [ -x "$(command -v pyenv)" ]; then
  pip3 install --upgrade pip
  # grand rules for folder /usr/local/share
  # need for man documents
  sudo chown -R "$USER" /usr/local/share
  # install pyenv
  brew install pyenv
  # install pyenv-virtualenv
  brew install pyenv-virtualenv
  # update parameters of enviroment
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  # add option for fix bug with matplotlib on macos
  env PYTHON_CONFIGURE_OPTS="--enable-framework CC=clang" pyenv install -v "${PYTHON_VERSION}"
  # initialize terminal
  reset
fi

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
# create enviroment
pyenv virtualenv "${PYTHON_VERSION}" "${ENV_NAME}"
# activate enviroment
pyenv activate "${ENV_NAME}"
# update pip
pip install --upgrade pip
# install requrements from file
pip install -r "${PYTHON_REQUIREMENTS_FILE}"
