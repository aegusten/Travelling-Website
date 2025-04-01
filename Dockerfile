FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements/requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy project
COPY . /code/

# Expose port and start server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]