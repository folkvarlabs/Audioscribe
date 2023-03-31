import unittest
from unittest.mock import patch
from audioscript.transcriber import Transcriber

class TestTranscriber(unittest.TestCase):
    @patch('audioscript.transcriber.Transcriber.transcribe')
    def test_transcribe_success(self, mock_transcribe):
        mock_transcribe.return_value = 'test transcription'
        transcriber = Transcriber()
        result = transcriber.transcribe('test_file.mp3')
        self.assertEqual(result, 'test transcription')

    @patch('audioscript.transcriber.Transcriber.transcribe')
    def test_transcribe_failure(self, mock_transcribe):
        mock_transcribe.return_value = ''
        transcriber = Transcriber()
        result = transcriber.transcribe('test_file.mp3')
        self.assertEqual(result, 'Error: Transcription failed')

if __name__ == '__main__':
    unittest.main()
