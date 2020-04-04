import click, toml, pathlib
pyproject = toml.load(pathlib.Path(__file__).parent / 'data' / 'pyproject.toml')

@click.command()
def main():
    author, module, author_email, home_page = None