from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lessons-tap",
    version="1.0.0",
    author="Andrii Sidachenko",
    author_email="a.sidachenko@gmail.com",
    description="Python lessons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrQanderson/Python-TAP.git",
    packages=find_packages(
        exclude=["draft_*"]
    ),
    python_requires=">3.7",
    install_requires=[
        "prettytable>=3.2.0",
        "loguru>=0.6.0"
    ],
)