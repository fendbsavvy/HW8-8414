# INSTALLATION Guide

This guide walks you through setting up a development environment from scratch, configuring the secrets file, and running the app via `make up`.

---

#Clone the repository or use a tool like SCP to move from local system to EC2

  
# Ensure required tools are installed
  **python3, python3-venv**
    sudo apt update
    sudo apt install -y python3 python3-venv

  **docker.io**
    sudo apt install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker

  **docker-compose**
    sudo apt install -y docker-compose

  **make**
    sudo apt install -y make


# Create and activate virtual environment
  (inside project directory)
  python3 -m venv venv
  source venv/bin/activate



# Create secrets (see Section 4 for details)
  mkdir -p .streamlit
  cd <project folder>/.streamlit
  nano .streamlit/secrets.toml
  (Get Gemini AI key from https://aistudio.google.com/app/u/1/apikey)
  (add AI key to secrets file in this format GEMINI_API_KEY = "AIza....")

# Run
  make up
# Open http://<IP or localhost>:8501

# Check error
  make logs
