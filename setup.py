from setuptools import setup

setup(
    name='cli-tools',
    version='1.0',
    py_modules=['weather', 'neo'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'weather = weather:main',
            'neo = neo:main',
        ],
    },
)
