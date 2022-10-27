# Check is cuda works
python -c "import torch; print('torch.cuda.is_available() {}'.format(torch.cuda.is_available())); print('torch.cuda.device_count() {}'.format(torch.cuda.device_count())); print('torch.cuda.device(0) {}'.format(torch.cuda.device(0))); print('torch.cuda.get_device_name(0) {}'.format(torch.cuda.get_device_name(0)))"

