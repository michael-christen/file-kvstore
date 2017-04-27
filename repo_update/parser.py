import argparse
import sys

from .utils import modify_yaml_dictionary


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
        # kpis = get_dict_from_yaml(parsed_args.file)
        # write_dict_to_yaml(parsed_args.file, kpis)
        with modify_yaml_dictionary(parsed_args.file) as kpis:
            kpis[parsed_args.kpi] = parsed_args.value
