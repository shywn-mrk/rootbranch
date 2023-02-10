import click

@click.command()
@click.argument('branch', type=click.STRING, required=True)
def cli(branch):
    """
        Adds directories to staging.
    """
    pass
