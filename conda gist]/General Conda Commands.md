* `conda info --envs` : lists all environments
* `source activate <env name>`: activate an environment
* `source deactivate`: deactivate an environment
* `conda list` : list all packages installed
* `conda create --name <env name> python=3 astroid babel` : create new environment, specify version of python, and install packages
* __WINDOWS NOTE: SOURCE is not recognized.__ When deactivating and activating in the anaconda command prompt, skip `source` and just type `deactivate` or `activate` depending on what you are trying to do. 
* `conda env export > environment.yml`: export conda environment requirements list to a file
* `conda env remove -n ENV_NAME` : delete environment