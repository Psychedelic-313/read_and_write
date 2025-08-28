# Ask the user for the filename
filename = input("Enter the filename: ")

try:
    # Open the file in read mode
    with open(filename, 'r') as original_file:
        content = original_file.read()

    # Modify the content (for example, convert to uppercase)
    modified_content = content.upper()

    # Create a new file to write the modified content
    new_filename = "modiffied_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified file created succesfully: {new_filename}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError:
    print(f"Error: The file '{filename}' cannot be read or written.")