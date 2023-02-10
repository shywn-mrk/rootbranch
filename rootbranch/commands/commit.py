import click

@click.command()
@click.argument('message', type=click.STRING, required=True)
def cli(message):
    """
        Commits your staging files and directories in
        your working directory with one commit message.
    """
    pass
