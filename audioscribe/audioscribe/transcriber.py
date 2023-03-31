import logging
import os
import sys
import time

from typing import Dict
from audio_transcription import AudioTranscriber
from output import write_output
from config import Config
from exceptions import InvalidAudioFileException, APIKeyMissingException

logger = logging.getLogger(__name__)

class AudioscribeTranscriber:
    """Class for audio transcription"""

    def __init__(self, audio_file: str, output_type: str, api_key: str):
        self.audio_file = audio_file
        self.output_type = output_type
        self.api_key = api_key

    def transcribe_audio(self) -> str:
        """Transcribe the audio file"""

        if not self.api_key:
            raise APIKeyMissingException("API key missing")

        if not os.path.isfile(self.audio_file):
            raise InvalidAudioFileException("Invalid audio file")

        logger.info("Transcribing audio file")

        transcriber = AudioTranscriber(api_key=self.api_key)
        transcript = transcriber.transcribe_audio_file(self.audio_file)

        output = write_output(transcript=transcript, output_type=self.output_type)

        return output
