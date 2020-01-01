import click

from src.controller import Controller


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--players_num',
    required=True,
    type=click.IntRange(3, None),
    default=3,
    help='Number of players',
)
def optimal_strategy(players_num):
    controller = Controller(players_num)

    # Optimal points for the first player
    point = controller.get_optimal_point()
    points = controller.get_optimal_points()

    click.echo(point)
    click.echo('Randomly chosen from optimal points: {}'.format(points))


@cli.command()
@click.option(
    '--players_num',
    required=True,
    type=click.IntRange(3, None),
    default=3,
    help='Number of players',
)
@click.option(
    '--samples_num',
    required=True,
    type=click.IntRange(1, None),
    default=100,
    help='Number of samples',
)
def proof(players_num, samples_num):
    controller = Controller(players_num)

    points = controller.get_optimal_points()
    win_statistics = controller.make_experiment(samples_num)

    click.echo('Points {} won in {} percent of cases respectively'.format(points, win_statistics))


if __name__ == '__main__':
    cli()
