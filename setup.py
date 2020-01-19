from setuptools import setup, find_packages

with open('docs/overview.rst', 'r') as f:
    long_description = f.read()

setup(
    name='degenome',
    version='1.0.0-rc1',
    url='https://github.com/eweitz/degenome',
    author='Eric Weitz',
    author_email='eric.m.weitz@gmail.com',
    license='CC0-1.0',
    description='Pipeline to convert differential gene expression matrices to Ideogram JSON',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    install_requires=[],
    packages=find_packages(),
)