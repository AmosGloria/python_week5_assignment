# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file and write initial content
        with open('my_file.txt', 'w') as file:
            file.write("First line: Hello, world!\n")
            file.write("Second line: Number 42\n")
            file.write("Third line: Python is fun!\n")
        print("File created and initial content written.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Finished creating the file.")

def read_file():
    try:
        # Read the contents of the file and display them
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nContents of the file:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Finished reading the file.")

def append_to_file():
    try:
        # Append additional lines to the existing content
        with open('my_file.txt', 'a') as file:
            file.write("Fourth line: Appending more text.\n")
            file.write("Fifth line: Another line of text.\n")
            file.write("Sixth line: Python file handling is easy!\n")
        print("Additional lines appended to the file.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Finished appending to the file.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Re-reading to show the appended content
