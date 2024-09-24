FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the book_catalog directory contents into the container at /app
COPY book_catalog /app/book_catalog

# Install any dependencies required by the application
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8001

# Command to run the FastAPI app
CMD ["uvicorn", "book_catalog.app.main:app", "--host", "0.0.0.0", "--port", "8001"]



# FROM python:3.9-slim
# WORKDIR /app
# COPY . /app
# RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 8001
# CMD ["uvicorn", "book_catalog.main:app", "--host", "0.0.0.0", "--port", "8001"]