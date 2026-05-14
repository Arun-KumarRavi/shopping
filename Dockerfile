FROM python:3.11-slim

WORKDIR /app

# Copy the entire project
COPY . .

# Install dependencies from the app subdirectory
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Set the working directory to where app.py is or ensure the path is correct
# We run from the root so that database.db is created in a predictable location
CMD ["python", "app/app.py"]
