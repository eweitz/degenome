from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='degenome',
    version='0.1.0',
    url='https://github.com/eweitz/degenome',
    author='Eric Weitz',
    author_email='eric.m.weitz@gmail.com',
    description='Pipeline to convert differential gene expression matrices to Ideogram JSON',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    install_requires=[],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization'
    ]
)