"""
"""

import unittest
import arcpy

class TestDatatypeLong64(unittest.TestCase):
    """Tests the int task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_long64',
                                 'test_datatype_long64')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_long64_max(self):
        """Tests the long64 datatype maximum value."""
        # 32 bit long upper limit.  IDL long64 can handle up to 9223372036854775807 for long64 but arcpy cannot.
        input = 2147483647
        result = arcpy.QA_IDLTaskEngine_DataType_Long64_TEST(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_long64_min(self):
        """Tests the long64 datatype minimum value."""
        # 32 bit long lower limit.  IDL long64 can handle up to -9223372036854775808 for long64 but arcpy cannot.
        input = -2147483648
        result = arcpy.QA_IDLTaskEngine_DataType_Long64_TEST(input)

        self.assertEqual(int(result.getOutput(0)), int(input))