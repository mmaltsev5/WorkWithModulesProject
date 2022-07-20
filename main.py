import os
import time

while True:
    site = input('Vvedite adress sayta>>\n')
    if site == '':
        break

    if "https://" in site:
        print('if')
        time.sleep(3)
        os.system('start ' + site)
    elif "www." in site:
        print('elif')
        time.sleep(3)
        site = "https://" + site
        os.system('start ' + site)
    else:
        print('else')
        time.sleep(3)
        site = "https://www." + site
        os.system('start ' + site)