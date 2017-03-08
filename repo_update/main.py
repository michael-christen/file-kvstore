import argparse
import inspect
import sys

from .io import read_kpi_config
from .io import write_kpi_output


class Parser(object):
    def __init__(self):
        self._base_parser = argparse.ArgumentParser(
            description='Manage repo kpis',
        )
        possible_methods = [
            attr for attr in dir(self) if not attr.startswith('_')]
        possible_methods.remove('run')
        self._base_parser.add_argument(
            'command',
            choices=possible_methods,
            help='subcommand to run')

    def run(self):
        args = self._base_parser.parse_args(sys.argv[1:2])
        try:
            getattr(self, args.command)()
        except AttributeError:
            print 'Unrecognized command {}'.format(args.command)
            self.base_parser.print_help()

    def update(self):
        parser = argparse.ArgumentParser(
            description='Update kpi file'
        )
        parser.add_argument(
            '--config',
            default='.kpi_config.yaml',
            help='KPI configuration file')
        parser.add_argument(
            '--output',
            default='kpi.yaml',
            help='subcommand to run')
        args = parser.parse_args(sys.argv[2:])
        update(args.config, args.output)


def update(config_filename, output_filename):
    kpis = read_kpi_config(config_filename)
    failures = write_kpi_output(kpis, output_filename)
    if failures:
        for f in failures:
            print f
        sys.exit(1)


def main():
    parser = Parser()
    parser.run()


if __name__ == '__main__':
    main()
