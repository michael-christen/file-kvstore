import argparse
import sys

from .constants import DEFAULT_FILE
from .utils import get as file_get
from .utils import update


class Parser(object):
    def __init__(self):
        self.base_parser = argparse.ArgumentParser(
            description='Update key-value store in yaml file',
        )
        self.base_parser.add_argument(
            '--file',
            default=DEFAULT_FILE,
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
        update(parsed_args.kpi, parsed_args.value, parsed_args.file)


def main():
    parser = Parser()
    parser.run()


class GetParser(object):
    def __init__(self):
        self.base_parser = argparse.ArgumentParser(
            description='Get value from key store in yaml file',
        )
        self.base_parser.add_argument(
            '--file',
            default=DEFAULT_FILE,
            help='KPI file')
        self.base_parser.add_argument(
            'kpi',
            help='KPI to update')

    def run(self, args=None):
        args = args or sys.argv[1:]
        parsed_args = self.base_parser.parse_args(args)
        print file_get(parsed_args.kpi, parsed_args.file)


def get():
    parser = GetParser()
    parser.run()
