FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --no-cache-dir "pydantic[email]<2"

COPY ./app /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]