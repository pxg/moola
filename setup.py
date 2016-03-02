from __future__ import absolute_import
import re
from setuptools import find_packages
from setuptools import setup


# Dynamically pull the version from file
# http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
VERSIONFILE = 'moola/_version.py'
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))


setup(
    name='moola',
    version=verstr,
    description='moola money tools',
    classifiers=['Private :: Do Not Upload'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['moola = moola.shell:create_sheet_for_month']
    })
