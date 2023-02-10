"""
"""

import unittest
import os
import arcpy
import filecmp
import tempfile
from datetime import datetime as dt


class TestDataTypeENVITIME(unittest.TestCase):
    """Tests the ENVITIME task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_envitime',
                                 'test_datatype_envitime')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_envitime_string(self):
        """Tests the envitime datatype with file uri."""
        input = '8/20/2001 9:30:45 PM'
        result = arcpy.qa_envitaskengine_datatype_envitime_TEST(input)
        self.assertEqual(input, result.getOutput(0))

    def test_datatype_envitime_datetime(self):
        format = '%m/%d/%Y %H:%M:%S %p'
        input = dt.strptime('8/20/2001 9:30:45 PM', format)
        result = arcpy.qa_envitaskengine_datatype_envitime_TEST(input)
        output = dt.strptime(result.getOutput(0), format)
        self.assertEqual(input, output)
