from setuptools import find_packages, setup


setup(
    name="dublin_bikes_ml",
    version="0.0.1",
    description="Machine Learning Utilities for Dublin Bikes 2.0",
    author="John McLoughlin",
    author_email="john.mc-loughlin.3@ucdconnect.ie",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask", 'pytest'
    ],
)