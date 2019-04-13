from setuptools import setup, find_packages
import sys

sys.path.append('./builder')
sys.path.append('./tests')

setup(
        name = 'StoryBuilder',
        version = '0.1',
        description = "This is a tool for construct a story",
        packages = find_packages(),
        test_suite = 'test_all.suite'
)
