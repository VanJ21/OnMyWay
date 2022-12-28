import pywhatkit

try:
    phoneNum = input("What is the phone number you wish to send it a message to? ")
    pywhatkit.sendwhatmsg_instantly(
        phone_no=f'<{phoneNum}>', 
        message="Howdy! This is a test message!",
        tab_close=True
    )
    print("Message sent!")
except Exception as e: 
    print("Sorry, something went wrong, try again!")
