import os

from setuptools import setup

extras = {
    'test_suite': 'pkginfo2.tests',
    'zip_safe': False,
}

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='pkginfo2',
    version='30.0.0',
    description='Query metadata from sdists / bdists / installed packages. Safer fork of pkginfo to avoid doing arbitrary imports and eval()',
    platforms=['Unix', 'Windows'],
    long_description='\n\n'.join([README, CHANGES]),
    long_description_content_type='text/x-rst',
    keywords='distribution sdist installed metadata',
    url='https://github.com/aboutcode-org/pkginfo2',
    author='Maintained by nexB, Inc. Authored by Tres Seaver, Agendaless Consulting',
    author_email='tseaver@agendaless.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Software Distribution',
    ],
    entry_points={
        'console_scripts': [
            'pkginfo2 = pkginfo.2commandline:main',
        ]
    },
    packages=['pkginfo2', 'pkginfo2.tests'],
    **extras
)
