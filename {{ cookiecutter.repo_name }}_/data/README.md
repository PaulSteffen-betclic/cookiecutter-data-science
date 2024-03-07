# `data` folder overview

Any data that needs to be stored locally should be saved in this location. 
These folders are ignored by git but are tracked using DVC.

The sub-folders are organized as follows:

- `input/`
  - `raw/`: raw parquet files obtained using the `{{ cookiecutter.package_name }}/src/data/get_data.py` script
    - `folder/ or file 1`: describe data 
  - `processed/`: processed parquet files obtained using the `{{ cookiecutter.package_name }}/src/data/preprocess.py` script on the `input/raw` data.
    - `folder/ or file 1`: describe data 
- `output/`
    - `folder/ or file 1`: describe data 


The paths for these directories are loaded as environment variables written in `.env` by the
`.envrc` file. To load them in Python, use the following code:

```python
import os

# Load environment variables for the `data` folder, and its sub-folders
DIR_DATA: str = os.getenv("DIR_DATA")
```
