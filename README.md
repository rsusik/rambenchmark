<p align="center">
    <img src="https://github.com/rsusik/rambenchmark/raw/master/rambenchmark.png" alt="RAM Benchmark" />
</p>
<p align="center">
    <em>Simple RAM benchmark for Linux.</em>
</p>
<p align="center">
<a href="https://pypi.org/project/rambenchmark" target="_blank">
    <img src="https://img.shields.io/pypi/v/rambenchmark?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://github.com/rsusik/rambenchmark/blob/master/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/rsusik/rambenchmark" alt="Package version">
</a>
</p>


# Simple RAM Benchmark
This is a simple RAM benchmark written in C++. 
It allows checking approximate RAM speed. The code creates a 1 GiB (1024\*1024\*1024 bytes) buffer, fills it with zeroes, 
scans the buffer, and measure the time.

*Note: This is only experimental code written to check the RAM speed on Linux. There are probably better tools for memory analysis available like memtest86.*

## Requirements
* Unix/Linux OS (can be easily ported to Windows)
* g++ compiler compatible with OpenMP (for multi-threaded variant)
* at least 1 GB free RAM (for buffer)

## Install and run using pip
To execute the benchmark, you only have to meet the requirements and run the below commands:
```shell
pip install rambenchmark
rambenchmark
```

## Compile and run manually
If you prefer to compile and execute the code manually, you can do that by running the following commands:
```shell
git clone git@github.com:rsusik/rambenchmark.git
cd rambenchmark/rambenchmark
g++ -O3 -std=c++11 -fopenmp -o rambench ./rambench.cpp
./rambench
```

## Tests
The benchmark uses two functions for tests:
1. *memset()*
2. *memchr()*

## Output
The benchmark produces below example output:

```
======================================================================
BENCHMARKING RAM WITH MULTI THREADS
(...please wait...)

4 concurrent threads are supported.

----------------------------------------------------------------------
MEMSET TEST

RESULT of filling 1GiB buffer with zeros.
>>> 0.0654 (s) / 16415.2 (MB/s) <<<

                   Details
  #Threads        Time (s)      Speed (MB/s)
         1      0.0654 (s)    16415.2 (MB/s)
         2      0.0663 (s)    16189.3 (MB/s)
         3      0.0708 (s)    15161.6 (MB/s)
         4      0.0750 (s)    14299.5 (MB/s)

----------------------------------------------------------------------
MEMCHR TEST

RESULT of scanning 1GiB buffer.
>>> 0.0776 (s) / 13820.1 (MB/s) <<<

                   Details
  #Threads        Time (s)      Speed (MB/s)
         1      0.1686 (s)     6365.2 (MB/s)
         2      0.0985 (s)    10893.6 (MB/s)
         3      0.0874 (s)    12281.8 (MB/s)
         4      0.0776 (s)    13820.1 (MB/s)

======================================================================
```
