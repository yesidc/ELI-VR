import pandas as pd
import argparse
import re
from NLP.utils import handle_pickle
from NLP.utils import list_of_columns_transcription
# setting up CLI


#TODO specify path to save pickle file

parser = argparse.ArgumentParser(description = "Text analysis")
parser.add_argument("transcription_csv", help = "path to the csv file containing the transcriptions")
parser.add_argument("output_dic", help = "path to the output directory")
args = parser.parse_args()


df = pd.read_csv(args.transcription_csv)
df = df[list_of_columns_transcription]
print('')

def create_condition_txt(column):
    #TODO this can be implemented using map()
    text=''
    for cell in column:
        if type(cell) != float:
            #TODO delete /n
            text = f'{text}  \n {str(cell)}'
            #text= text + '\n' + str(cell)
    return text

def create_text (df_transcription):
    """
    Creates a whole text from the transcriptions belonging to each condition.
    Args:
        df_transcription: Data frame containing the transcriptions

    Returns:

    """

    #this regex returns the name of the column
    column_regex = re.compile(r'([A-Za-z]*)\s?\_?([0-9]$)')
    #list of the columns
    columns = df_transcription.columns
    columns=columns[1:-1]
    #column_name= lambda count: column_regex.search(columns[count]).groups()[0]
    text={}
    for column in columns:
        text[column]=[create_condition_txt(df_transcription[column])]

    handle_pickle(args.output_dic,text)
create_text(df)
