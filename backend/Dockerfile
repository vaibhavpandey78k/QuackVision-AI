FROM python:3.11

WORKDIR /app

# Install FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN python -m pip install \
    --default-timeout=1000 \
    --retries=20 \
    --no-cache-dir \
    -r requirements.txt

# Copy the remaining source code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]