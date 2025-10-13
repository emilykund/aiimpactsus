#!/usr/bin/env python3
"""
Text File to CSV Converter

This script demonstrates different methods to convert text files to CSV format.
It handles various text file formats including comma-separated, tab-separated,
and space-separated data.
"""

import csv
import pandas as pd
import argparse
import os
from pathlib import Path


def method1_csv_module(input_file, output_file, delimiter=','):
    """
    Method 1: Using Python's built-in csv module
    Best for: Simple conversions, full control over CSV formatting
    """
    print(f"Converting {input_file} to {output_file} using csv module...")
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            # Read lines and split by delimiter
            lines = infile.readlines()
            writer = csv.writer(outfile)
            
            for line in lines:
                # Strip whitespace and split by delimiter
                row = line.strip().split(delimiter)
                writer.writerow(row)
    
    print(f"✓ Conversion complete: {output_file}")


def method2_pandas(input_file, output_file, delimiter=','):
    """
    Method 2: Using pandas library
    Best for: Complex data manipulation, handling missing values, data analysis
    """
    print(f"Converting {input_file} to {output_file} using pandas...")
    
    try:
        # Read the text file
        df = pd.read_csv(input_file, delimiter=delimiter)
        
        # Save as CSV
        df.to_csv(output_file, index=False)
        
        print(f"✓ Conversion complete: {output_file}")
        print(f"Data shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
    except Exception as e:
        print(f"Error with pandas method: {e}")


def method3_manual_parsing(input_file, output_file, delimiter=','):
    """
    Method 3: Manual parsing with custom logic
    Best for: Complex text formats, custom validation, special requirements
    """
    print(f"Converting {input_file} to {output_file} using manual parsing...")
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            
            for line_num, line in enumerate(infile, 1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                # Split by delimiter and clean up each field
                fields = [field.strip() for field in line.split(delimiter)]
                
                # Optional: Add validation or data cleaning here
                # For example, validate that all fields are non-empty
                if all(fields):  # Only write if all fields have content
                    writer.writerow(fields)
                else:
                    print(f"Warning: Skipping line {line_num} due to empty fields")
    
    print(f"✓ Conversion complete: {output_file}")


def detect_delimiter(file_path, sample_lines=5):
    """
    Auto-detect the delimiter used in the text file
    """
    delimiters = [',', '\t', ';', '|', ' ']
    
    with open(file_path, 'r', encoding='utf-8') as file:
        sample = ''.join(file.readline() for _ in range(sample_lines))
    
    delimiter_counts = {}
    for delimiter in delimiters:
        delimiter_counts[delimiter] = sample.count(delimiter)
    
    # Return the delimiter with the highest count
    detected = max(delimiter_counts, key=delimiter_counts.get)
    print(f"Detected delimiter: '{detected}' (appears {delimiter_counts[detected]} times)")
    return detected


def convert_txt_to_csv(input_file, output_file=None, method='csv', delimiter=None):
    """
    Main conversion function
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        return
    
    # Generate output filename if not provided
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.with_suffix('.csv')
    
    # Auto-detect delimiter if not specified
    if delimiter is None:
        delimiter = detect_delimiter(input_file)
    
    print(f"Converting: {input_file} → {output_file}")
    print(f"Using delimiter: '{delimiter}'")
    print("-" * 50)
    
    # Choose conversion method
    if method == 'csv':
        method1_csv_module(input_file, output_file, delimiter)
    elif method == 'pandas':
        method2_pandas(input_file, output_file, delimiter)
    elif method == 'manual':
        method3_manual_parsing(input_file, output_file, delimiter)
    else:
        print(f"Unknown method: {method}")
        return
    
    print("-" * 50)
    print("Conversion completed successfully!")


def main():
    """
    Command-line interface
    """
    parser = argparse.ArgumentParser(description='Convert text files to CSV format')
    parser.add_argument('input_file', help='Input text file path')
    parser.add_argument('-o', '--output', help='Output CSV file path (optional)')
    parser.add_argument('-m', '--method', 
                       choices=['csv', 'pandas', 'manual'], 
                       default='csv',
                       help='Conversion method (default: csv)')
    parser.add_argument('-d', '--delimiter', 
                       help='Input file delimiter (auto-detect if not specified)')
    
    args = parser.parse_args()
    
    convert_txt_to_csv(
        input_file=args.input_file,
        output_file=args.output,
        method=args.method,
        delimiter=args.delimiter
    )


if __name__ == "__main__":
    # Example usage when run directly
    print("Text File to CSV Converter")
    print("=" * 50)
    
    # Convert the sample file using different methods
    sample_file = "sample_data.txt"
    
    if os.path.exists(sample_file):
        print("Converting sample file using different methods:\n")
        
        # Method 1: CSV module
        convert_txt_to_csv(sample_file, "output_csv_module.csv", "csv")
        print()
        
        # Method 2: Pandas
        convert_txt_to_csv(sample_file, "output_pandas.csv", "pandas")
        print()
        
        # Method 3: Manual parsing
        convert_txt_to_csv(sample_file, "output_manual.csv", "manual")
        
    else:
        print("Sample file not found. Run with command line arguments:")
        print("python txt_to_csv_converter.py your_file.txt")
        main()