def main():
    """
    Main function to handle file reading, modifying, and writing with error handling.
    """
    print("=== File Processor with Error Handling ===")
    
    # Ask user for input filename
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            print(f"\nSuccessfully read file '{input_filename}'")
            print(f"File size: {len(content)} characters")
            
            # Show first 100 characters of content (if available)
            preview_length = min(100, len(content))
            print(f"\nPreview of content (first {preview_length} characters):")
            print(content[:preview_length] + ("..." if len(content) > preview_length else ""))
            
            # Ask for modification choice
            print("\nHow would you like to modify the file?")
            print("1. Convert to uppercase")
            print("2. Convert to lowercase")
            print("3. Add line numbers")
            print("4. Replace a word")
            
            choice = input("Enter your choice (1-4): ")
            
            # Process based on user choice
            if choice == '1':
                modified_content = content.upper()
                modification_desc = "Converted to uppercase"
            elif choice == '2':
                modified_content = content.lower()
                modification_desc = "Converted to lowercase"
            elif choice == '3':
                lines = content.split('\n')
                modified_content = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(lines))
                modification_desc = "Added line numbers"
            elif choice == '4':
                word_to_replace = input("Enter word to replace: ")
                replacement_word = input("Enter replacement word: ")
                modified_content = content.replace(word_to_replace, replacement_word)
                modification_desc = f"Replaced '{word_to_replace}' with '{replacement_word}'"
            else:
                print("Invalid choice. Using original content.")
                modified_content = content
                modification_desc = "No modifications made"
            
            # Ask for output filename
            output_filename = input("\nEnter name for the output file: ")
            
            # Write to output file
            try:
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                print(f"\nSuccess! {modification_desc}")
                print(f"Modified content written to '{output_filename}'")
            except IOError as e:
                print(f"\nError writing to output file: {e}")
            except Exception as e:
                print(f"\nUnexpected error during file writing: {e}")
                
    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please check the filename and try again.")
    except PermissionError:
        print(f"\nError: You don't have permission to read '{input_filename}'.")
    except UnicodeDecodeError:
        print(f"\nError: Unable to decode '{input_filename}'. It may be a binary file.")
    except IOError as e:
        print(f"\nI/O error occurred: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        
    print("\nProgram completed.")

if __name__ == "__main__":
    main()
