import os
from dotenv import load_dotenv as dotenv_load

def load_env():
    dotenv_load()

def get_env(var_name, default=None):
    return os.getenv(var_name, default)
