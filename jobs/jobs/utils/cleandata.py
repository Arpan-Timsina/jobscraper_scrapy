import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('./output.csv')

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Split the value in the 'Contract Type' column by comma
    contract_type_parts = row['Contract Type'].split(', ')
    if len(contract_type_parts) == 2:
        # Update the 'Job Type' column with the value before the comma
        df.at[index, 'Job Type'] = contract_type_parts[0]
        # Update the 'Contract Type' column with the value after the comma
        df.at[index, 'Contract Type'] = contract_type_parts[1]

# Save the modified DataFrame back to a CSV file
df.to_csv('modified_file.csv', index=False)
