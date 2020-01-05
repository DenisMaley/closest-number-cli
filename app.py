import click

from src.controller import Controller

DECIMALS = 3


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--players_num', '-n',
    required=True,
    type=click.IntRange(3, None),
    default=3,
    help='Number of players',
)
def optimal_strategy(players_num):
    controller = Controller(players_num)

    # Optimal points for the first player
    point = round(controller.get_optimal_point(), DECIMALS)
    points = [round(elem, DECIMALS) for elem in controller.get_optimal_points()]

    click.echo('The optimal strategy for the first player: {}'.format(point))
    click.echo('Was randomly chosen from the several optimal points: {}'.format(points))


@cli.command()
@click.option(
    '--players_num', '-n',
    required=True,
    type=click.IntRange(3, None),
    default=3,
    help='Number of players',
)
@click.option(
    '--samples_num', '-s',
    required=True,
    type=click.IntRange(1, None),
    default=100,
    help='Number of samples',
)
def proof(players_num, samples_num):
    controller = Controller(players_num)

    points, win_statistics = controller.make_experiment(samples_num)
    points = [round(elem, DECIMALS) for elem in points]
    win_statistics = [round(elem * 100, 1) for elem in win_statistics]

    click.echo('The points: {}'.format(points))
    click.echo('Respectively won in percent of cases: {}'.format(win_statistics))


if __name__ == '__main__':
    cli()
