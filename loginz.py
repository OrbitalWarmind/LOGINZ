import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

print("""
  ░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░    ░▒▓██▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██▓▒░    
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██▓▒░      
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                                        
                                                                                  
""")

# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def check_login_fields(url):
    try:
        # Check if the URL has HTTP or HTTPS scheme, if not, prepend "http://"
        if not urlparse(url).scheme:
            url = "http://" + url

        # Define custom User-Agent header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

        # Send a GET request to the website with custom User-Agent header
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses (e.g., 404, 500)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all input fields in the login section
        login_inputs = soup.select('form input[type="text"], form input[type="password"], form input[type="email"], form input[type="tel"], form input[type="number"], form input[type="username"]')

        if login_inputs:
            print(GREEN + "Input fields found in the login section with the following HTML code:" + RESET)
            for field in login_inputs:
                print("\n" + GREEN + "Field type: " + RESET + field['type'])
                print(GREEN + "Field name: " + RESET + field.get('name', ''))
                print(GREEN + "Field ID: " + RESET + field.get('id', ''))
                print(GREEN + "Field HTML code: " + RESET)
                print(field)
        else:
            print(RED + "No input fields found in the login section." + RESET)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Main loop
while True:
    # Get website URL from user input
    url = input("\nEnter the website URL (type 'exit' to quit): ")
    if url.lower() == 'exit':
        break
    else:
        check_login_fields(url)
