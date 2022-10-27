# stop on first error
set -e

apt-get install openssh-server -y
service ssh restart
