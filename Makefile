.PHONY: venv install run clean

# Create the venv and automatically install dependencies
venv:
	@if [ ! -d "venv" ]; then \
		echo "Creating virtual environment venv..."; \
		python3 -m venv venv; \
	fi
	@echo "Updating pip and installing requirements..."
	@./venv/Scripts/python -m pip install --upgrade pip || ./venv/bin/python -m pip install --upgrade pip
	@./venv/Scripts/pip install -r requirements.txt || ./venv/bin/pip install -r requirements.txt

install: venv

run: venv
	@./venv/Scripts/python bot.py || ./venv/bin/python bot.py

clean:
	rm -rf venv __pycache__ .pytest_cache