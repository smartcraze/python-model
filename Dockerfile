FROM ubuntu:22.04


RUN apt-get update && apt-get install -y \
    build-essential \
    apt-get install -y python3 python3-venv python3-pip && \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*
    
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1



WORKDIR /app

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
