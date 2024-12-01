from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(filename:str)->List[str]:
    '''
    this function will return the list of the requirements from the requirements.txt
    '''
    with open(filename) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements  

setup(
    name='mlproject',
    version='0.0.1',
    author='naman',
    author_email='namansharmaves@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)