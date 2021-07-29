import pandas as pd


def avg_duration_movies_by_year(df):
    """ Function to manipulate df to get average duration of movies per year.
    Args:
        df: dataframe containing data of movies

    Returns:
        final_df: final dataframe containing result
    """

    df = df[ (df['titleType'].isin(['movie', 'tvMovie'])) & (df['startYear'] != '\\N') & (df['runtimeMinutes'] != '\\N') ]
    
    df = df.astype({
        'runtimeMinutes': 'int',
        'startYear': 'int'
    })
    
    df = df[ (df['startYear'] >= 2000) ]

    final_df = df.groupby('startYear').mean()
    final_df.reset_index(inplace=True)
    final_df.columns = ['Year', 'Average Duration']

    return final_df


def top_highest_duration_movies(basics_df, akas_df):
    """ Function to get top 100 highest duration movies 
    Args:
        basics_df: basics movie data df
        akas_df  : localized movie information df

    Returns:
        final_df: final dataframe containing result
    """
    basics_df = basics_df[ 
        (basics_df['titleType'].isin(['movie', 'tvMovie'])) & 
        (basics_df['startYear'] != '\\N') & 
        (basics_df['runtimeMinutes'] != '\\N') &
        (basics_df['originalTitle'] != '\\N') 
    ]

    basics_df = basics_df.astype({
        'runtimeMinutes': 'int',
        'startYear': 'int',
        'tconst': 'str'
    })

    basics_df = basics_df[ (basics_df['startYear'] >= 2000) ]

    akas_df['title'].fillna('\\N', inplace=True)
    akas_df = akas_df[ (akas_df['title'] != '\\N') ]

    akas_df = akas_df.astype({
        'titleId': 'str'
    })

    basics_df.rename(columns = {'tconst':'titleId'}, inplace = True)

    final_df = pd.merge(basics_df, akas_df, on='titleId')

    final_df = final_df[ (final_df['originalTitle'] != final_df['title']) ]

    final_df = final_df[[ 'title', 'region', 'language', 'runtimeMinutes' ]]

    final_df = final_df.sort_values(by=['runtimeMinutes'], ascending=False)

    del final_df['runtimeMinutes']

    final_df = final_df.head(100)

    return final_df