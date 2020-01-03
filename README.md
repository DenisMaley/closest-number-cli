## Closest number game
### The game description

Three players A, B, C play the following game. 

First, A picks a real number between 0 and 1 (both inclusive),  
then B picks a number in the same range (different from A’s choice) and  
finally C picks a number, also in the same range, (different from the two chosen numbers). 

We then pick a number in the range uniformly randomly.  
Whoever’s number is closest to this random number wins the game. 

Assume that A, B and C all play optimally and their sole goal is to maximise their chances of winning.  
Also assume that if one of them has several optimal choices,  
then that player will randomly pick one of the optimal choices.

### The problems

1. If A chooses 0, then what is the best choice for B?
2. What is the best choice for A?
3. What is the best choice for the first player when the game is played among n players?

### The solution

For the theory of the solution and answers for the problems 1-2 please check 
[this document][Theory].

The solution of the problem 3 is implemented in the current CLI app.

### Requirements

To build this project you will need [Docker][Docker Install].

### Installation
```bash
$ git clone https://github.com/DenisMaley/closest-number-cli.git
```
```bash
$ cd closest-number-cli
```
```bash
$ make install
```

If something goes wrong check Makefile to explore docker commands.

### Usage
1. To find an optimal strategy:
```bash
$ make strategy NUM=4
```
where `NUM` is the number of players

2. To make an experiment and see statistics of winning:
```bash
$ make proof NUM=4 SAMPLES=1000000
```
where `NUM` is the number of players, `SAMPLES` is the number of experiments.

### Examples

With `make strategy NUM=4` the app gives the optimal point for the first player:

```
> The optimal strategy for the first player: 0.167
> Was randomly chosen from the several optimal points: [0.167, 0.5, 0.833]
```

With `make proof NUM=3 SAMPLES=1000000` the app gives the theoretical result calculated 
in the [solution of problem 2][Theory]:

```
> The points: [0.25, 0.5, 0.75]
> Respectively won in percent of cases: [37.5, 25.0, 37.5]
```

[Theory]: docs/closest_number_game_solution_description.pdf
[Docker Install]:  https://docs.docker.com/install/
[Matrix method]:  https://en.wikipedia.org/wiki/System_of_linear_equations#Matrix_solution