.PHONY:	run

run:	gator_taxi.py
	python $< $(word 2,$(MAKECMDGOALS))

%:
	@:
# make run input_file.txt 