import click


@click.group
@click.option('-v', '--verbose', is_flag=True, help='Enter verbose mode')
def main(*options, **kwargs):
    """
    ================= Route Calculation =================

        Command Line interface of Route Calculation.
    """


@main.command
@click.argument('name', type=str, nargs=1)
def hello(name):
    print(f"Hello {name}.")
    print("I hope you enjoy coding.")
