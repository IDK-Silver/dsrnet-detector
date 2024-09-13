import pathlib
import sys

sys.path.append(str((pathlib.Path(__file__).parent / 'extern' / 'DSRNet').absolute()))
from . import detector

__version__ = "0.1.0"
__all__ = ['detector']