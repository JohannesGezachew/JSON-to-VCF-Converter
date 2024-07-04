import json
import os

# Function to convert JSON to VCF
def json_to_vcf(json_file, vcf_file):
    # Load JSON data from the file with the correct encoding
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            contacts = json.load(file)
    except UnicodeDecodeError as e:
        print(f"Error reading the JSON file: {e}")
        return

    # Check if the JSON data is not empty
    if not contacts:
        print("The JSON file is empty or not formatted correctly.")
        return

    # Create VCF content
    vcf_content = ""
    for contact in contacts:
        vcf_content += "BEGIN:VCARD\n"
        vcf_content += "VERSION:3.0\n"
        if "first_name" in contact and "last_name" in contact:
            vcf_content += f"N:{contact['last_name']};{contact['first_name']};;;\n"
            vcf_content += f"FN:{contact['first_name']} {contact['last_name']}\n"
        elif "first_name" in contact:
            vcf_content += f"FN:{contact['first_name']}\n"
        elif "last_name" in contact:
            vcf_content += f"FN:{contact['last_name']}\n"

        if "phone_number" in contact:
            vcf_content += f"TEL;TYPE=CELL:{contact['phone_number']}\n"

        if "date" in contact:
            vcf_content += f"REV:{contact['date']}\n"

        vcf_content += "END:VCARD\n"

    # Write to VCF file
    try:
        with open(vcf_file, 'w', encoding='utf-8') as file:
            file.write(vcf_content)
        print(f"Contacts have been written to {vcf_file}")
    except IOError as e:
        print(f"Error writing to the VCF file: {e}")

# Main function
def main():
    # Prompt the user for the input JSON file name
    json_file = input("Enter the name of the input JSON file (with .json extension): ").strip().strip('"')
    
    # Check if the file exists
    if not os.path.isfile(json_file):
        print(f"File '{json_file}' not found.")
        return

    # Define the output VCF file name
    vcf_file = 'contacts.vcf'

    # Convert JSON to VCF
    json_to_vcf(json_file, vcf_file)

# Run the main function
if __name__ == "__main__":
    main()
