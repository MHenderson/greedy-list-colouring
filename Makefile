run: png/petersen-shell.png png/random-graph.png

png/petersen-shell.png: src/petersen-shell.py
	poetry run python $<

png/random-graph.png: src/random-graph.py
	poetry run python $<

install:
	poetry install
