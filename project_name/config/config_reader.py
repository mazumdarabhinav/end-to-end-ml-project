import configparser

config = configparser.ConfigParser()
config.read("./config/config_dev.ini")

REQUIREMENTS_PATH = config.get("DEFAULT", "requirements_path")
