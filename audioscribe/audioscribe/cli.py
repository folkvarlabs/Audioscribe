import click
from menu import main_menu

@click.command()
def cli():
    """Audioscribe CLI"""
    main_menu()

if __name__ == "__main__":
    cli()
