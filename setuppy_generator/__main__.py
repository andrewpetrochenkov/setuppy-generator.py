#!/usr/bin/env python
"""create `setup.py`"""
import click
import setuppy_generator


MODULE_NAME = "setuppy_generator"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    generator = setuppy_generator.Generator()
    print(generator.render())


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
