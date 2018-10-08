
import click
import sys

@click.group()
def lpad():
    pass

@lpad.group()
def ppa():
    pass

@ppa.command()
@click.argument('url')
@click.option('--series')
def ls(url, series):
    from . import ppa
    sources, err = ppa.ls(url, series=series)
    if sources is None:
        click.echo(err, err=True)
        sys.exit(err.value)
    else:
        for src in sources:
            click.echo("%-8s %-24s %s" % (src.distro_series, src.version, src.name))

