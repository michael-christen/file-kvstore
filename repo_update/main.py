import sys

from .io import read_kpi_config
from .io import write_kpi_output


def main():
    kpis = read_kpi_config('.kpi_config.yaml')
    failures = write_kpi_output(kpis, 'kpi.yaml')
    if failures:
        for f in failures:
            print f
        sys.exit(1)


if __name__ == '__main__':
    main()
