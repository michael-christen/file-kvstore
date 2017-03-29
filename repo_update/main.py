import argparse
import sys

from .io import read_kpi_config
from .io import read_kpi_output
from .io import write_kpi_output
from .objects import KPIOutput


class Parser(object):
    def __init__(self):
        self.base_parser = argparse.ArgumentParser(
            description='Manage repo kpis',
        )
        possible_methods = [
            attr for attr in dir(self)
            if callable(getattr(self, attr)) and
            not attr.startswith('_') and
            not attr == 'run']
        self.base_parser.add_argument(
            'command',
            choices=possible_methods,
            help='subcommand to run')
        self.base_parser.add_argument(
            '--config',
            default='.kpi_config.yaml',
            help='KPI configuration file')
        self.base_parser.add_argument(
            '--output',
            default='kpi.yaml',
            help='KPI output file')

    def run(self):
        args = self.base_parser.parse_args(sys.argv[1:2])
        self.config_file = args.config
        self.output_file = args.output
        try:
            getattr(self, args.command)()
        except ValueError as ex:
            print 'Unrecognized command {}'.format(args.command)
            raise ex
            self.base_parser.print_help()

    def update(self):
        parser = argparse.ArgumentParser(
            description='Write kpi file with commands from config'
        )
        parser.add_argument(
            'kpi',
            help='KPI to update')
        parser.add_argument(
            'value',
            help='Value to update the KPI')
        args = parser.parse_args(sys.argv[2:])
        update(self.output_file, args.kpi, args.value)

    def write(self):
        parser = argparse.ArgumentParser(
            description='Write kpi file with commands from config'
        )
        args = parser.parse_args(sys.argv[2:])
        write(self.config_file, self.output_file)


def write(config_filename, output_filename):
    kpis = read_kpi_config(config_filename)
    kpi_outputs = []
    for kpi in kpis:
        try:
            output = kpi.get_result()
        except KPIReadException as ex:
            failures.append(ex)
            output = KPIOutput(kpi.name, '')
        kpi_outputs.append(output)
    write_kpi_output(kpi_outputs, output_filename)
    if failures:
        for f in failures:
            print f
        sys.exit(1)


def update(output_filename, name, value):
    kpis = read_kpi_output(output_filename)
    new_kpis = []
    for kpi in kpis:
        if kpi.name == name:
            new_kpis.append(KPIOutput(kpi.name, value))
        else:
            new_kpis.append(kpi)
    write_kpi_output(new_kpis, output_filename)


def main():
    parser = Parser()
    parser.run()


if __name__ == '__main__':
    main()
