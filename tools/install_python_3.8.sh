# stop on first error
set -e

# https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
apt install -y software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa

# install python 3.8
apt install -y python3.8 python3.8-venv
