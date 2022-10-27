from typing import List

from setuptools import find_packages, setup


def get_requirments()->List[str]:
    """
    this function returns a list of requiremnets
    """
    requirement_list:List[str]=[]
    with open("requirements.txt") as requirement_file:
        requirement_lists = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_lists]
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
    
    return requirement_list

setup(
    name='sensor-fault-detection',
    version='1.0',
    author='Athul',
    author_email='velagapudiathul@gmail.com',
    packages =find_packages(),
    install_requires=get_requirments(),
    
)

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="avnish@ineuron.ai",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)
