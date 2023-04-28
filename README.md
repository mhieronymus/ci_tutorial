# Docker, CI, and Stuff Tutorial

This repository is supplementary material for a W2W internal tutorial.
The tutorial aims to cover 
- Creating a Docker image
- Using GitLab CI or GitHub Actions
- Analyzing coding style
- Creating and running unit tests and end-to-end tests

## About the contents
This repository is based on [DWD's regrid image](https://hub.docker.com/r/deutscherwetterdienst/regrid).
It downloads the image along with GRIB2 ICON samples and converts them to grid files. These can be plotted with a different container
using some Python routines.
To access the Jupyter notebook, go to `localhost:9000/lab` and enter the token shown in the terminal.
We use [mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html) to expedite the installation process since conda can be rather slow.
The `plot_scripts.py` provides functions to load the data and plot it. Try it out in a notebook.
The notebook could look like this:
``` 
import sys

if ".." not in sys.path:
    sys.path.insert(0, "..")
from plot_scripts import plot_418, load_data, create_widget

fig = plot_418()
```
or have a cell like that:
```
grbs = load_data()
create_widget(grbs)
```
Note: Adding `..` to `sys.path` allows you to import functions from files in the parent directory.

## Your TODOs
- Modify the `Dockerfile` that uses Python and installs necessary libraries. Are all dependencies installed? Check every file carefully.
- Check the `docker-compose.yml`. How can you make sure that the container `jupyter_regrid` has access to the sample file from `regrid_sample`? 
- Define the ports for the jupyterlab instance to get access to it from outside the container.
- Try `load_data()` and `create_widget(grbs)`

Have you done that? Then continue with adding a GitHub Action or use GitLab CI.
- Create a workflow/pipeline that prints something.
- Add a job/stage that checks if the code is stylish (watch out for the comments!)
- Choose one or more functions or write some yourself and create test functions.
- Add another job/stage that uses the test functions
