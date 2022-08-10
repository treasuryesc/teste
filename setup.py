from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in teste/__init__.py
from teste import __version__ as version

setup(
	name="teste",
	version=version,
	description="Teste",
	author="TEste",
	author_email="teste",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
