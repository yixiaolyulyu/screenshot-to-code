FROM python:3.12.3-slim-bullseye

ENV POETRY_VERSION=1.8.0 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies (ffmpeg is required by moviepy for video features)
RUN apt-get update \
 && apt-get install -y --no-install-recommends ffmpeg \
 && rm -rf /var/lib/apt/lists/* \
 && pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Set work directory
WORKDIR /app

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /app/

# Disable the creation of virtual environments and install only main deps
RUN poetry config virtualenvs.create false \
 && poetry install --only main --no-interaction --no-ansi

# Copy the current directory contents into the container at /app
COPY ./ /app/

# Render / Fly / generic PaaS inject $PORT; default to 7001 for local docker run
ENV PORT=7001
EXPOSE 7001

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
