from contextlib import contextmanager

from .io import get_dict_from_yaml
from .io import write_dict_to_yaml


@contextmanager
def modify_yaml_dictionary(filename):
    try:
        dictionary = get_dict_from_yaml(filename)
        yield dictionary
    finally:
        write_dict_to_yaml(filename, dictionary)
