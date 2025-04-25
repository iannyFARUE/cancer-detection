import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
__version__ = "0.0.0"
REPO_NAME = "cnnClassifier"
AUTHOR_USER_NAME = "ianmadhara"
AUTHOR_EMAIL = "iannyfarai@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN image classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)