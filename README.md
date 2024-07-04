# JSON to VCF Converter

This is a Python script that converts a JSON file containing contact information into a VCF (vCard) file. This script reads a JSON file with contact details and generates a corresponding VCF file, which can be imported into various contact management applications. You can use this script to convert your Telegram contacts JSON file to VCF format.

## Features
- Converts JSON formatted contact data to VCF format.
- Handles Unicode characters in the JSON file.
- Checks for the existence of the JSON file and its content.
- Writes the VCF file with appropriate encoding.

## Prerequisites
- Python 3.x
- Ensure you have the required permissions to read and write files in the directory where you are running the script.

## Usage
1. Save the script to a file, e.g., `json_to_vcf.py`.
2. Prepare your JSON file containing contact information in the following format:
    ```json
    [
        {
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "+123456789",
            "date": "2024-07-04T12:34:56Z"
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "phone_number": "+987654321"
        }
    ]
    ```
3. Run the script from the command line:
    ```bash
    python json_to_vcf.py
    ```
4. When prompted, enter the name of the JSON file (including the `.json` extension).

## Example
```bash
$ python json_to_vcf.py
Enter the name of the input JSON file (with .json extension): contacts.json
Contacts have been written to contacts.vcf
```

## Script Explanation

The script consists of two main functions:
- `json_to_vcf(json_file, vcf_file)`: This function reads the JSON file, processes the contact information, and writes it to a VCF file.
- `main()`: This function prompts the user for the input JSON file name, checks if the file exists, and calls the `json_to_vcf` function to perform the conversion.

### Detailed Breakdown
- The script begins by importing the required modules: `json` for handling JSON data and `os` for file operations.
- The `json_to_vcf` function:
  - Loads the JSON data from the specified file with UTF-8 encoding.
  - Checks if the JSON data is not empty.
  - Constructs the VCF content by iterating through each contact in the JSON file.
  - Writes the constructed VCF content to the specified VCF file.
- The `main` function:
  - Prompts the user for the input JSON file name.
  - Checks if the specified file exists.
  - Defines the output VCF file name.
  - Calls the `json_to_vcf` function to perform the conversion.
- The script runs the `main` function if it is executed as the main module.

### Error Handling
- The script handles `UnicodeDecodeError` when reading the JSON file and `IOError` when writing to the VCF file.
- It also checks if the JSON file exists and if the JSON data is not empty or incorrectly formatted.

## Converting Telegram JSON
- You can use this script to convert your Telegram contacts JSON file to VCF format. Export your Telegram contacts to a JSON file and follow the usage instructions to convert it to a VCF file.

## Notes
- Ensure your JSON file is properly formatted and contains the required fields: `first_name`, `last_name`, `phone_number`, and `date` (optional).
- The script generates a VCF file named `contacts.vcf` in the same directory as the script.

Feel free to modify the script to suit your specific needs.
