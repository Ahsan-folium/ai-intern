# added for the branch PR
import pandas as pd
import os

def get_file(file_name):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file_name)
    return file_path

def get_average_df(file_name):

    file_path =   get_file(file_name)
    df = pd.read_csv(file_path)

    print(df)

    # this takes all columns except the name
    subjects = df.iloc[: , 1:]

    print(subjects)

    # now we calculate the average 
    # axis 1 calculates row-wise mean , axis 0 would do it column wise
    averages = subjects.mean(axis=1)  
    print(averages)

    # assign averages in a new column called average 

    df['Average'] = averages

    df.rename(columns={'name': 'Name'}, inplace=True)

    print(df)
    
    # now we create a new df , containgig name and averages and contain them into a new csv file 

    summary_df = df[['Name' , 'Average']]
    print(summary_df)
    return summary_df


def generate_csv(file_name):
    summary_df = get_average_df(file_name)
     # Get the directory of the current Python file
    script_dir = os.path.dirname(__file__)

    # Build full path to save in the same folder
    output_path = os.path.join(script_dir, "summary.csv")


    summary_df.to_csv(output_path, index=False)



generate_csv("students.csv")

def generate_csv_old():

    # first we get the path 
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "students.csv")

    df = pd.read_csv(file_path)

    print(df)

    # this takes all columns except the name
    subjects = df.iloc[: , 1:]

    print(subjects)

    # now we calculate the average 
    # axis 1 calculates row-wise mean , axis 0 would do it column wise
    averages = subjects.mean(axis=1)  
    print(averages)

    # assign averages in a new column called average 

    df['Average'] = averages

    df.rename(columns={'name': 'Name'}, inplace=True)

    print(df)


    # now we create a new df , containgig name and averages and contain them into a new csv file 

    summary_df = df[['Name' , 'Average']]
    print(summary_df)

    # Get the directory of the current Python file
    script_dir = os.path.dirname(__file__)

    # Build full path to save in the same folder
    output_path = os.path.join(script_dir, "summary.csv")


    summary_df.to_csv(output_path, index=False)






