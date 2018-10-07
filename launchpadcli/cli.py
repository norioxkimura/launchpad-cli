
import click

@click.group()
def lpad():
    pass

@lpad.group()
def ppa():
    pass

@ppa.command()
def ls():
    click.echo("lpad ppa ls")

