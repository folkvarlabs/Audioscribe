# Audioscript main file
import os
from typing import List, Tuple

import click
import requests
from dotenv import load_dotenv

from audioscript.transcription import transcribe_audio
from audioscript.output import save_to_file, send_email, convert_to_mp3, print_transcription


load_dotenv()


@click.group()
def cli():
    pass


@click.command()
@click.argument('url')
@click.option('--format', '-f', type=click.Choice(['txt', 'json', 'html', 'md', 'pdf', 'docx']), default='txt')
@click.option('--email', '-e', type=str, help='Email to send transcription to.')
@click.option('--mp3', '-m', type=str, help='Path to MP3 file.')
def transcribe(url: str, format: str, email: str, mp3: str) -> None:
    """Transcribe an audio file from a URL."""
    response = requests.get(url)
    if response.ok:
        audio_content = response.content
        transcription = transcribe_audio(audio_content)
        if email:
            send_email(email, transcription, format)
        elif mp3:
            convert_to_mp3(transcription, mp3)
        else:
            print_transcription(transcription)
            save_to_file(transcription, format)
    else:
        click.echo(f'Response error: {response.status_code}')


cli.add_command(transcribe)

if __name__ == '__main__':
    cli()
