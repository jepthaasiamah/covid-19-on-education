import numpy as np
import pandas as pd

# reading the scraped csv file into a DataFrame 
raw_data = pd.read_csv('raw_data.csv')

# removing columns with 120 (all) missing values and leaving other columns for transformation
condition = raw_data.loc[:].isnull().sum() == 120
all_data = raw_data.drop(raw_data.loc[:, condition], axis=1)

# removed columns with only null values; shape changed; (120, 14) -> (120, 10) 
all_data.isnull().sum(), all_data.shape
# selecting columns with mostly null values as messy_data to be looked into for any valid data
messy_data = all_data[['7', '5', '9', '10', '12']] 

# multiple data types and levels of measure are in columns. data can be lost if this is ignored 
# need to identify main columns, group them then proceed to gathering remaining details which may be relevant to the final file

# working on messy data to identify non-null values and make required change
# messy_data.head(10) 
# messy_data.columns.values


# Ref column investigation - '9'
nine = pd.DataFrame(data=messy_data['9'])
ref_col_name = nine.loc[[0]]

# checking for non float objects to and skip them in the conversion later index them 
# working on remaining values of other data types which raised errors and caused division of column into sections
ref_index = nine[(messy_data.loc[:, '9'] == 'Ref')].index.values[0] # index of 
covid_index = nine[(messy_data.loc[:, '9'] == 'COVID-19 pandemic in Hong Kong')].index.values[0]
twenty7_index = nine[(messy_data.loc[:, '9'] == '[27]')].index.values[0]

section_91 = messy_data.loc[ref_index+1:covid_index-1, '9'].astype(float, errors='raise') # error = 'Ref' cannot be float
section_92 = messy_data.loc[covid_index+1:twenty7_index-1, '9'].astype(float, errors='raise') # 'COVID-19 pandemic...' cant be converted to float
section_93 = messy_data.loc[twenty7_index+1:, '9'].astype(float, errors='raise') # '[27]' is also a string
sections = pd.concat([section_91, section_92, section_93], axis=1)

# a look at all parts of the data to locate any information that may be part of the table or useful 
detail = pd.DataFrame(nine.loc[[ref_index, covid_index, twenty7_index]])


# number of learners enrolled in tertiary education programmes captioned column '5'
five = pd.DataFrame(data=messy_data['5'])
# this section contains null values 
section = five.loc[1:118, '5'].astype(float, errors='raise') # ValueError: could not convert string to float: '128,207,915'
# selecting misplaced value - at index 119
float_val = five[messy_data.loc[:, '5'] == '128,207,915']
# retrieving a column name from this misplaced column 
tertiary_col_name = pd.Series(five.loc[0, '5'])  # column = 'Number of learners enrolled in tertiary education programmes'
tertiary_col_name = str('Number of learners enrolled in tertiary education programmes')

# investigating 'additional information' column , '7'
info_col_name = messy_data.loc[0, '7']
seven = messy_data.loc[:, '7']
# selecting misplaced information 
details = seven[[29, 40, 58, 67, 84, 114, 111, 110]]

# investigating last two null captioned columns which are empty all the way through '[ '12', '10' ]
nulls = messy_data.iloc[:, [-1, -2]].astype(float, errors='ignore')
twelve_details = pd.Series(nulls.iloc[40, -2]) # non-null data in column , '12'
ten_details = pd.DataFrame(nulls.iloc[[29, 40, 58, 84, 110, 111, 114], -1])  # non-null data in column, '13'

# summarizing all retrieved data into a dataframe to have a better view of the misplaced columns and to use some to replace null values in the more complete table
all_details = pd.concat([float_val, twelve_details, details, detail, ten_details], keys=['col5', 'cites', 'additional_info', 'Ref', 'cites2'], axis=1)


# selecting the main columns, adding column names
all_data = all_data.loc[:, ['1', '3', '4', '6', '9']]
all_details = all_data.iloc[0, :]

# and filling in missing data using the details gathered
# all_data.loc[:, :]
# mapping required data into a dictionary sounds like a good idea
full_detail = { 
    'egypt' : str(all_data.loc[29, '6'] + details[29]),
    'kenya' : all_data.loc[58, '6'] + details.loc[58], 
    'phillipines' : all_data.loc[84, '6'] + details[84], 
    'turkey' : all_data.loc[110, '6'] + details[110],
    'turkm' : all_data.loc[111, '6'] + details[111],
    'united kingdom' : details[114]
    }

# filling in the missing columns in additional information. some of these are extra details which were misplaced while parsing html - only United Kingdom additional info was null with the required data falling into the wrong column.  
# all_data.loc[29, '6'] = eval(full_detail.get('egypt'))
all_data.loc[114, '6'] = str(full_detail.get('united kingdom'))  # united kingdom 
all_data.loc[84, '6'] = full_detail.get('phillipines')
all_data.loc[110, '6'] = full_detail.get('turkey')
all_data.loc[111, '6'] = full_detail.get('turkm')

# replacing the missing value in the last row, 'Total', column: Number of learners enrolled in tertiary education programmes with the float_val detail from the other columns in messy_data
all_data.loc[119, '4'] = (str(float_val['5']))
all_data.loc[119, '4'] = str(all_data.loc[119, '4']).split()[1]

# setting column names 
all_data.columns = [all_data.loc[0, '1'], all_data.loc[0, '3'], str(tertiary_col_name), str(info_col_name), str(ref_col_name)]
all_data = all_data.rename(columns={'0 Number of learners enrolled in tertiary educat...\ndtype: object': 'Number of learners enrolled in tertiary education programmes'})


clean_data = all_data.drop(columns=['     9\n0  Ref'], axis=1) # dropping ref here 

# preparing 'numerical' columns for conversion
tertiary = (clean_data.iloc[:, -2].replace(['—a', '—', np.NaN], '0')).str.replace(',', '')
formal = (clean_data.iloc[:, 1].replace(['—a', '—', np.NaN], '0')).str.replace(',', '')
info = (clean_data.iloc[:, -1]).replace(np.NaN, 'no record')
tf = pd.concat([tertiary, formal], keys=['tertiary', 'formal']) # inspecting the tertiary and formal columns 

# making conversions o||n data types 
formal_integer = pd.to_numeric(formal[1:], errors='raise', downcast='signed', )
tertiary_integer = pd.to_numeric(tertiary[1:], errors='raise', downcast='signed')

# integer column assignment 
clean_data['Number of learners enrolled from pre-primary to upper-secondary education'] = formal_integer
clean_data['Number of learners enrolled in tertiary education programmes'] = tertiary_integer

#  complete additional information column
clean_data['Additional information'] = info