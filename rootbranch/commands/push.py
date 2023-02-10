import click

@click.command()
@click.option('-f', '--force', flag_value='force')
def cli(force):
    """
        Adds directories to staging.
    """
    pass
