import click

@click.command()
@click.argument('branch_name', type=click.STRING, required=True)
def cli(branch_name):
    """
        Switchs or creates a new branch in your working directories.
    """
    pass
