import click

@click.command()
@click.argument('directory', type=click.Path(exists=True), required=True)
def cli(directory):
    """
        Adds directories to git staging.
    """
    pass
