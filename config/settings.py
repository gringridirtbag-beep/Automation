import configparser
from dotenv import load_dotenv

import os

load_dotenv()
config = configparser.ConfigParser()
config.read("config/config.ini")

BASE_URL = config["DEFAULT"]["BASE_URL"]
TIMEOUT = config["DEFAULT"]["TIMEOUT"]
DEMOQA_USERNAME = os.getenv("DEMOQA_USERNAME")
DEMOQA_PASSWORD = os.getenv("DEMOQA_PASSWORD")

