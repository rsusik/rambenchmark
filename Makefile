all: main

main:
	g++ -O3 -std=c++11 -fopenmp -o rambench rambench.cpp
clean:
	rm -f rambench

benchmark:
	make all
	./rambench
