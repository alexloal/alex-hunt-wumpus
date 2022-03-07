#!/bin/sh
docker start wumpus
docker exec -it wumpus python3 wumpus.py