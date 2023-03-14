from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:

    with open(file_path) as f:
        requirements = [line.strip() for line in f]
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements



setup(
    name="genericml",
    version= "0.0.1",
    author = "Harshith",
    author_email="harshithreddymula20@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)