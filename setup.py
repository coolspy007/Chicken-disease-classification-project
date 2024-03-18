import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-disease-classification-project"
AUTHOR_USER_NAME = "coolspy007"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "krishnakumar.balu@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)