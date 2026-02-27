from pathlib import Path
from selenium import webdriver
import os, shelve, shutil, time, webbrowser, requests, send2trash
driver = webdriver.Firefox()
print(rf'write number.number to start.(eg:1.1 and 2.1)')
#def------------------------------------------------------------------------------------------------------------------------------1.1
def _1_1():
    print('')
    print('----------------------------------------------------------------------')
    while True:
        print('In which folder do you want to create your new file?')
        old_dir=os.getcwd()
        create_in=input('---->')
        try:
            if os.path.exists(create_in):
                os.chdir(create_in)
                while True:
                    print('type the name of your file that you want to create[the only type allowed is .txt][if not, say:quit]')
                    new_file=input('---->')
                    if new_file.lower()=='quit':
                        break
                    p=Path(new_file)
                    if p.suffix in ['.txt']:
                        _=open(new_file, 'w')
                        _.close()
                        print('saved correctly-------------------------')
                        break
                    else:
                        print('bad input.----try again.')
                if p.suffix in ['.txt']:
                    break
            else:
                print('Invalid input')
        except PermissionError:
            print('invalid folder name.')
            print(r'The folder name must be upper than:"C:\Users\[your user name}"')
            print('Try again--------------------------')
    os.chdir(old_dir)
#def-----------------------------------------------------------------------------------------------------------------------------1.2
def _1_2():
    print('')
    print('----------------------------------------------------------------------')
    while True:
        print('which file do you want to edit?')
        editfile=input('file>')
        if os.path.exists(editfile):
            if Path(editfile).suffix in ['.txt']:
                with open(editfile, 'a') as _:
                    print('Start typing---to stop, write:"1234567890stop"')
                    while True:
                        _1=input('>')
                        if _1.lower() == "1234567890stop":
                            break
                        else:
                            _.write(_1 + '\n')
                    print('edit successfully')
                    break
            else:
                print('it only supports .txt files!')
        else:
            print('invalid input')
            time.sleep(0.5)#avoid bug
#def-----------------------------------------------------------------------------------------------------------------------------1.3
def _1_3():
    print('')
    print('----------------------------------------------------------------------')
    print('can you tell me the file that you want to delete?')
    print('________IMPORTANT INFORMATION!____________')
    print('YOU CAN NOT GET IT BACK!')
    delete=input('input the file>')
    try:
        if os.path.exists(delete):
            print('Are you sure?')
            ans=input('yes/no')
            if ans == 'yes':
                print('	Deleting....................')
                for _ in range(4,0,-1):
                    print(str(_) + '...........')
                    time.sleep(1)
                print('deleted')
                if os.path.isfile(delete):
                    os.remove(delete)
                if os.path.isdir(delete):
                    shutil.rmtree(delete)
            else:
                print('all right!')
    except PermissionError:
        print('invalid input.')
#def------------------------------------------------------------------------------------------------------------------------------2.1
def _2_1():
    global driver
    try:
        openweb=input('tell me the web that you want to open')
        driver.get(openweb)
    except Exception:
        print("Invalid web. Try including https://")
#def------------------------------------------------------------------------------------------------------------------------------2.2
def _2_2():
    global driver
    print('Enter the website you want to open')
    print('''web allowed:
google
bing
duckduckgo
firefox''')
    searchengine = input('>').lower()
    engines = {"google": "https://www.google.com", "bing": "https://www.bing.com", "duckduckgo": "https://duckduckgo.com", "firefox": "https://www.firefox.com"}
    if searchengine in engines:
        driver.get(engines[searchengine])
    else:
        print(r"Unexpected/Unknown search engine")
#def------------------------------------------------------------------------------------------------------------------------------3.1
def _3_1():
    global driver
    if driveralive():
        place = input('input the place you want to search')
        driver.get(f"https://www.google.com/maps/search/{place}")
    else:
        print('Chrome was closed!')
        driver = webdriver.Firefox()
        place = input('input the place you want to search')
        driver.get(f"https://www.google.com/maps/search/{place}")
#def------------------------------------------------------------------------------------------------------------------------------3.2
def _3_2():
    global driver
    if driveralive():
        city = input("input the place where you want to know its weather：")
        try:
            result = requests.get(f'https://wttr.in/{city}?format=4', timeout = 5)
            print(result.text)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            print('Search time out, the net work may be disconnected or too slow.')
    else:
        print('Chrome was closed!')
        driver = webdriver.Firefox()
        city = input("input the place where you want to know its weather：")
        try:
            result = requests.get(f'https://wttr.in/{city}?format=4', timeout = 5)
            print(result.text)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            print('Search time out, the net work may be disconnected or too slow.')
#def------------------------------------------------------------------------------------------------------------------------------3.2


#don't check this
#unfinished



#def _3_3():
#    print('this part may take some times')
#    driver.get("https://www.bing.com/chat")



#def----------------------------------------------------------------------------------------------------------------------driver alive
def driveralive():
    try:
        global driver
        _ = driver.title
        return True
    except:
        return False
#running part------------------------------------------------------------------------------------------------------------running part
while True:
    print("""-------------------------------------files-------------------------------------
1.1-create a text file.
1.2-edit a file that exist in your computer.
1.3-delete a file(you can't get it back).
--------------------------------------web--------------------------------------
2.1-open a web.
2.2-change search engine.
--------------------------------web you may use--------------------------------
3.1-google map.
3.2-weather
#3.3-access ai
""")
    anss = input('input the task number>')
    if anss == '1.1':
        _1_1()
    elif anss == '1.2':
        _1_2()
    elif anss == '1.3':
        _1_3()
    elif anss == '2.1':
        _2_1()
    elif anss == '2.2':
        _2_2()
    elif anss == '3.1':
        _3_1()
    elif anss == '3.2':
        _3_2()
    else:
        print('invalid')
driver.quit()
