# Responsible for creating the machine learning application as package

from setuptools import find_packages, setup
from typing import List
from config.config_reader import REQUIREMENTS_PATH


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
    return requirements

setup(
    name='mlproject',
    packages=find_packages(),
    version='0.0.1',
    description='end to end ml project',
    author='abhinav',
    author_email="mazumdarabhinav@gmail.com",
    license='MIT',
    install_requires=get_requirements(REQUIREMENTS_PATH)
)
