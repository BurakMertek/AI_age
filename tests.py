from functions.get_files_info import get_files_info
from functions.run_python import run_python_file


def test():
    
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print("")

    
    print("Testing run_python_file:")
    print("=" * 50)
    
   
    print("Test 1: run_python_file('calculator', 'main.py')")
    result = run_python_file("calculator", "main.py")
    print(result)
    print("")
    
    
    print("Test 2: run_python_file('calculator', 'tests.py')")
    result = run_python_file("calculator", "tests.py")
    print(result)
    print("")
    
    
    print("Test 3: run_python_file('calculator', '../main.py')")
    result = run_python_file("calculator", "../main.py")
    print(result)
    print("")
    
    
    print("Test 4: run_python_file('calculator', 'nonexistent.py')")
    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    print("")


if __name__ == "__main__":
    test()