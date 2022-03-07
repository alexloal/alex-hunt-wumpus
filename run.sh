#!/bin/sh
docker build --tag wumpus .
docker run -ti --name wumpus wumpus