def modify_file_content(content):
    return content.upper()

def read_and_write_file():
    try:
        input_filename = input("Enter the name of the file to read: ")
        
        with open(input_filename, 'r') as infile:
            content = infile.read()
            
        modified_content = modify_file_content(content)

        # Ask the user for the output file name
        output_filename = input("Enter the name of the file to write to: ")
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content successfully modified and written to {output_filename}.")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the file name and try again.")
    except PermissionError:
        print("Error: You do not have permission to read or write one of the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()
