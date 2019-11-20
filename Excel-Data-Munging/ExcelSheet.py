
import _sqlite3
import pandas as pd
import glob
#first we import all the necessary dependicies.
# since all of the excel files are in the same folder we will first create an array then loop through
all_data = pd.DataFrame()
#We use the glob module to search through a specified directory, and *. file extension to denote which file that
# you are searching for. We use a for loop to loop through the directory, to get all files, and then we merge
#  them sequentially.
for file in glob.glob("datasets/*"):
    df = pd.read_excel(file, sheetname= 1)
    all_data = all_data.append(df, ignore_index=True)

#Now that we have all the data in a dataframe, we can create a database, that can be viewed. eventually you do want to
#get a database to hold your infomration, as well as the data goverenance behind them as well.

conn = _sqlite3.connect('data-1.db')
c = conn.cursor()

all_data.to_sql('collated', con= conn)

conn.commit()