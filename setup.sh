#!/bin/bash

# Create main program directory
#mkdir audioscribe
#cd audioscribe

# Create subdirectories
mkdir audio
#mkdir doc

# Create README file
touch README.md
echo "# Audioscribe" >> README.md
echo "Audioscribe is a command-line tool that transcribes YouTube videos into text." >> README.md
echo "" >> README.md
echo "## Installation" >> README.md
echo "1. Clone the repository" >> README.md
echo "2. Install the required packages by running: \`pip install -r requirements.txt\`" >> README.md
echo "" >> README.md
echo "## Usage" >> README.md
echo "To transcribe a YouTube video, run:" >> README.md
echo "\`python audioscribe.py <youtube_video_url>\`" >> README.md
echo "" >> README.md
echo "## Contributing" >> README.md
echo "Contributions are welcome! Please see CONTRIBUTING.md for more information." >> README.md

# Create requirements file
touch requirements.txt
echo "google-auth==1.35.0" >> requirements.txt
echo "google-auth-oauthlib==0.4.6" >> requirements.txt
echo "google-auth-httplib2==0.4.6" >> requirements.txt
echo "google-api-python-client==2.22.0" >> requirements.txt

# Create Dockerfile
touch Dockerfile
echo "FROM python:3.9" >> Dockerfile
echo "" >> Dockerfile
echo "WORKDIR /app" >> Dockerfile
echo "" >> Dockerfile
echo "COPY . /app" >> Dockerfile
echo "" >> Dockerfile
echo "RUN pip install --trusted-host pypi.python.org -r requirements.txt" >> Dockerfile
echo "" >> Dockerfile
echo "CMD [\"python\", \"audioscribe.py\"]" >> Dockerfile
