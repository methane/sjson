# Simplified JSON

This project is for benchmarking Pure Python, Cython and CFFI.

## CPython 2.7.10

```console
$ python bench.py
pure Python: [None,True,False,0,1,2,3,4,5,6,7,8,9]
1.14317703247
pyx: [None,True,False,0,1,2,3,4,5,6,7,8,9]
0.302298069
```

## PyPy 2.6.0

```console
$ ~/local/pypy-2.6.0-osx64/bin/pypy bench.py
pure Python: [None,True,False,0,1,2,3,4,5,6,7,8,9]
0.106273889542
pyx: [None,True,False,0,1,2,3,4,5,6,7,8,9]
4.17487287521
```
