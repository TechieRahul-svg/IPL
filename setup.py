from setuptools import setup, find_packages

setup(
    name='ipl-analysis',
    version='0.1.0',
    description='IPL Cricket Data Analysis and Statistics',
    author='Rahul Panda',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.0',
        'numpy>=1.21.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
    ],
    python_requires='>=3.7',
)
