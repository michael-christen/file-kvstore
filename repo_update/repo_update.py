import yaml
import subprocess
import sys


class KPI(object):
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def get_result(self):
        output = subprocess.check_output(['sh', '-c', self.command])
        output = output.strip()
        try:
            output = float(output)
            if output.is_integer():
                output = int(output)
        except ValueError:
            pass
        return output


def parse_kpi_config(config_file='.kpi_config.yaml'):
    with open(config_file, 'r') as f:
        yaml_config = yaml.load(f.read())
    names = set()
    kpis = []
    for name2cmd in yaml_config:
        assert len(name2cmd.items()) == 1
        kpi = KPI(*name2cmd.items()[0])
        kpis.append(kpi)
        names.add(kpi.name)
    assert len(names) == len(yaml_config)
    return kpis


def write_kpi_output(kpis, output_file='kpi.yaml'):
    failures = []
    output_yaml = []
    for kpi in kpis:
        try:
            output = kpi.get_result()
        except subprocess.CalledProcessError as ex:
            failures.append(ex)
            output = ''
        output_yaml.append({kpi.name: output})

    with open(output_file, 'w') as f:
        yaml.dump(output_yaml, stream=f, default_flow_style=False)

    if failures:
        for f in failures:
            print f
        sys.exit(1)


def main():
    kpis = parse_kpi_config()
    return write_kpi_output(kpis)


if __name__ == '__main__':
    main()
