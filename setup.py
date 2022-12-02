from setuptools import setup, find_packages  # noqa: H301

NAME = "whylogs-container-client"
VERSION = "0.0.6"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="whylogs container API",
    author_email="support@whylabs.ai",
    url="https://github.com/whylabs/whylogs-container-python-client",
    long_description_content_type="text/markdown",
    keywords=["swagger", "whylogs", "container", "client"],
    install_requires=REQUIRES,
    package_dir = {"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    long_description=long_description
)

