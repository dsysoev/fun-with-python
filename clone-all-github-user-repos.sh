#!/bin/sh
# Pure bash solution for clone first 100 public repos for specific github user

set -e
# github user name
read -p 'Github username: ' NAME
# root folder for clone all repos
read -p 'Root folder for clone: ' FOLDER
# download using https by default (ssh as optional)
read -p "Clone using HTTPS? [y|n]? " REPLY

case $REPLY in
    [y]* ) MASK='clone_url';;
    [n]* ) MASK='ssh_url';;
esac

# replace tilde to HOME path
dir_name="${FOLDER/#\~/$HOME}"
echo "cd $dir_name"
cd "$dir_name"
# magic command
curl -s "https://api.github.com/users/${NAME}/repos?page=1&per_page=100" | grep -e "$MASK" | cut -d '"' -f4 | xargs -i git clone {}
