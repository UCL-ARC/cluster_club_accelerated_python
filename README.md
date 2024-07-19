# Cluster club workshop on Accelerating Scientific Code in Python

This repository contains the material (notes, exercises and a challenge) for the cluster-club workshop on _Accelerating Scientific Code in Python_ run by UCL-ARC.

## Setting up an isolated python environment

We recommend to set up a separate python environment that is isolated from your system's installation of python or any other version in your other projects. This is so that we can obtain a deterministic development environment with only the relevant python libraries and packages that are essential for this project.

You may use any tool to obtain a suitable python virtual environment, although the instructions here shall use `conda`.

```
conda create -n condaenv_arc_clusterclub python=3.12
conda activate condaenv_arc_clusterclub
pip install -r requirements.txt
```

## Usage

For working on the exercises, please invoke the command `jupyter lab` session for notebooks in the appropriate directory.

For viewing the materials as rendered HTML pages in a web browser, clone this repository and run `jupyter book .`. The HTML files shall be created in the `_build/html/` directory.

## Contributors

We welcome and recognize all contributions. A contribution guide can be found [here](./CONTRIBUTING.md).

## Credits

- This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
- Based on Prof Timo Betcke's [HPC Lecture Notes in Python](https://tbetcke.github.io/hpc_lecture_notes/intro.html)
