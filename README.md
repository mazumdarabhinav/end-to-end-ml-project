# End to End ML Project

An End to End ML Project



**All the Commands are `project_name` folder**

# Configurations

## 1. Create and Activate Environment

1. `conda create -n venv python=3.9 -y`
2. `conda activate venv`

## 2. Git Configuration

1. `git config user.name "<your github profile name>"`
2. `git config user.email "<your github email id>"`

## 3. Update Config Reader

1. In the file path `config/config_reader.py`, update the line accordingly:

*DEV*:

    config.read("./config/config_dev.ini")

*PROD*:

    config.read("./config/config_prod.ini")

