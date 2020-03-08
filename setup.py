import setuptools

with open('README.md') as fp:
    long_description = fp.read()

setuptools.setup(
    name='pydel',
    version='0.5.1',
    description='Parser for Synthstrom Audible Deluge song files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dillon Cower',
    license='MIT',
    url='https://github.com/dcower/pydel',
    packages=setuptools.find_packages(),
    install_requires=[
        'attrs',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ])