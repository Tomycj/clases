import argparse

def remove_json_property(input_file, output_file, matching_string):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    output_lines = []
    skip_lines = False
    deleted_lines_counter = 0

    for line in lines:
        if matching_string in line:
            skip_lines = True  # Start skipping lines
        
        if skip_lines:
            if ']' in line or '}' in line:
                skip_lines = False  # Stop skipping when closing bracket is found
            deleted_lines_counter += 1
            continue  # Skip the closing bracket line

        output_lines.append(line)  # Keep the line if not skipping

    print(f"{deleted_lines_counter} lines deleted.")

    # Write the modified lines to a new file
    with open(output_file, 'w') as file:
        file.writelines(output_lines)

# Usage example:
#input_file_path = 'elements.json'
#output_file_path = 'elements2.json'
#matching_string = input('enter string to match: ')

parser = argparse.ArgumentParser(description='Remove array or object properties from a JSON file.')
parser.add_argument('input_file', help='Path to the input JSON file')
parser.add_argument('target_string', help='String in the property name to be matched')
parser.add_argument('--output_file', default='output.json', help='Path to the output JSON file (default: output.json)')

args = parser.parse_args()

remove_json_property(args.input_file, args.output_file, args.target_string)
