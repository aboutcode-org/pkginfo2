# requirements

def additional_tests():
    import doctest
    import unittest
    return unittest.TestSuite((
        doctest.DocFileSuite('../../docs/index.rst',
                                module_relative=True),
        doctest.DocFileSuite('../../docs/distributions.rst',
                                module_relative=True),
        doctest.DocFileSuite('../../docs/metadata.rst',
                                module_relative=True),
        doctest.DocFileSuite('../../docs/indexes.rst',
                                module_relative=True),
    ))


def _checkSample(testcase, installed):
    try:
        import pkg_resources
    except ImportError: # no setuptools :(
        pass
    else:
        version = pkg_resources.require('pkginfo')[0].version
        testcase.assertEqual(installed.version, version)
    testcase.assertEqual(installed.name, 'pkginfo')
    testcase.assertEqual(installed.keywords,
                        'distribution sdist installed metadata' )
    testcase.assertEqual(list(installed.supported_platforms), [])

def _checkClassifiers(testcase, installed):
    testcase.assertEqual(list(installed.classifiers),
                         [
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2.5',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: System :: Software Distribution',
    ])
