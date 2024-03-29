from setuptools import setup, version

setup(
    name="DataBinder",
    version="0.0.0",
    author="William E. Robinson",
    packages=["DataBinder"],
    install_requires=[],
    extras_require={
        "dev": [
            "pdoc",
            "mypy",
            "black",
            "pylint",
        ],
        "vis": [
            "graphviz",
        ],
    },
)
