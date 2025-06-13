from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="datacleaner",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy==2.3.0",
        "pandas==2.3.0"
    ],
    author="Troy Anthony Barker",
    description="Una librería de Python para la limpieza de datos utilizando pandas.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TroyAnthonyBarker/datacleaner.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 