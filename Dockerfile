FROM python:3
EXPOSE 8000

RUN git clone https://github.com/Glico21/NapoleonHomework.git
#COPY requirements.txt /NapoleonHomework/
RUN pip install --no-cache-dir -r /NapoleonHomework/requirements.txt
#COPY . /NapoleonHomework/
