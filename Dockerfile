FROM python:3
EXPOSE 8000

RUN git clone https://github.com/Glico21/NapoleonHomework.git
RUN pip install --no-cache-dir -r /NapoleonHomework/requirements.txt
