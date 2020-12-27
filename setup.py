from setuptools import setup

setup(
    name="parler-api",
    version="1.0",
    description="Reverse engineered Parler API",
    author="d0nk",
    author_email="",
    packages=["parler_api"],
    install_requires=[
        "requests",
    ]
)
