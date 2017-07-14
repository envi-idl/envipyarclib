"""
"""

import unittest
import arcpy


class TestDataTypeUInt(unittest.TestCase):
    """Tests the uint task datatype"""

    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_uint',
                                 'test_datatype_uint')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_uint_max(self):
        """Tests the uint datatype."""
        input = 65535
        result = arcpy.QA_IDLTaskEngine_DataType_UInt_TEST(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_uint_min(self):
        """Tests the uint datatype."""
        input = 0
        result = arcpy.QA_IDLTaskEngine_DataType_UInt_TEST(input)

        self.assertEqual(int(result.getOutput(0)), int(input))