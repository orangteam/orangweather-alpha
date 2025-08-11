from setuptools import setup

setup(
    name="WeatherResources",
    version="0.1.1",
    description="A simple weather app",
    author="KMAR",
    author_email="kmaripradio@gmail.com",
    packages=["WeatherResources"],
    install_requires=[
        "requests",
        "geopy",
    ],
    entry_points={
        "console_scripts": [
            "WeatherResources=WeatherResources:main",
        ],
    },
)

