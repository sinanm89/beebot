src = $(wildcard *.c)
obj = $(src:.c=.o)

.PHONY: run
run: source
	git pull
	python flask_app.py

.PHONY:source
source:
	workon beebot
