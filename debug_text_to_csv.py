import pandas as pd
from typing import Optional
import os


def convert_txt_to_csv(
    input_file: str,
    output_file: str,
    delimiter: Optional[str] = None,
    include_index: bool = False
) -> pd.DataFrame:
    """
    Reads data from a text file and converts it to CSV format.
    
    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output CSV file.
        delimiter (Optional[str]): The delimiter used in the text file. 
                                  If None, pandas will try to infer it.
        include_index (bool): Whether to include DataFrame index in the CSV output.
        
    Returns:
        pd.DataFrame: The DataFrame containing the data from the input file.
        
    Raises:
        FileNotFoundError: If the input file doesn't exist.
        ValueError: If the input file is empty or cannot be parsed.
    """
    # Check if input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")
    
    try:
        # Read the text file into a DataFrame using 'sep' parameter instead of 'delimiter'
        # If delimiter is None, try to infer it, otherwise use the specified delimiter
        if delimiter is None:
            data_df = pd.read_csv(input_file, sep=None, engine='python')
        else:
            data_df = pd.read_csv(input_file, sep=delimiter)
        
        # Check if DataFrame is empty
        if data_df.empty:
            raise ValueError("Input file is empty or could not be parsed.")
        
        # Write the DataFrame to a CSV file (pandas will use comma as default delimiter)
        data_df.to_csv(output_file, index=include_index)
        
        return data_df
        
    except pd.errors.EmptyDataError:
        raise ValueError("Input file is empty or contains no valid data.")
    except pd.errors.ParserError as e:
        raise ValueError(f"Error parsing input file: {e}")
    except Exception as e:
        raise ValueError(f"Unexpected error reading file: {e}")


# Example usage
if __name__ == "__main__":
    ms_data = convert_txt_to_csv(
        input_file='MS_2008_2013_Treatment_Data.txt',
        output_file='MS_2008_2013_Data.csv',
        delimiter='\t'  # Specify tab delimiter for the input file
    )
    print(ms_data)