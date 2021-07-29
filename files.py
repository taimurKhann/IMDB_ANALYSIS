import urllib.request as req
import pandas as pd

def file_downloader(links):
    """ Function to download files from link and save into data folder
    Args:
        links:  List of links to be downloaded
    """
    print('Files Downloading Started...')
    for link in links:
        try:
            filename = link.split('/')[-1]
            req.urlretrieve(link, 'data/'+filename)
            print(filename+' downloaded...')
        except Exception as error:
            print('Error in link '+link,error)
            return 0
    print('Files Downloading Completed...')


def file_to_dataframe(filename):
    """ Function to convert file to dataframe
    Args:
        filename: name of file to convert to Dataframe
    
    Returns:
        dataframe object of file
    """
    try:
        df = pd.read_csv('data/'+filename, sep='\t', compression='gzip', dtype=object)
    except Exception as error:
        print(error)
        return 0

    return df


def dataframe_to_file(df, filename):
    """ Function to save pandas dataframe to file
    Args:
        df: dataframe which needs to be write to file
        filename: name of the file on disk
    """
    df.to_csv(filename, index=False, sep='\t', header=True)