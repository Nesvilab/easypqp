# for testing via a full Click command
import click
import sys

from easypqp.main import convertpsm
from easypqp.main import convertpsm_core


def parse_arguments(argument_string):
    """
    Parse the input string arguments into a dictionary of parameters.
    """
    ctx = click.Context(convertpsm)
    opts = ctx.command.parse_args(ctx, argument_string)
    return ctx.params


if __name__ == '__main__':
    cmdargs = parse_arguments(sys.argv[1:])
    convertpsm_core(**cmdargs)
