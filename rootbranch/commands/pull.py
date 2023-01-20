import click

@click.command()
def cli(name):
    """
        Pulls every repository and updates them.
    """
    print(f'We are pulling :)')
