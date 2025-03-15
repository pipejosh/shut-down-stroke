import os
import platform
import getWords

def main():
    operatingSystem = platform.system()
    wordBank = getWords.getWords();
    print(wordBank)


def shutDownMac():
    # os.system('shutdown -h now') #shuts down mac
    print('test')

def shutDownWindows():
    # os.system('cmd /k "shutdown /s /t 2"') # shuts down the computer 
    print('test')


if __name__ == "__main__":
    main()