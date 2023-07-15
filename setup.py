from setuptools import find_packages,setup
from typing import List


HYPHEN_DOT_E="-e ."
def get_requirements(file_path)->List[str]:
    requirements=[]
    with open(file_path) as file_str:
        requirements=file_str.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)




setup(
    name="data_practice",
    version="0.0.1",
    author="Kamesh",
    author_email="karankewlani1997@gmail.com",
    packages=find_packages(),
    install_packages=get_requirements('requirements.txt')
    
    )