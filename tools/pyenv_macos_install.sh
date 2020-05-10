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
  # add ROOT folder
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
fi

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
# initialize terminal
reset
# add option for fix bug with matplotlib on macos
env PYTHON_CONFIGURE_OPTS="--enable-framework CC=clang" pyenv install -v "${PYTHON_VERSION}"
# create enviroment
pyenv virtualenv "${PYTHON_VERSION}" "${ENV_NAME}"
# activate enviroment
pyenv activate "${ENV_NAME}"
# update pip
pip install --upgrade pip
pip install --upgrade setuptools
# install requrements from file
pip install -r "${PYTHON_REQUIREMENTS_FILE}"

#
#https://github.com/pypa/pip/issues/7254#issuecomment-546119909/
brew update && brew upgrade && brew install openssl
##note: some people report that the dylib files needed in #3 are in the 1.0.2t folder, rather than the lib folder. adjust your path in #2 as needed.
cd /usr/local/Cellar/openssl/1.0.2t/lib
sudo cp libssl.1.0.0.dylib libcrypto.1.0.0.dylib /usr/local/lib/
cd /usr/local/lib
sudo ln -s libssl.1.0.0.dylib libssl.dylib
sudo ln -s libcrypto.1.0.0.dylib libcrypto.dylib

#https://github.com/pyca/pyopenssl/issues/728#issuecomment-390099034
pip uninstall pyOpenSSL