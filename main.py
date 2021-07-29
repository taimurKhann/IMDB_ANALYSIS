import pandas as pd
import files as file_handler
import transformation

links = [
    'https://datasets.imdbws.com/name.basics.tsv.gz',
    'https://datasets.imdbws.com/title.akas.tsv.gz',
    'https://datasets.imdbws.com/title.basics.tsv.gz',
    'https://datasets.imdbws.com/title.crew.tsv.gz',
    'https://datasets.imdbws.com/title.episode.tsv.gz',
    'https://datasets.imdbws.com/title.principals.tsv.gz',
    'https://datasets.imdbws.com/title.ratings.tsv.gz'
]

files_dict = {
    'name'       : 'name.basics.tsv.gz',
    'akas'       : 'title.akas.tsv.gz',
    'basics'     : 'title.basics.tsv.gz',
    'crew'       : 'title.crew.tsv.gz',
    'episode'    : 'title.episode.tsv.gz',
    'principals' : 'title.principals.tsv.gz',
    'ratings'    : 'title.ratings.tsv.gz'
}


if __name__ == '__main__':

    # downloading data files
    file_handler.file_downloader(links)

    # Getting dataframe of files
    basics_df = file_handler.file_to_dataframe(files_dict['basics'])
    akas_df   = file_handler.file_to_dataframe(files_dict['akas'])


    # get average duration of movies by year
    basics_final_df = transformation.avg_duration_movies_by_year(basics_df)
    # writing result to file
    file_handler.dataframe_to_file(basics_final_df, 'Task1.tsv')
    print('Average duration of movies per year calculated...')


    # get highest duration movies
    final_df = transformation.top_highest_duration_movies(basics_df, akas_df)
    # writing result to file
    file_handler.dataframe_to_file(final_df, 'Task2.tsv')
    print('Highest duration movies calculated...')

