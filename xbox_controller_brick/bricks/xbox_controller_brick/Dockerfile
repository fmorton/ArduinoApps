# 1. Use a lightweight official Python image
FROM python:3.11-slim

# 2. Set the workspace directory inside the container
WORKDIR /app

# 3. Copy all your brick's code into the container
COPY . .

# 4. Install dependencies if you have a requirements.txt file
# (If you don't have one, this step skips gracefully)
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# 5. Expose the port your server listens on
EXPOSE 8080

# 6. Run your Python script (Change main.py if your server script has a different name!)
ENV PYTHONUNBUFFERED=1

CMD [ "python", "server.py" ]
