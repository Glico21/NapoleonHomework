FROM python:3
EXPOSE 8000

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r NapoleonHomework/requirements.txt
