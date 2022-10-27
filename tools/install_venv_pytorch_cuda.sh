# stop on first error
set -e

# install venv pytorch_cuda venv
mkdir -p venvs
python3.10 -m venv ~/venvs/pytorch_cuda
source ~/venvs/pytorch_cuda/bin/activate
pip3 install numpy==1.23.4 pandas==1.5.1 jupyterlab==3.4.8 scikit_learn==1.1.2
pip3 install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
