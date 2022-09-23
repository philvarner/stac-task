import os
from setuptools import setup, find_packages
from glob import glob

from os.path import basename, splitext

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as readme_file:
    readme = readme_file.read()


setup(
    name="stactask",
    description=(
        "STAC Task class provides a class interface for running custom algorithms on STAC Items"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author=u"Matthew Hanson",
    author_email="matt.a.hanson@gmail.com",
    url="https://github.com/stac-utils/stactask",
    packages=find_packages(exclude=["tests*"]),
    package_data={"": ["py.typed", "*.jinja2"]},
    py_modules=[splitext(basename(path))[0] for path in glob("pystac/*.py")],
    python_requires=">=3.8",
    install_requires=[
        "python-dateutil>=2.7.0",
        "boto3-utils>=0.3.2",
        "jsonpath_ng>=1.5.3",
        "requests>=2.28.1",
    ],
    extras_require={
        "validation": ["jsonschema>=4.0.1"],
        "orjson": ["orjson>=3.5"]
    },
    license="Apache Software License 2.0",
    license_files=["LICENSE"],
    zip_safe=False,
    keywords=["pystac", "imagery", "raster", "catalog", "STAC"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    project_urls={
        "Tracker": "https://github.com/stac-utils/stactask/issues",
    },
    test_suite="tests",
    entry_points={"console_scripts": ["stactask = stactask.cli:cli"]},
)