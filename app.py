import click

from src.controller import Controller


@click.command()
@click.option(
    '--players_num',
    required=True,
    type=click.IntRange(3, None),
    default=3,
    help='Number of players',
)
def main(players_num):
    controller = Controller(players_num)

    # Optimal points for the first player
    point = controller.get_optimal_point()
    points = controller.get_optimal_points()

    click.echo(point)
    click.echo('Randomly chosen from optimal points: {}'.format(points))


if __name__ == '__main__':
    main()
