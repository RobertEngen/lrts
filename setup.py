from setuptools import setup, find_packages

setup(
    name="lrts",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pyzmq',
    ],
    extras_require={
        'detailed_progress': ['enlighten', 'loguru']
    },
    entry_points={
        'console_scripts': [
            'lrts=lrts.cli:main'
        ]
    }
)
