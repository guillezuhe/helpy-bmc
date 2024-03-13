from setuptools import find_packages, setup

setup(
    name='helpybmc',
    packages=find_packages(include=['helpybmc']),
    version='0.1.0',
    description='A package for sending helpy!',
    author='Guillermo Camacho',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
