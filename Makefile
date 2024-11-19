run: png/petersen-shell-node.png\
     png/petersen-shell-total.png\
     png/petersen-shell.png\
     png/random-graph.png

png/petersen-shell-node.png: src/petersen-shell-node.py
	poetry run python $<

png/petersen-shell-total.png: src/petersen-shell-total.py
	poetry run python $<

png/petersen-shell.png: src/petersen-shell.py
	poetry run python $<

png/random-graph.png: src/random-graph.py
	poetry run python $<

install:
	poetry install
