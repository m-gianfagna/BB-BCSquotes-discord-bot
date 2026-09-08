FROM python:3.10-slim

# Work directory inside the container
WORKDIR /app

# Copy the requirements' files and install dependencies directly in the container system
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project’s code into the container
COPY . .

# Start command for the bot
CMD ["python3", "bot.py"]