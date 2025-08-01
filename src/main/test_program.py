import pytest
import os
from program import   get_average_df , get_file , generate_csv
import pandas as pd

FILE = "students.csv"

# using a fixture so we get the dataframe that gives us the name and avg dataframe and we dont have to generate it again and again

@pytest.fixture
def summary_df():
    return get_average_df(FILE)


#1 . check if file is valid csv file

def test_file_is_valid_csv():
    try:
        pd.read_csv(get_file(FILE))
    except Exception as e:
        pytest.fail(f"students.csv is not a valid CSV file: {e}")



#2 check if the avg column exists in this dataframe

def test_average_column_exists(summary_df):
    assert 'Average' in summary_df.columns, "Average column not found in output."


#3 test the average values generated

def test_average_values(summary_df):
    # Load original to calculate expected averages
    file = get_file(FILE)
    df = pd.read_csv(file)
    expected_averages = df.iloc[:, 1:].mean(axis=1).round(2)
    actual_averages = summary_df['Average'].round(2)

    # Check values are close enough
    assert all(expected_averages == actual_averages), "Average values mismatch."

# check if the csv was generated

def test_summary_csv_written():
    generate_csv(FILE)
    assert os.path.exists(get_file("summary.csv")), "summary.csv was not created."