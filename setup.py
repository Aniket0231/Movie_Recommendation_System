from setuptools import setup 

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'ANIKET'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='aniketchess0231@gmail.com',
    description='A simple python package to make a simple web app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[SRC_REPO],  # Corrected from "package" to "packages"
    python_requires='>=3.7',  # Corrected key from "python_version" to "python_requires"
    install_requires=LIST_OF_REQUIREMENTS,
)
