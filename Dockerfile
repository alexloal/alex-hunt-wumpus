FROM python:3.7.0-alpine
ADD src/board.py /
ADD src/files.py /
ADD src/instructions.py /
ADD src/interactions.py /
ADD src/points.py /
ADD src/score.py /
ADD src/wumpus.py /
ADD data.txt /
CMD ["python3", "./wumpus.py"]