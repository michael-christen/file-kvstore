import yaml

from .exceptions import KPIReadException
from .objects import KPI
from .objects import KPIOutput


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


def read_kpi_output(output_file):
    with open(output_file, 'r') as f:
        yaml_output = yaml.load(f.read())
    kpis = []
    names = set()
    for name2val in yaml_output:
        assert len(name2val.items()) == 1
        kpi = KPIOutput(*name2val.items()[0])
        kpis.append(kpi)
        names.add(kpi.name)
    assert len(names) == len(yaml_output)
    return kpis


def write_kpi_output(kpi_outputs, output_file):
    failures = []
    output_yaml = []
    for kpi in kpi_outputs:
        output_yaml.append({kpi.name: kpi.value})
    with open(output_file, 'w') as f:
        yaml.dump(output_yaml, stream=f, default_flow_style=False)
    return failures
