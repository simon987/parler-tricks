from setuptools import setup

setup(
    name="parler_api",
    version="1.0",
    description="Reverse engineered Parler API",
    author="d0nk",
    author_email="",
    packages=["parler"],
    install_requires=[
        "requests",
    ]
)
