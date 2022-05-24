# Notes for profiling python code. For more details see

- https://docs.nersc.gov/development/languages/python/profiling-debugging-python/
- https://machinelearningmastery.com/profiling-python-code/

## Source code example

- https://github.com/adrianjhpc/archer-python/tree/master/examples/cfd/solutions/numpy_loops

## cProfile

- Built-in profiling module.
- Collect data using cProfile:
```
python -m cProfile -o output.prof path/to/your/script
```
- View results on command line:
```
python -m pstats output.prof
sort tottime
stats <filter>
quit()
```
- View results in python:
```python
import pstats
stats = pstats.Stats('output.prof')
stats.sort_stats('tottime')
stats.print_stats()
```

- View results in GUI:
```
pip install snakeviz
snakeviz output.prof
ctrl+C
```

## line_profiler

```
pip install line_profiler
```

- Decorate functions with `@profile`
- Run line profiler:
```
kernprof -l script_to_profile.py
```
- Generate human readable output:
```
python -m line_profiler script_to_profile.lprof > line_profiler_out.txt
```

## ARM Forge Map

- Commercial software. Installed on Myriad.
- Requires X11 forwarding (or local client, show config if there's time)
  - Linux: Should work with `ssh -X`
  - Macos: Install XQuartz
  - Windows: ...
  
- Open GUI with
```
module load armforge
map python path/to/your/script.py
```
- "Application" is `python`
- Name of script and command line arguments go in "Arguments"
- Remember to set "Working Directory"!
- "Submit to Queue"
