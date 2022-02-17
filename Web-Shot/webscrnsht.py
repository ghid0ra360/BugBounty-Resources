import sys
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PIL import Image
from urllib.parse import urlparse
import pyfiglet
from termcolor import colored

# Banner
def title():
    banner = pyfiglet.figlet_format("WEB-SHOT", justify="center")
    print(colored(banner, "blue"))
    print("\t\t\t\t\t\tA Website Screenshot tool \n\t\t\t\t\t\t\t\t\t\t\t\t\t-By Aneesh")
    a = 1
    while a <=70:
        print('*', end = ' ')
        a+=1

def web_shot():
    title()

    # Disclaimer
    print("\n\n## DISCLAIMER ## \n\nPlease download chromedriver and give its full path when asked. This program needs chromedriver for it to properly function. \nChromedriver can be downloaded from https://chromedriver.chromium.org/downloads")

    print("\n")
    a = 1
    while a <=70:
        print('*', end = ' ')
        a+=1
    print("\n")

    try:
        # Specify path to chromedriver installed on users computer
        path_to_driver = input("\nEnter path to chromedriver : ")

        # Making chrome run headless
        options = Options()
        options.headless = True

        # Asking for the url to ss
        url = input("Enter the website : ")
        path_to_save = input("Full path to save : ")
        ss_name = input("Name of the screenshot : ")

        # Checking if the inputted url contain scheme or not
        if urlparse(url).scheme == 'https' or urlparse(url).scheme == 'http':
            pass
        else:
            url = "https://" +url

        # specifying chrome driver
        s=Service(path_to_driver)
        driver = webdriver.Chrome(service=s , options=options)

        # Visiting the url
        driver.get(url)

        # saving the ss
        org_path = path_to_save + '/' + ss_name + ".png"
        driver.save_screenshot(org_path)

        #opening the ss
        def op_sc():
            op = input("Do you want to open the taken screenshot (Y/N) ? : ")

            if re.match("^[yY]*$", op):
                screenshot = Image.open(org_path)
                screenshot.show()
            elif re.match("^[nN]*$", op):
                print("Exiting...")
            else:
                print("Please give a correct response")
                sleep(2)
                op_sc()
        op_sc()
        def options_a():
            print("\n(A) Go back to c-tool \n(B) Exit")
            o = input("\nPlease choose any of the following options: ")

            if re.match("^[Aa]*$", o):
                sleep(2)
                print("Entering C-tool")
                sleep(2)
                ctool()
            elif re.match("^[bB]*$", o):
                print("Exiting the tool..")
                sleep(2)
                sys.exit()
            else:
                print("Please give options correctly")
                sleep(2)
                options_a()
        options_a()

    except Exception as ex:
        print(ex , '\n' "Please try again\nProgram Restarting...\n")

        sleep(3)





web_shot()