import urllib.request

def read_text():
    content = str(input("Enter your text to check please: "))
    check_profanity(content)
    
def check_profanity(text_to):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+text_to)
    output = str(connection.read())
    connection.close()

    if "true" in output:
        print("Have profanity text inside")
    elif "false" in output:
        print("No profanity text inside")
    else:
        print("Error")

read_text()
