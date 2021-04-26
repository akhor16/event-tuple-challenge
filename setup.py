from setuptools import setup, find_namespace_packages

setup(
    name="event-tuple",
    version="0.0.1",
    install_requires=[
        'pytest'
    ],
    description="Event Tuple Challenge",
    packages=find_namespace_packages(include=['pokerdevs.*', 'tests.*', 'scripts.*']),
    entry_points={
      'console_scripts': [
      ]
    }    
)
