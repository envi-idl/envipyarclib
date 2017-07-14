"""
"""

import unittest
import arcpy


class TestDataTypeLong64Array(unittest.TestCase):
    """Tests the 64-bit long array task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_long64array',
                                 'test_datatype_long64array')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_long64array_one_dimension(self):
        """Verify a one dimensional array of 64-bit longs returns a semicolon separated string list."""
        input = [0, 2147483647, -40002]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_Long64Array_TEST(input, expect_dims)
        self.assertEqual(result[0], ';'.join(str(i) for i in input))