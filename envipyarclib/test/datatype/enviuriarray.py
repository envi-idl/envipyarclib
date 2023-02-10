"""
"""

import unittest
import os
import arcpy


class TestDataTypeENVIURIArray(unittest.TestCase):
    """Tests the ENVIURIArray task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_enviuriarray',
                                 'test_datatype_enviuriarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_enviuriarray_uri(self):
        """Tests the enviuriarray datatype with file uri."""
        input = [ os.path.join(self.config.test_data_dir, 'checkerboard_1roi.xml'),
                  os.path.join(self.config.test_data_dir, 'checkerboard.hdr'),
                  os.path.join(self.config.test_data_dir, 'checkerboard.dat') ]

        result = arcpy.qa_envitaskengine_datatype_enviuriarray_TEST(input)
        self.assertEqual(';'.join(input).lower(), result[0].lower())

    def test_datatype_enviuriarray_string(self):
        """Tests the enviuriarray datatype with file uri."""
        input = [ 'foo.bar', 'tea.leaves', 'sar' ]

        result = arcpy.qa_envitaskengine_datatype_enviuriarray_TEST(input)
        self.assertEqual(input, result[0].split(';'))
