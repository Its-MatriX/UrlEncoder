# Generates encoded webpage open script

from random import choice
from base64 import b64encode
from string import ascii_letters
from colorama import Fore
from os.path import split
from os import system, listdir, rename, remove
from shutil import rmtree
from sys import executable

fg = Fore.GREEN
fc = Fore.CYAN
fy = Fore.YELLOW
fw = Fore.WHITE
fr = Fore.RED

url = input(f'{fc}Enter a string: {fy}')

if url == '':
    print(f'{fr}String cannot be empty{fw}')
    exit(1)

src = '''from base64 import b64decode
def d(s):
    return b64decode(s+"==")
'''
vals = []
used = []

for i in url:
    while True:
        c = ''.join([choice(ascii_letters) for x in range(10)])

        if c not in used:
            used.append(c)
            break

    n = b64encode(i.encode('utf-8')).decode('utf-8').replace('==', '')
    src += c + f'="{n}"\n'
    vals.append(c)

builder_src = f'url=(\n'

for i in vals:
    builder_src += f'    d({i})+\n'

src += builder_src[:-2:1] + ('\n).decode("utf-8")\n' +
                             'from webbrowser import open_new_tab\n' +
                             'open_new_tab(url)')

path = split(__file__)[0].replace('\\', '/') + '/__webopen.py'
file = open(path, 'w')
file.write(src)
file.close()

try:
    rmtree(split(__file__)[0].replace('\\', '/') + '/__pycache__')

except:
    pass

system(f'{executable} -m py_compile {path}')

cache = listdir(split(__file__)[0].replace('\\', '/') + '/__pycache__')
cached_file = split(__file__)[0].replace('\\',
                                         '/') + '/__pycache__/' + cache[0]

rename(cached_file, split(__file__)[0].replace('\\', '/') + '/urlopen.py')

try:
    rmtree(split(__file__)[0].replace('\\', '/') + '/__pycache__')

except:
    pass

remove(path)

print(fw)