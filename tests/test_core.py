import unittest
from pandas.util.testing import assert_frame_equal
from python_scripts import core
import pandas as pd


class TestCore(unittest.TestCase):

    def test_read_csvs(self):
        path = r'tests/csv_files'

        df = core.read_csvs(path)
        df_expected = pd.DataFrame(
                        {
                            'col1': ['c11', 'c21', 'c31', 'b11', 'b21', 'b31', 'a11', 'a21', 'a31'],
                            'col2': ['c12', 'c22', 'c32', 'b12', 'b22', 'b32', 'a12', 'a22', 'a32'],
                            'col3': ['c13', 'c23', 'c33', 'b13', 'b23', 'b33', 'a13', 'a23', 'a33']
                        }
                    )
        assert_frame_equal(
            df,
            df_expected
        )