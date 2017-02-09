from setuptools import setup, find_packages


setup(
    name='lsm-db-extras',
    version='0.1',
    author='Dmitry Orlov',
    author_email='me@mosquito.su',
    description='Thread/Process safe shelves and other lam-db helpers',
    long_description=open("README.rst"),
    license="Apache 2",
    packages=find_packages(".", exclude=['tests', 'doc']),
    install_requires=[
        "lsm-db",
    ],
    platforms="all",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Microsoft',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)