#!/bin/bash

# Create audioscribe directory and change into it
mkdir audioscribe
cd audioscribe

# Create package directory and __init__.py
mkdir audioscribe
touch audioscribe/__init__.py

# Create remaining Python files
touch audioscribe/cli.py
touch audioscribe/config.py
touch audioscribe/exceptions.py
touch audioscribe/transcriber.py
touch audioscribe/utils.py

# Create docs directory and files
mkdir docs
touch docs/index.md
mkdir docs/technical_docs

# Create remaining files
touch Dockerfile
touch docker-compose.yml
touch LICENSE
touch README.md
touch requirements.txt
mkdir scripts
touch scripts/create_directories.sh
touch scripts/generate_readme.sh
touch setup.cfg
touch setup.py

# Create tests directory and files
mkdir tests
touch tests/__init__.py
touch tests/test_transcriber.py

# Output success message
echo "Audioscribe directory structure and files created successfully"
