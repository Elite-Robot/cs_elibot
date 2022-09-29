from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup, find_packages



d = generate_distutils_setup(
    name="cs_driver",
    version="1.0.0",
    author="",
    author_email="akashgarg@elibot.cn",
    description="The cs_driver package",
    packages=['cs_driver'],
    package_dir={'': 'src'}
)

setup(**d)
