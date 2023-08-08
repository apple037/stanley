FROM python:3.9-slim
WORKDIR /bot
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "-u", "main.py"]