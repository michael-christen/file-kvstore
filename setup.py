from setuptools import find_packages
from setuptools import setup


setup(
    name='kvstore',
    version='0.1.0',
    description='Tool for storing key/value pairs in text files',
    author='Michael Christen',
    url='https://github.com/michael-christen/kvstore',
    license='MIT',
    packages=find_packages(exclude=["tests*"]),
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
