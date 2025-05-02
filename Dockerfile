FROM python:3.11.5

RUN mkdir /max_wb_tgbot

WORKDIR /max_wb_tgbot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
