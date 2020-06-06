from environs import Env

env: Env = Env()
env.read_env(recurse=False)

DEBUG = env.bool("DEBUG", False)
SECRET_KEY = env.str("SECRET_KEY", "")
SALT = env.str("SALT")
