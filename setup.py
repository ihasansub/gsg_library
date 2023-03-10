from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in library/__init__.py
from library import __version__ as version

setup(
	name="library",
	version=version,
	description="library management",
	author="iyad",
	author_email="iyad@iyad",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
