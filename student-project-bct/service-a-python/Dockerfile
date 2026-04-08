FROM python:3.10

WORKDIR /app
# COPY generator.py . 
# COPY validator.py . 
# COPY watcher.py .


COPY . .

RUN pip install -r requirements.txt

RUN mkdir -p data output

EXPOSE 5000

CMD ["python", "app.py"]