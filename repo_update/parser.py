import argparse
import sys

from .io import get_dict_from_yaml
from .io import write_dict_to_yaml


class Parser(object):
    def __init__(self):
        self.base_parser = argparse.ArgumentParser(
            description='Update key-value store in yaml file',
        )
        self.base_parser.add_argument(
            '--file',
            default='stats.yaml',
            help='KPI file')
        self.base_parser.add_argument(
            'kpi',
            help='KPI to update')
        self.base_parser.add_argument(
            'value',
            help='Value to update the KPI')

    def run(self, args=None):
        args = args or sys.argv[1:]
        parsed_args = self.base_parser.parse_args(args)
        kpis = get_dict_from_yaml(parsed_args.file)
        kpis[parsed_args.kpi] = parsed_args.value

        write_dict_to_yaml(parsed_args.file, kpis)
