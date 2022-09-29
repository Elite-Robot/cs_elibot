from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup, find_packages



d = generate_distutils_setup(
    name="cs_msgs",
    version="1.0.0",
    author="",
    author_email="akashgarg@elibot.cn",
    description="The cs_msgs package",
    packages=['cs_msgs'],
    package_dir={'': 'include'}
)

setup(**d)
