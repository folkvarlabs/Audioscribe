![alt text](https://media.discordapp.net/attachments/1051385609769472020/1091141838141919252/cywf_Youre_on_a_journey_through_a_dense_forest_and_you_come_acr_09004d17-fcea-46b5-9835-d3c54b039435.png?width=1138&height=1138)

# Audioscribe

Audioscribe is a command-line tool for transcribing audio from YouTube videos. It uses Google Cloud Speech-to-Text API and OpenAI's Whisper API to perform speech recognition and provide accurate transcriptions of audio content.

Audioscribe now includes isolated virtual environments for each implementation (Python, Rust, and Go) to ensure safe and secure execution of the tool.

Audioscribe can also be run on cloud platforms using Docker. Simply build the Docker image using the provided Dockerfile and Docker Compose file, and run it on your preferred cloud platform.
## New Features (rolling release):

* Audioscribe now launches its own isolated environment for each implementation (Python, Rust, and Go).

* Audioscribe can be run on cloud platforms using Docker.
How it Works:

Sure, I can help you with that. Here are the updated features and revised README:

## How it Works:

Audioscribe is a command-line tool for transcribing audio from YouTube videos. It uses Google Cloud Speech-to-Text API and OpenAI's Whisper API to perform speech recognition and provide accurate transcriptions of audio content.


## Directory Structure:

```lua
├── audioscribe
│   ├── __init__.py
│   ├── audioscribe.py
│   ├── README.md
│   ├── rust
│   │   ├── Cargo.lock
│   │   ├── Cargo.toml
│   │   ├── README.md
│   │   ├── src
│   │   └── target
│   └── go
│       ├── go.mod
│       ├── go.sum
│       ├── main.go
│       └── README.md
├── doc
│   └── technical-docs.md
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── Dockerfile
└── docker-compose.yml
```

## Running Audioscribe:

To run Audioscribe, you can follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the audioscribe directory using the command line.
3. Create a virtual environment for Python implementation:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Create a virtual environment for Rust implementation:

```bash
cd rust
cargo build
Create a virtual environment for Go implementation:
bash
Copy code
cd ../go
go build
```

## Start the program by running:

```shell
python audioscribe.py [YOUTUBE_VIDEO_LINK]
```

The program will then prompt you to select which implementation you want to use for transcription.


Alternatively, you can run Audioscribe on a cloud platform using Docker. Simply build the Docker image using the provided Dockerfile and Docker Compose file, and run it on your preferred cloud platform.

## Technical Documentation:

For technical documentation, please see the [technical-docs.md](docs/technical-docs.md) file.

Let me know if you need any further assistance!