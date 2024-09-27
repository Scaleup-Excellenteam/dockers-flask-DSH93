import requests


def print_landing_message():
    green = "\033[92m"
    yellow = "\033[93m"
    cyan = "\033[96m"
    reset = "\033[0m"
    
    message = f"""
    {yellow}===============================================================
       Welcome to the Multi-Language Code Execution Client!
   ==============================================================={reset}
   | This client allows you to submit and execute code           |
   | in Python, Java, and Dart.                                  | 
   |                                                             |
   | You can write your code in the example files                |
   | located in the 'router' directory:                          |
   |  - example.py for Python                                    |
   |  - example.java for Java                                    |
   |  - example.dart for Dart                                    |
   |                                                             |
   | The execution will be performed using the selected language.|
    ==========================================================={reset}
    """
    print(message)

def submit_code(language, code):
    print(f"Submitting code for language: {language}")
    response = requests.post(
        'http://localhost:5000/submit',
        data={'language': language, 'code': code}
    )
    print(response.json().get('status', 'Submission failed'))

def execute_code(language):
    print(f"Executing code for language: {language}")
    response = requests.get(f'http://localhost:5000/execute/{language}')
    print("Execution result:", response.json().get('output', 'Execution failed'))
    print("")
    
def user_input():
    while True:
        language = input("Enter the language or 'exit' to quit: ")
        if language == 'exit':
            print("Exiting...")
            exit()
        if language == 'python':
            with open('../router/example.py', 'r') as file:
                python_code = file.read()
            submit_code('python', python_code)
            execute_code('python')
        elif language == 'java':
            with open('../router/example.java', 'r') as file:
                java_code = file.read()
            submit_code('java', java_code)
            execute_code('java')
        elif language == 'dart':
            with open('../router/example.dart', 'r') as file:
                dart_code = file.read()
            submit_code('dart', dart_code)
            execute_code('dart')
        else:   
            print("Unsupported language")  


def main():
    print_landing_message()
    user_input()
        
    


if __name__ == "__main__":
    main()
