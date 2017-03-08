import yaml

from .exceptions import KPIReadException
from .objects import KPI


def read_kpi_config(config_file):
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


def write_kpi_output(kpis, output_file):
    failures = []
    output_yaml = []
    for kpi in kpis:
        try:
            output = kpi.get_result()
        except KPIReadException as ex:
            failures.append(ex)
            output = ''
        output_yaml.append({kpi.name: output})

    with open(output_file, 'w') as f:
        yaml.dump(output_yaml, stream=f, default_flow_style=False)
    return failures
