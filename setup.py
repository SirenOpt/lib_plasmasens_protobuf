from setuptools import setup, find_packages

setup(
    name='measurement_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'grpcio',
        'protobuf'
    ],
    author='Michael O Craig Jr',
    description='A library for sending measurements to a server',
    url='https://github.com/SirenOpt/lib_plasmasens_protobuf',

)
