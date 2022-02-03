"""
openPage() function:
    1. Open the web page
    2. Read the web page source code
buildDataForModual_one_two() function:
    1. Build the functionality for modual one and two

i variable: represent the index of the moduals, if i = 0, then the program will
stop

you can run any modual if the web page it alredy called and saved but if not, that
will call the openPage() first to open the web page and then the modual
functionality will be executed
"""
from urllib.request import urlopen
import re
import matplotlib.pyplot as plt
import pprint as pp

def openPage():
    global url
    url = None

    while url == None:
        url = input('Enter the url of the web page you want to read:\n')
        try:
            response = urlopen(url)
        except:
            print('Not vaild hyper link!')
            url = None
    global data
    data = response.read()
    data = data.decode()
def buildDataForModual_one_two():
    global lowerCase
    global upperCase
    global digits
    global href

    lowerCase, upperCase, digits, href = 0, 0, 0, data.count('href=')

    for el in data:
        if el in 'abcdefghijklmnopqrstyvwxyz':
            lowerCase += 1
        elif el in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            upperCase += 1
        elif el in '0123456789':
            digits += 1

i = None

while i == None:
    try:
        print('We have a list of moduals, enter any number between 1-6 to get result or enter 0 to exit from program')
        i = int(input('Modual = '))
    except ValueError:
        print('Not vaild number!')

while i != 0:
    if i == 1:
        try:
            url
        except:
            openPage()

        buildDataForModual_one_two()

        print(f'Lower case letters in the page {url} = {lowerCase}' )
        print(f'Upper case letters in the page {url} = {upperCase}' )
        print(f'Digits in the page {url} = {digits}' )
        print(f'The hyper linkes in the page {url} = {href}' )
            
    elif i == 2:
        try:
            url
        except:
            openPage()
            buildDataForModual_one_two()

        activities = ['Lower Case', 'Upper Case', 'Digits']
        slices = [lowerCase, upperCase, digits]
        colors = ['g', 'y', 'r']

        plt.pie(slices, labels = activities, colors = colors
                , startangle=90, shadow = True, explode = (0,0,0)
                , radius = 1.2, autopct = '%1.1f%%')
        plt.legend()
        plt.show()
    elif i == 3:
        try:
            url
        except:
            openPage()

        obj = {"URL's": None, "E-mails": None}
        obj["URL's"] = re.findall(
            r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'
            , data)
        obj["E-mails"] = re.findall('[\w\.-]+@[\w\.-]+', data)

        pp.pprint(obj)
    elif i == 4:
        try:
            url
        except:
            openPage()

        letters = {}
        for el in 'ABCDEFGHIJKLMNOPKRSTUVWXYZ':
            letters[el] = data.count(el) + data.count(el.lower())

        height = [letters[el] for el in 'ABCDEFGHIJKLMNOPKRSTUVWXYZ']
        names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'K', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        color = 'green'

        plt.bar(names, height, color = color)
        plt.xlabel('Letters')
        plt.ylabel('Count')
        plt.title('Count of letters in the page')
        plt.show()
    elif i == 5:
        try:
            url
        except:
            openPage()

        obj = {}
        letters = {}

        for el in 'ABCDEFGHIJKLMNOPKRSTUVWXYZ':
            letters[el] = data.count(el) + data.count(el.lower())
        for el in data:
            if el not in 'ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstyvwxyz':
                obj[el] = data.count(el)
        for el in letters.keys():
            obj[el] = letters[el]
        
        height = [el for el in obj.values()]
        names = [el for el in obj.keys()]
        color = 'green'

        plt.bar(names, height, color=color)
        plt.xlabel('characters')
        plt.ylabel('Count')
        plt.title('Count of characters in the page')
        plt.show()
    elif i == 6:
        try:
            url
        except:
            openPage()

        digits = {}
        for el in '0123456789':
            digits[el] = data.count(el)

        activities = [el for el in digits.keys()]
        occurences = [digits[el] for el in '0123456789']

        plt.pie(occurences, labels = activities, autopct = '%1.1f%%')
        plt.legend()
        plt.show()
    else:
        print('Not vaild number!')
    i = None
    while i == None:
        try:
            print('We have a list of moduals, enter any number between 1-6 to get result or enter 0 to exit from program')
            i = int(input('Modual = '))
        except ValueError:
            print('Not vaild number!')
