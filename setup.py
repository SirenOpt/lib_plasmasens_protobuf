from setuptools import setup, find_packages

setup(
    name='lib_plasmasens_protobuf',
    version='1.5.3',
    packages=find_packages(),
    install_requires=[
        'grpcio',
        'protobuf'
    ],
    author='Michael O Craig Jr',
    description='A library for sending measurements to a server using gRPC',
    url='https://github.com/SirenOpt/lib_plasmasens_protobuf',
    python_requires='>=3.6',
)
