FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD correct pour Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
