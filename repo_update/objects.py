import subprocess

from collections import namedtuple

from .exceptions import KPIReadException


def _format_output(value):
    value = value.strip()
    try:
        value = float(value)
        if value.is_integer():
            value = int(value)
    except ValueError:
        pass
    return value


class KPI(object):
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def get_result(self):
        try:
            output = subprocess.check_output(['sh', '-c', self.command])
        except subprocess.CalledProcessError as ex:
            raise KPIReadException(str(ex))

        return KPIOutput(self.name, _format_output(output))


KPIOutput = namedtuple('KPIOutput', ['name', 'value'])
