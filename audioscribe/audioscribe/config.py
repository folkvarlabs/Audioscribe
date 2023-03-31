import os

class Config:
    """Configuration class"""

    # Set the API key
    API_KEY = os.environ.get("AUDIOSCRIBE_API_KEY")
    
    # Set the default output file type
    DEFAULT_OUTPUT_TYPE = "txt"
    
    # Set the default output directory
    DEFAULT_OUTPUT_DIR = "output"
    
    # Set the default audio file directory
    DEFAULT_AUDIO_DIR = "audio"
    
    # Set the default log file directory
    DEFAULT_LOG_DIR = "logs"

