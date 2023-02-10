"""

"""
import os
from setuptools import setup
from distutils.core import Command as BaseCommand
from unittest import TestLoader, TextTestRunner


class TestCommand(BaseCommand):
    """Runs the package tests."""
    description = 'Runs all package tests.'

    user_options = [
        ('junit=', None,
         'outputs results to a results.xml file.')
    ]

    def initialize_options(self):
        self.junit = None

    def finalize_options(self):
        pass

    def run(self):
        # Import xmlrunner here so it's not a setup requirement
        import xmlrunner
        test_suite = TestLoader().discover('.')
        if self.junit:
            with open('report.xml', 'wb') as output:
                runner = xmlrunner.XMLTestRunner(output)
                runner.run(test_suite)
        else:
            runner = TextTestRunner(verbosity=2)
            runner.run(test_suite)

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(name='envipyarclib',
      version='1.0.11',
      description='ENVI Py Client Utilities for ArcGIS',
      long_description=long_description,
      url='https://github.com/envi-idl/envipyarclib',
      author='Harris Geospatial Solutions, Inc.',
      extras_require={
          'dev': [
            'coverage',
            'envipyengine>=1.0.5',
            'pylint',
            'Sphinx',
            'Sphinx-PyPI-upload',
            'sphinx_rtd_theme',
            'twine',
            'unittest-xml-reporting',
            'wheel'
          ]
      },
      packages=['envipyarclib',
                'envipyarclib.gptool',
                'envipyarclib.gptool.parameter',
                'envipyarclib.gptool.parameter.templates',
                'envipyarclib.test',
                'envipyarclib.test.datatype'],
      package_data={
          'envipyarclib': [
              'test/tasks/*.pro',
              'test/tasks/*.task',
              'test/tasks/*.sav',
              'test/data/*.dat',
              'test/data/*.hdr',
              'test/data/*.shp',
              'test/data/*.qtr',
              'test/data/*.prj',
              'test/data/*.shx',
              'test/data/*.xml',
              'test/data/*.gif',
              'test/data/*.series',
              'test/data/*.h5'
          ]
      },
      license='MIT',
      zip_safe=False,
      cmdclass=dict(test=TestCommand))
