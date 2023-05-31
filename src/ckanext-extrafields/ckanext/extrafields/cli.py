import click


@click.group(short_help="extrafields CLI.")
def extrafields():
    """extrafields CLI.
    """
    pass


@extrafields.command()
@click.argument("name", default="extrafields")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [extrafields]
