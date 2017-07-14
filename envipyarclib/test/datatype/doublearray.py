"""

"""
import unittest


import arcpy


class TestDataTypeDoubleArray(unittest.TestCase):
    """Tests the double array task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_doublearray',
                                 'test_datatype_doublearray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_doublearray_one_dimension(self):
        """Verify a one dimensional array of doubles returns a semicolon separated string list."""
        input = [0, 5.64777, -254.9]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_DoubleArray_TEST(input, expect_dims)
        resultArr = result.getOutput(0).split(';')
        for index in range(len(input)):
            self.assertAlmostEqual(input[index],float(resultArr[index]),places=6)