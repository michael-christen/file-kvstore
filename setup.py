from setuptools import find_packages
from setuptools import setup


setup(
    name='repo_update',
    version='0.1.0',
    description='Tool for keeping track of repo KPIs',
    author='Michael Christen',
    url='https://github.com/michael-christen/repo_update',
    license='MIT',
    packages=find_packages(exclude=["tests*"]),
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
