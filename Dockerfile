FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    --trusted-host pypi.python.org \
    --retries 10 \
    --timeout 100 \
    -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main_api:app", "--host", "0.0.0.0", "--port", "8000"]