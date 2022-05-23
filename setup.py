from setuptools import setup, find_packages

setup(
    name='Osensapy2',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    install_requires=['sys', 'glob', 'serial',],
    url='https://github.com/Adi-Rai/Osensapy2',
    author='Aditya Rai',
    author_email='rai.aditya01@gmail.com'
)