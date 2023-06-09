import runpy

import setuptools

DEV_REQUIREMENTS = [
    "black",
    "flake8",
    "isort",
    "jupyterlab",
    "pre-commit",
    "pytest",
]

# Parse requirements
install_requires = [line.strip() for line in open("requirements.txt").readlines()]

# Get long description
with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

__version__ = runpy.run_path("neural-jax/_version.py")["__version__"]

# Setup package
setuptools.setup(
    name="Neural-JAX",
    version=__version__,
    author="Sandesh Katakam",
    author_email="sandeshkatakam@gmail.com",
    description="A JAX Based Library for Deep Learning Algorithms and Model Architectures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Neural-JAX",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    extras_require={"dev": DEV_REQUIREMENTS},
)
