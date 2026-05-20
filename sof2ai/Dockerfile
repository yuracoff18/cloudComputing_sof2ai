FROM python:3.12-slim

WORKDIR /app

COPY sof2ai/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY sof2ai ./sof2ai

CMD ["uvicorn", "sof2ai.main:app", "--host", "0.0.0.0", "--port", "8000"]