FROM ubuntu:latest
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt
RUN mkdir -p /usr/local/nltk_data
RUN [ "python3", "-c", "import nltk; nltk.download('punkt', download_dir='/usr/local/nltk_data')"] 
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader omw-1.4
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
