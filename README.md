# Cluster club workshop on Accelerating Scientific Code in Python

This repository contains the material (notes, exercises and a challenge) for the cluster-club workshop on _Accelerating Scientific Code in Python_ run by UCL-ARC.

(setup-devenv)=
## Setting up an isolated python environment

We recommend to set up a separate python environment that is isolated from your system's installation of python or any other installation of python configured for your other projects. This is so that we can obtain a deterministic development environment with a streamlined set of relevant python libraries and packages that are essential for this project.

You may use any tool to obtain a suitable python virtual environment, although the instructions here shall use `conda`.

```
conda create -n condaenv_arc_clusterclub python=3.12
conda activate condaenv_arc_clusterclub
pip install -r requirements.txt
```

## Usage

For working on the exercises, please clone (or download) this repository and invoke the command `jupyter lab` to access the computational notebooks from the relevant directory. The challenge problem towards the last hour of the workshop is intended to be worked on as a python script using your preferred text editor/IDE.

A web version of the materials can be found online at [https://github-pages.arc.ucl.ac.uk/cluster_club_accelerated_python/](https://github-pages.arc.ucl.ac.uk/cluster_club_accelerated_python/). To view a local copy of the materials as rendered HTML pages, please clone (or download) this repository, set up the development environment as outlined [above](setup-devenv), and run `jupyter book build .`. The static web pages shall be created in the `_build/html/` directory, and the main landing page can be accessed by opening `_build/html/index.html` in a web browser.

## Contributors

We welcome and recognize all contributions. A contribution guide can be found [here](./CONTRIBUTING.md).

## Credits

- This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
- Based on Prof Timo Betcke's [HPC Lecture Notes in Python](https://tbetcke.github.io/hpc_lecture_notes/intro.html)
