# Update nodejs if needed

Check nodejs version (should be 5+)

```bash
node --version
```

if version lower than 5.

```bash
# for show plotly charts need install nodejs 5+ version
# Tested on my machine Ubuntu 18.04.3 LTS
sudo apt-get purge nodejs npm
# install from here
# https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions-enterprise-linux-fedora-and-snap-packages
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
```

# Install jupyterlab

```bash
# create new virtualenv
mkvirtualenv --python /usr/bin/python3 lab
# install packages
pip install jupyterlab nbconvert plotly altair matplotlib seaborn pandas numpy psutil ipympl
```

# Install batteries

```bash
workon lab
# interactive matplotlib plots
# https://github.com/matplotlib/jupyter-matplotlib
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install jupyter-matplotlib

# table of contents extension
# https://github.com/jupyterlab/jupyterlab-toc
jupyter labextension install @jupyterlab/toc

# drawing diagram
# https://github.com/QuantStack/jupyterlab-drawio
jupyter labextension install jupyterlab-drawio

# ipywidgets
# https://github.com/jupyter-widgets/ipywidgets/blob/master/docs/source/user_install.md
jupyter labextension install @jupyter-widgets/jupyterlab-manager

# dark themes
jupyter labextension install @jupyterlab/theme-dark-extension
jupyter labextension install @oriolmirosa/jupyterlab_materialdarker

# Go to definition
# https://github.com/krassowski/jupyterlab-go-to-definition
jupyter labextension install @krassowski/jupyterlab_go_to_definition

# plotly https://plot.ly/python/renderers/
jupyter labextension install @jupyterlab/plotly-extension
```

After this just run
```bash
workon lab
jupyter-lab .
# and open demo.ipynb
```

# Convert notebook to beautiful presentation

```bash
jupyter nbconvert --to slides demo.ipynb
# and open in browser
browse demo.slides.html
```

# Helpful links

-
https://github.com/mauhai/awesome-jupyterlab
