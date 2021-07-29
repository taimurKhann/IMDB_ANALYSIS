import unittest
import pandas as pd
import files as f
import transformation as t
import gzip

valid_url = "https://datasets.imdbws.com/title.ratings.tsv.gz"
invalid_url = "https://datasets.imdbwsdsdsd.comsd/ratings.tsv.gz"

valid_file = "test.basics.tsv.gz"
invalid_file = "testtt.basics.tsv.gz"

class Testing(unittest.TestCase):

    def test_file_downloader(self):
        """ Testing file downloaded function """
        
        self.assertNotEqual(
            f.file_downloader([valid_url]),
            0
        )

        self.assertEqual(
            f.file_downloader([invalid_url]),
            0
        )


    def test_file_to_dataframe(self):
        """ Testing file conversion to dataframe function """

        self.assertTrue(
            isinstance(
                f.file_to_dataframe(valid_file),
                pd.DataFrame
            )
        )

        self.assertFalse(
            isinstance(
                f.file_to_dataframe(invalid_file),
                pd.DataFrame
            )
        )

    
    def test_avg_duration_movies_by_year(self):
        """ Testing function on subset of data """

        df = f.file_to_dataframe(valid_file)
        final_df = t.avg_duration_movies_by_year(df)
        val_list = final_df.loc[0, :].values.tolist()
        
        self.assertTrue(
            val_list[0] == 2000.0 and val_list[1] == 90.5
        )


if __name__ == '__main__':
    unittest.main()