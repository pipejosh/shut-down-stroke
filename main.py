import getWords as words
import tkinter as tk
import platform
import serial
import time
import os

arduino = serial.Serial("COM8", 9600)  

time.sleep(2)  

frame = tk.Tk()
entry = tk.Entry(frame)

operativeSystem = platform.system()
wordBank = words.getWords()
inputBox = None
historyLabel = None
livesLeftLabel = None
wordsCounter = 0
livesLeft = 3

def onSpace(event):
    global wordsCounter

    if hasWon():
        return

    userWord = entry.get().strip()

    if checkWord(userWord):
        inputBox.config(text=f'Submitted: {userWord}', foreground='green')
    else:
        inputBox.config(text=f'Submitted: {userWord} WRONG', foreground='red')
        loseLife()

    entry.delete(0, tk.END)

    if wordsCounter + 1 < len(wordBank):
        historyLabel.config(text=wordBank[wordsCounter + 1])

    wordsCounter += 1

def initFrame():
    global inputBox, historyLabel, livesLeftLabel
    frame.title("Typing Game")
    frame.geometry("500x500")

    livesLeftLabel = tk.Label(frame, text=f"Lives Left: {livesLeft}", font=("Arial", 14))
    livesLeftLabel.pack(pady=10)

    label = tk.Label(frame, text="Welcome to the Typing Game!", font=("Arial", 24))
    label.pack(pady=20)

    inputBox = tk.Label(frame, text="", font=("Arial", 16))
    inputBox.pack(pady=20)

    historyLabel = tk.Label(frame, text="Current Word:", font=("Arial", 20))
    historyLabel.pack(pady=20)
    historyLabel.config(text=wordBank[wordsCounter])

    # Input Box
    initInput()

    frame.mainloop()

def initInput():
    entry.pack(pady=10)
    entry.bind("<space>", onSpace)
    entry.focus_set()

def hasWon():
    global wordsCounter
    if wordsCounter >= len(wordBank):
        print("You have won!")
        return True
    return False

def checkWord(userWord):
    return userWord == wordBank[wordsCounter]

def loseLife():
    global livesLeft

    if livesLeft > 0:
        livesLeft -= 1
        setLivesLeft()

        arduino.write(b'L')  
        time.sleep(0.5)

    if livesLeft == 0:
        arduino.close()
        shutdown()

def setLivesLeft():
    global livesLeftLabel
    livesLeftLabel.config(text=f"Lives Left: {livesLeft}")

def shutdown():
    global operativeSystem
    print("Game Over! Shutting down...")

    match operativeSystem:
        case "Windows":
            os.system("shutdown /s /t 1")
        case "Darwin":
            os.system("shutdown -h now")
        case "Linux":
            os.system("shutdown -h now")

    frame.destory()

def main():
    print(wordBank)
    initFrame()

if __name__ == "__main__":
    main()