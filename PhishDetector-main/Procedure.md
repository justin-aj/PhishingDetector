This guide is based on Ubuntu 20.04 OS and Python 3.8-3.9.

# GUI Based App:

    1. First create venv in python using 'python3 -m venv PhishDec'. ;; You can change PhishDec to your own name.  
    2. Change to virtual Environment "PhishDec" on linux.
    3. Install required libraries listed below.
    3. Run the "main.py" in 'src' directory from cmd or Terminal.
    3. Enter the url in Input and press Enter to for to check Phishing or legitimate.
    4. A Dialog with a message will be presented to the user.
    5. Along with dialog, the info about the url is also represented in a Table.


# Required libraries for usage are: 
    Sklearn, Numpy, bs4, xgboost, whois, ipaddress, lxml, urllib, urllib3, seaborn, requests, tornado, pandas and PyQt5.

# To use a Web Extension: 

1. Run the "Server.py" in terminal or command prompt.
2. Open Chrome, go to Extensions, select Developer mode and Select Load unpacked Extension.
3. You can now open the Extension in specific webpage and Click on "check this page" to check for phishing url.
4. A popup with message is showed to the user, confirming is the website legit or not.

Note:- Web Extension only provides information about, is the website Legit or Phishing, no additional inforamtion will be provided.



