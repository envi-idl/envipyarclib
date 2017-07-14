"""
"""

import unittest

import arcpy

class TestDataTypeLongArray(unittest.TestCase):
    """Tests the long array task datatype"""

    config = None

    @classmethod
    def setUpClass(cls):
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_longarray',
                                 'test_datatype_longarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_longarray_one_dimension(self):
        """Verify a one dimensional array of longs returns a semicolon separated string list."""
        input = [0, 2147483647, -2147483647]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_LongArray_TEST(input, expect_dims)
        self.assertEqual(result[0], ';'.join(str(i) for i in input))