FROM python:slim

COPY . . 
RUN pip install -r requirements.txt
CMD python telebot_translator.py
