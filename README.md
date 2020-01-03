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

Let's agree that 
* the players choose numbers ***x<sub>i</sub>*** where ***i*** - tne number of a player.

##### 1. The best choice for B if A chooses 0

We have ***x<sub>1</sub> = 0***  
Let's assume the player B has already chosen his number ***x<sub>2</sub>***.

Now the player C is making decision: he can choose either 
***x<sub>3</sub> < x<sub>2</sub>*** or 
***x<sub>3</sub> > x<sub>2</sub>***.

In case of ***x<sub>3</sub> < x<sub>2</sub>*** probability of winning is 
***<sup>x<sub>2</sub></sup>/<sub>2</sub>*** regardless of the third player's choice.

In case of ***x<sub>3</sub> > x<sub>2</sub>*** optimally to choose 
***x<sub>2</sub> + &epsilon;*** i.e.
probability of winning is ***1 - x<sub>3</sub> = 1 - x<sub>2</sub> - &epsilon;*** 
where ***&epsilon;*** is infinitely small and can be omitted.

For the player B the optimal strategy is equalizing the chances of the third player:  
***<sup>x<sub>2</sub></sup>/<sub>2</sub> = 1 - x<sub>2</sub>***  

So the optimal choice for B if A chooses 0 

***x<sub>2</sub> = <sup>2</sup>/<sub>3</sub>***

In this case if (A, B, C) choose ***(0, <sup>2</sup>/<sub>3</sub>, <sup>1</sup>/<sub>3</sub>)***,
probabilities to win are 
***(<sup>1</sup>/<sub>6</sub>, <sup>1</sup>/<sub>2</sub>, <sup>1</sup>/<sub>3</sub>)*** respectively.

##### 2. The best choice for A

Let's assume the player A and B have already 
chosen ***x<sub>1</sub>*** and ***x<sub>2</sub>*** respectively  
and ***x<sub>1</sub> < x<sub>2</sub>***.

Then for the third player the optimal strategy ***x<sub>3</sub>*** is among
***x<sub>1</sub> - &epsilon;***, 
***x<sub>1</sub> < x<sub>3</sub> < x<sub>2</sub>***,
***x<sub>2</sub> + &epsilon;*** 
where ***&epsilon;*** is infinitely small and can be omitted.

The probabilities to win are
***x<sub>1</sub>***, 
***<sup>(x<sub>2</sub> - x<sub>1</sub>)</sup>/<sub>2</sub>***,
***1 - x<sub>2</sub>*** 
 
Optimal strategies we will get resolving the system of equations:
 
***[ x<sub>1</sub> = <sup>(x<sub>2</sub> - x<sub>1</sub>)</sup>/<sub>2</sub>***  
***[ x<sub>1</sub> = 1 - x<sub>2</sub>***

=>

***[ 3x<sub>1</sub> - x<sub>2</sub> = 0***  
***[ x<sub>1</sub> + x<sub>2</sub> = 1***

=>

***[ x<sub>1</sub> = <sup>1</sup>/<sub>4</sub>***  
***[ x<sub>2</sub> = <sup>3</sup>/<sub>4</sub>***

Thus considering symmetry (could be ***x<sub>1</sub> > x<sub>2</sub>***) both answers 
***<sup>1</sup>/<sub>4</sub>*** and ***<sup>3</sup>/<sub>4</sub>*** are optimal for the first player.

In this case if (A, B, C) choose 
***(<sup>1</sup>/<sub>4</sub>, <sup>3</sup>/<sub>4</sub>, <sup>1</sup>/<sub>2</sub>)***,
probabilities to win are 
***(<sup>3</sup>/<sub>8</sub>, <sup>3</sup>/<sub>8</sub>, <sup>1</sup>/<sub>4</sub>)*** respectively.

##### 3. The best choice for the first player when the game is played among n players?

Now let's expand the previous solution to ***n*** players:

Let's assume the first ***n-1*** players have already 
chosen ***x<sub>1</sub>***, ..., ***x<sub>n-1</sub>*** respectively  
and ***x<sub>1</sub> < ... < x<sub>n-1</sub>***.

Then for the third player the optimal strategy ***x<sub>3</sub>*** is among  
***x<sub>1</sub> - &epsilon;***,  
***x<sub>1</sub> < x<sub>n</sub> < x<sub>2</sub>***,  
***...***,  
***x<sub>n-2</sub> < x<sub>n</sub> < x<sub>n-1</sub>***,  
***x<sub>n-1</sub> + &epsilon;***   
where ***&epsilon;*** is infinitely small and can be omitted.

The probabilities to win are  
***x<sub>1</sub>***,  
***<sup>(x<sub>2</sub> - x<sub>1</sub>)</sup>/<sub>2</sub>***,  
***...***,  
***<sup>(x<sub>n-1</sub> - x<sub>n-2</sub>)</sup>/<sub>2</sub>***,  
***1 - x<sub>n-1</sub>*** 
 
Optimal strategies we will get resolving the system of equations:
 
***[ x<sub>1</sub> = <sup>(x<sub>2</sub> - x<sub>1</sub>)</sup>/<sub>2</sub>***  
***[ x<sub>1</sub> = <sup>(x<sub>3</sub> - x<sub>2</sub>)</sup>/<sub>2</sub>***  
***[ ...***  
***[ x<sub>1</sub> = <sup>(x<sub>n-1</sub> - x<sub>n-2</sub>)</sup>/<sub>2</sub>***  
***[ x<sub>1</sub> = 1 - x<sub>n-1</sub>***

=>

***[ 3x<sub>1</sub> - x<sub>2</sub> = 0***  
***[ 2x<sub>1</sub> + x<sub>2</sub> - x<sub>3</sub> = 0***  
***[ ...***  
***[ 2x<sub>1</sub> + x<sub>n-2</sub> - x<sub>n-1</sub> = 0***  
***[ x<sub>1</sub> + x<sub>n-1</sub> = 1***

We can resolve this system  using 
[matrix method][Matrix method] 
converting to matrix form ***Ax = b*** where:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[3&nbsp;-1&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;...&nbsp;&nbsp;0&nbsp;&nbsp;0]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[2&nbsp;&nbsp;1&nbsp;-1&nbsp;&nbsp;0&nbsp;&nbsp;...&nbsp;&nbsp;0&nbsp;&nbsp;0]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[2&nbsp;&nbsp;0&nbsp;&nbsp;1&nbsp;-1&nbsp;&nbsp;...&nbsp;&nbsp;0&nbsp;&nbsp;0]***  
A&nbsp;=&nbsp;&nbsp;***[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]***    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[2&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;...&nbsp;-1&nbsp;&nbsp;0]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[2&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;...&nbsp;&nbsp;1&nbsp;-1]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[1&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;0&nbsp;&nbsp;...&nbsp;&nbsp;0&nbsp;&nbsp;1]***   ,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;x<sub>1</sub>&nbsp;]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;x<sub>2</sub>&nbsp;]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;x<sub>3</sub>&nbsp;]***  
x&nbsp;=&nbsp;&nbsp;***[&nbsp;...&nbsp;&nbsp;]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[x<sub>n-3</sub>]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[x<sub>n-2</sub>]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[x<sub>n-1</sub>]***  ,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;0&nbsp;]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;0&nbsp;]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;0&nbsp;]***  
b&nbsp;=&nbsp;&nbsp;***[&nbsp;...&nbsp;]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;0&nbsp;]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;0&nbsp;]***  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***[&nbsp;1&nbsp;]***  

The solution of this system is implemented in the current CLI app.
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
in [Solution 2](#2-the-best-choice-for-a):

```
> The points: [0.25, 0.5, 0.75]
> Respectively won in percent of cases: [37.5, 25.0, 37.5]
```

[Docker Install]:  https://docs.docker.com/install/
[Matrix method]:  https://en.wikipedia.org/wiki/System_of_linear_equations#Matrix_solution