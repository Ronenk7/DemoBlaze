import os.path
from enum import Enum


class Definitions(Enum):
    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))
