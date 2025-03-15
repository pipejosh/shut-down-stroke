import tkinter as tk
import getWords as words

frame = tk.Tk()
entry = tk.Entry(frame)

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

    userWord = entry.get()

    if checkWord(userWord.strip()):
        inputBox.config(text=f'Submitted: {userWord}', foreground='green')
        entry.delete(0, tk.END)
    else:
        inputBox.config(text=f'Submitted: {userWord} WRONG', foreground='red')
        entry.delete(0, tk.END)

    if wordsCounter + 1 < len(wordBank):
        historyLabel.config(text=wordBank[wordsCounter + 1])

    wordsCounter += 1
    print(wordsCounter)

def initFrame():
    global inputBox, historyLabel, wordsCounter, livesLeftLabel, livesLeft
    frame.title("Typing Game")
    frame.geometry("500x500")

    livesLeftLabel = tk.Label(frame, text=f"Lives Left: {livesLeft}", font=("Arial", 14))
    livesLeftLabel.place(x=15, y=20, anchor="nw")  # Position at the top left
    livesLeftLabel.pad = 10

    label = tk.Label(frame, text="Welcome to the Typing Game!", font=("Arial", 24))
    label.pack(pady=20)

    inputBox = tk.Label(frame, text="", font=("Arial", 16))
    inputBox.pack(pady=30)

    historyLabel = tk.Label(frame, text="Current Word:", font=("Arial", 20))
    historyLabel.pack(pady=30)
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
    global wordsCounter, livesLeft

    if livesLeft == 0:
        print("You have lost!")
        frame.destroy()
        return False

    if userWord == wordBank[wordsCounter]:
        return True
    else:
        livesLeft -= 1
        setLivesLeft()
        return False

def setLivesLeft():
    global livesLeftLabel, livesLeft
    livesLeftLabel.config(text=f"Lives Left: {livesLeft}")

def main():
    print(wordBank)
    initFrame()

main()
