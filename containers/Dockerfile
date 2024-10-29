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
COPY containers/requirements.txt /app/

# Pythonの依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
# COPY . /app
COPY ../src/ /app/

# 環境変数を設定（必要に応じて）
ENV PYTHONUNBUFFERED=1

# 静的ファイルを収集
RUN python score/manage.py collectstatic --noinput

# ポートを公開（Herokuでは不要だが、記載しても問題なし）
EXPOSE 8000

# アプリケーションを起動
CMD gunicorn score.wsgi --log-file - --bind 0.0.0.0:$PORT