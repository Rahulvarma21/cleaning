import pandas as pd

# read
df = pd.read_excel('Customer Call List.xlsx')
# print(df.info)
# print(df.head())

#dropping the column that is not useful for our analysis
df = df.drop(columns=['Not_Useful_Column'])

#removed extra spaces from the first name column
df['First_Name'] = df['First_Name'].str.strip()

#removed extra characters from the last name column
df['Last_Name'] = df['Last_Name'].str.strip('123._/')

#removed duplicates from the dataset
df = df.drop_duplicates()

#cleaned the phone number column by removing any non-numeric characters and formatting it in a standard way
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','', regex=True)
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#removed any rows with missing values in the phone number column
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--','')

#split the address column into separate columns for street address, state, and zip code
df[['Street_Adress', 'State', 'Zip_Code']] = df['Address'].str.split(',',n=2, expand=True)

#removed any extra spaces from the new columns
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')

#replaced any remaining missing values with an empty string
df = df.replace('N/a','')
df = df.fillna('')

#removed any rows where the customer has indicated that they do not want to be contacted or where the phone number is missing
df = df[df['Do_Not_Contact'] != 'Y']

#removed any rows where the phone number is missing
df = df[df['Phone_Number'] != '']

#reset the index of the cleaned dataset
df = df.reset_index(drop=True)
