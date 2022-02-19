FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade pandas
RUN pip install --upgrade openpyxl
RUN apt-get install -y mecab
RUN apt-get install -y mecab-ipadic-utf8
RUN pip install mecab-python3
RUN pip install unidic-lite

# RUN python -m pip install jupyterlab
