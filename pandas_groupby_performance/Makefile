VERSION := 1.5.2
PY3 := python3.8
VENV_PATH := ~/venvs/
VENV := $(VENV_PATH)/$(VERSION)/
PYTHON := $(VENV)/bin/python
INSTALL_STAMP := $(VENV)/.install.stamp

$(PYTHON):
		mkdir -p ~/venvs
		$(PY3) -m venv $(VENV)

install: $(INSTALL_STAMP)
$(INSTALL_STAMP): $(PYTHON)
		$(PYTHON) -m pip install pandas==$(VERSION) matplotlib
		touch $(INSTALL_STAMP)

run: $(INSTALL_STAMP)
		$(PYTHON) main.py

.PHONY: clean
clean:
		find . -type d -name "__pycache__" | xargs rm -rf {};
		rm -rf $(VENV) $(INSTALL_STAMP)
