# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import webbrowser
from time import sleep


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def rand_web():
    website_list = ["https://drive.google.com/drive/folders/1WkGIK8KJ3KsaOAEafLBbxEkde6G2hhDM",
                    "https://www.pythonforbeginners.com/",
                    "https://www.kickstarter.com/",
                    "https://www.crowdfunding.com/",
                    "https://www.freecodecamp.org/",
                    "https://www.w3resource.com/"]
    chosen = random.choice(website_list)
    print("The chosen site is:", chosen)
    sleep(2)
    webbrowser.open(chosen)


rand_web()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
