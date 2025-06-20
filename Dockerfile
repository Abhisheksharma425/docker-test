FROM python:3.10-slim

WORKDIR /app
COPY . .

# Install Flask and Ngrok
RUN apt-get update && apt-get install -y \
    curl gnupg2 lsb-release apt-transport-https unzip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add Ngrok’s GPG key and repo
RUN curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
    | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null

RUN echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
    | tee /etc/apt/sources.list.d/ngrok.list

# Update and install ngrok
RUN apt-get update && apt-get install -y ngrok
# Copy files


# Expose Flask port
EXPOSE 5000

# Start both Flask and Ngrok
CMD ["sh", "-c", "python server.py & ngrok start --config=ngrok.yml --all"]
