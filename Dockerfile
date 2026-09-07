FROM python:3.13-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr for real-time logs
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Upgrade pip and install build dependencies
RUN python -m pip install --upgrade pip

# Copy dependency manifest first to leverage layer caching
COPY requirements.txt .

# Install requirements directly into system environment
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]