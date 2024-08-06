# for testing via a full Click command
import click
import sys

from easypqp.main import convertpsm, convertpsm_core
from easypqp.main import library_core, library


def parse_arguments_convertpsm(argument_string):
    """
    Parse the input string arguments into a dictionary of parameters.
    """
    ctx = click.Context(convertpsm)
    opts = ctx.command.parse_args(ctx, argument_string)
    return ctx.params


def parse_arguments_library(argument_string):
    """
    Parse the input string arguments into a dictionary of parameters.
    """
    ctx = click.Context(library)
    opts = ctx.command.parse_args(ctx, argument_string)
    return ctx.params


if __name__ == '__main__':
    if sys.argv[1] == 'convertpsm':
        cmdargs = parse_arguments_convertpsm(sys.argv[2:])
        convertpsm_core(**cmdargs)
    elif sys.argv[1] == 'library':
        cmdargs = parse_arguments_library(sys.argv[2:])
        library_core(**cmdargs)
    else:
        print('invalid command string or unsupported command for this test')

    print('done')
    sys.exit(0)
