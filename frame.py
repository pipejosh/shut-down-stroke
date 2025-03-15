import tkinter as tk
import getWords as words 

frame = tk.Tk()
entry = tk.Entry(frame)

wordBank = words.getWords()
inputBox = None
historyLabel = None
wordsCounter = 0

def onSpace(event):
    global wordsCounter

    if hasWon(): 
        return

    userWord = entry.get()
    if userWord.strip(): 
        inputBox.config(text=f"Submitted: {userWord}") 
        entry.delete(0, tk.END) 

    checkWord(userWord.strip())

    if wordsCounter + 1 < len(wordBank): 
        historyLabel.config(text=wordBank[wordsCounter + 1])

    wordsCounter += 1 
    print(wordsCounter)

def initFrame():
    global inputBox, historyLabel, wordsCounter
    frame.title("Typing Game")
    frame.geometry("500x500")

    label = tk.Label(frame, text="Welcome to the Typing Game!", font=("Arial", 24))
    label.pack()

    inputBox = tk.Label(frame, text="", font=("Arial", 16))
    inputBox.pack(pady=20)

    historyLabel = tk.Label(frame, text="Current Word:", font=("Arial", 14))
    historyLabel.pack(pady=10)
    historyLabel.config(text=wordBank[wordsCounter]) 

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
    global wordsCounter

    return userWord == wordBank[wordsCounter]

def main():
    print(wordBank) 
    initFrame()

main()
