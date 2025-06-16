from functions.get_files_info import get_files_content, write_file


def test():
    
    result = get_files_content("calculator", "main.py")
    print("Result for 'main.py':")
    print(result)
    print("-" * 50)
    
    result = get_files_content("calculator", "pkg/calculator.py")
    print("\nResult for 'pkg/calculator.py':")
    print(result)
    print("-" * 50)
    
    result = get_files_content("calculator", "/bin/cat")
    print("\nResult for '/bin/cat':")
    print(result)
    print("-" * 50)
    
    
    print("\n\n=== TESTING write_file ===\n")
    
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for writing 'lorem.txt':")
    print(result)
    print("-" * 50)
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("\nResult for writing 'pkg/morelorem.txt':")
    print(result)
    print("-" * 50)
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("\nResult for writing '/tmp/temp.txt':")
    print(result)
    print("-" * 50)


if __name__ == "__main__":
    test()