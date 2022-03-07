# Hunt the Wumpus:

## About:

Hunt the Wumpus is an old computer game created by Gregory Yob in 1972. The basic idea is that you are in a network of
caves which contain hazards like bottomless pits, super bats, and of course the deadly wumpus. Your goal is to move
throughout the caves, find the wumpus, and kill it before it kills you.
See [Wikipedia](https://en.wikipedia.org/wiki/Hunt_the_Wumpus) for more information about this game.

## Basic Rules:

The player has 5 arrows. If they run out of arrows before killing the Wumpus, the player loses the game. In the cave
there are:

    * One Wumpus
    * Two giant bats
    * Two bottomless pits

    If the player enters a room with the Wumpus       --> He is eaten by it and the game is lost.
    If the player enters a room with a bottomless pit --> He falls into it and the game is lost.
    If the player enters a room with a giant bat      --> The bat takes him and transports him into a random empty room.

Each turn the player can either walk into an adjacent room or shoot into an adjacent room. Whenever the player enters a
room, he/she "senses" what happens in adjacent rooms. The messages are:

    Nearby Wumpus: -->  "You smell something terrible nearby."
    Nearby Bat:    -->  "You hear a rustling."
    Nearby Pit:    -->  "You feel a cold wind blowing from a nearby cavern."

When the player shoots, he wins the game if he is shooting in the room with the Wumpus. If he shoots into another room,
the Wumpus has a 75% of chance of waking up and moving into an adjacent room:
if this is the room with the player, he eats him up and the game is lost.

## Game modes:

When the game starts, you can choose between three game modes.

    * Hard:   You will fight against 2 giant Bats and 1 Wumpus and you will only have 3 arrows.
              Be careful! because this cave will have 5 bottomless pits.

    * Normal: 5 arrows are 5 opportunities for killing the 2 giant Bats and 1 Wumpus. 
              Here you can be riskier in your movements because the number of bottomless pits is 2.

    * Easy:   This is the mode for beginners, to initiate you in the hunt of the Wumpus. 
              With 5 arrows you can shoot down to the Wumpus and only 1 giant Bat. 

## The Score:

To make 'Hunt the Wumpus' more exciting and competitive, all your actions are scored.

    * In each game you will start with 0 points.
    * If you make a move                                    --> 1 point will be substracted.
    * If you shoot an arrow and it does not hit your target --> you will lose 2 points, in addition to the arrow.
    * If a gian Bat catches you                             --> you will lose 5 points.
    * If you manage to kill a giant Bat                     --> you get 20 points.
    * If you kill the Wumpus                                --> 50 points will be added.

## Technical things:

This solution has been implemented in Python 3.7. 
No external library has been used in this implementation.

The solution has been dockerized, so you will probe it easier.
### Project

This is the project structure:

    /src
        board.py         ------------------>    Board of the game. 
        files.py         ------------------>    Manage the IO for the scoring.
        instructions.py  ------------------>    Contains everything related to the titles and instructions of the game.
        interactions.py  ------------------>    Manage user interaction.
        points.py        ------------------>    Enum for the scoring.
        score.py         ------------------>    Manage the upper scoring in the screen.
        wumpus.py        ------------------>    Contains the main loop and manage the shooting and movement algorithm.
    /test
        board_test.py    ------------------>    Unit test for the board class.
        interactions_test.py -------------->    Unit test for the interaction class.
    data.txt             ------------------>    Store the result of every game.
    Dockerfile           ------------------>    Docker configuration file.
    README.md            ------------------>    Project information.
    rerun.sh             ------------------>    Rerun the wumpus container.
    run.sh               ------------------>    Build the wumpus dockerization.
    stop.sh              ------------------>    Stop the wumpus container.

All needed classes have been located inside the src directory.

### How to play

#### Using Docker
Follow this steps in order to execute 'Hunt the Wumpus'.

Make sure the 'sh' files have 'execute' permission in your environment. If not, launch this command in the terminal: 

```shell
> chmod +x run.sh
> chmod +x rerun.sh
> chmod +x stop.sh
```
Now, execute the run file inside the project in order to build the docker and run it.

```shell
> ./run.sh
```

#### Using Python
If you have installed in your computer Python 3.7+ you can execute 'Hunt The Wumpus' easier.
In the terminal, execute this command:

```shell
> python3 wumpus.py
```

Once inside the game, you will see the title and the rules, you should choose the game mode, and then it will start the hunting.
When the game is over, you will type your name if you want to be registered in the scoring list.
    
If you want to play another game again:
#### Using Docker

Execute this command:

```shell
> ./rerun.sh
```

If you want to stop the created container, you can execute this command:

```shell
> ./stop.sh
```

#### Using Python

Execute again this command in order to launch the application:

```shell
> python3 wumpus.py
```
