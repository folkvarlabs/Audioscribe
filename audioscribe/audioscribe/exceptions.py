class AudioscribeException(Exception):
    """Base exception for Audioscribe"""
    pass

class APIKeyMissingException(AudioscribeException):
    """Raised when API key is missing"""
    pass

class InvalidAudioFileException(AudioscribeException):
    """Raised when invalid audio file is provided"""
    pass

class InvalidOutputTypeException(AudioscribeException):
    """Raised when invalid output file type is provided"""
    pass
