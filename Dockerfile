FROM python:3.11-slim

WORKDIR /app

# Upgrade pip and install build dependencies
RUN pip install --no-cache-dir --upgrade pip

# Copy project files
COPY . .

# Install dependencies directly from pyproject.toml
RUN pip install --no-cache-dir .

EXPOSE 7860

# Launch Chainlit pointing to the Space port
CMD ["chainlit", "run", "main.py", "--host", "0.0.0.0", "--port", "7860"]
