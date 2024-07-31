# N-body simulation of particles in Cosmology

## Introduction

In this challenge, we shall attempt to speed up a classical [n-body simulation](https://en.wikipedia.org/wiki/N-body_simulation).

You are given a starter code in the `challenge_problem/` folder. There are two files in here: `nbody.py` and `nbody_test.py`

### `nbody.py`

This code simulates the gravitational interaction between many astronomical bodies. In fact, this kind of algorithm is quite general; as well as simulating gravitational phenomena like galaxy formation, Saturn's rings and planetary systems, it can be used to simulate fluids, electrodynamics and even some statistical processes. This code includes two examples, a version of our solar system and a completely randomised solar system with as many planets (or bodies) as you like.

The main algorithm has two steps:

1. Calculate the gravitational force on one body from all other bodies (and do this for every single body)
2. Move all bodies forward in time

Identify the computationally intensive part of this through profiling.
If there are $N$ bodies, the code needs to calculate the force on one particular body from each of the $N-1$ other bodies, i.e. $N-1$ calculations, and it must repeat that for every body, so $N \times (N-1) \approx N^2$ calculations. For the planets in the solar system this is doable but if we wish to simulate all the asteroids as well (over a million!) this algorithm becomes computationally expensive very quickly. There are two approaches to tackle this; use a more sophisticated numerical algorithm, or try to speed up the basic algorithm using the techniques we came across. Since our focus has *not* been on numerical methods, we shall aim to speed up the basic algorithm. Luckily, the simple algorithm is amenable to be parallelised.

Run the provided starter code by invoking `python nbody.py` (from within the challenge directory) to see the baseline timing for various particle counts.

### `nbody_test.py`
This code checks that functions within `nbody.py` produce the same expected output for various known input conditions. Testing individual functions in this manner is known as unit testing, and is core idea behind the modern software development practice known as Test Driven Development (TDD). As we make attempts to continuously improve the performance of the code through frequent edits and updates to the body of the functions within `nbody.py`, we aim to ensure that the code still produces the expected results for a known set of inputs i.e. we aim to keep the input-output behaviour consistent. The test code `nbody_test.py` uses the popular unit testing library known as `pytest`.

To run the tests, simply invoke `pytest` at the command line from the challenge directory. The output `pytest` should indicate that all tests have passed. After making significant changes to the functions, we run `pytest` to ensure consistency and that the tests pass. If any tests fail, we investigate further, and suitably revert/edit the changes to make the tests pass again. At each stage, all tests must pass.

Keep a log of the speedups that you have been able to achieve as you progress with your attempts with different acceleration strategies.
