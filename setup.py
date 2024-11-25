from setuptools import find_packages,setup #this will automatically find out all the packages that are available in the entire ML application, in the directory that we have actually created
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

## META-DATA information about the entire project
setup(
name='mlproject',
version='0.0.1',
author='Niraj',
author_email='niraj.shinde619@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
) 