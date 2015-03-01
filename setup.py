from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='script-skeleton',

    version='0.1',

    description='A little program that creates skeletons of human readable scripts',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/marrcio/script-skeleton',

    # Author details
    author='Marcio Ramos',
    author_email='cubomarrcio@gmail.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Other Audience',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='utility text',

    packages=find_packages(),

    install_requires=['nose'],

    extras_require = {},

    package_data={},

    entry_points={
        'console_scripts': [
            'script-skeleton = scriptskeleton.cmdline:execute'
        ],
    },
)
