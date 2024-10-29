# Use an official Python runtime as a parent image
# FROM python:3.12-slim

# ENV PYTHONUNBUFFERED 1

# RUN mkdir -p /root/workspace
# COPY requirements.txt /root/workspace/
# WORKDIR /root/workspace

# RUN pip install --upgrade pip\
#     && pip install --upgrade setuptools\
#     && pip install -r requirements.txt

# ベースイメージを指定
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# システム依存関係をインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# 依存関係のファイルをコピー
COPY requirements.txt /app/

# Pythonの依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . /app

# ポートを公開
EXPOSE 8000

# アプリケーションを起動
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]