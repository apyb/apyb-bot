import click

from apyb import github


@click.group()
def cli():
    pass


def attach_commands(cli: click.Group, commands: list[click.Command]):
    for command in commands:
        cli.add_command(command)


attach_commands(cli, github.commands)


if __name__ == "__main__":
    cli()
