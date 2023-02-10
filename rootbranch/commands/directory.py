import click

@click.command()
@click.option('-r', '--remove', flag_value='remove', required=False)
@click.argument('directory', type=click.Path(exists=True), required=True)
def cli(remove, directory):
    """
        Adds or removes a working directory.
    """
    pass
