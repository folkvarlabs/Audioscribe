import os
import re
import time
import hashlib
from typing import Dict, Any, List

def generate_output_file_path(file_path: str, output_type: str) -> str:
    """Generate output file path"""

    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]

    output_file_name = f"{file_name_without_ext}.{output_type}"

    return os.path.join(Config.DEFAULT_OUTPUT_DIR, output_file_name)

def get_timestamp() -> str:
    """Get current timestamp"""

    return time.strftime("%Y%m%d-%H%M%S")

def generate_log_file_path(file_path: str) -> str:
    """Generate log file path"""

    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]

    log_file_name = f"{file_name_without_ext}_{get_timestamp()}.log"

    return os.path.join(Config.DEFAULT_LOG_DIR, log_file_name)

def generate_email_subject(audio_file: str) -> str:
    """Generate email subject"""

    file_name = os.path.basename(audio_file)
    return f"{file_name} transcription"

def get_file_hash(file_path: str) ->
