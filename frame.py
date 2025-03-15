import tkinter as tk
import getWords as words 

entry = tk.Entry()
frame = tk.Tk()

wordBank = words.getWords() 
inputBox = None
historyLabel = None 
wordsCounter = 0    

def onSpace(event):

    if hasWon():
        return

    global wordsCounter
    currentWord = ""



    userWord = entry.get()
    if userWord.strip():  # If word is not empty
        inputBox.config(text=f"Submitted: {userWord}")  # Update label with submitted word
        entry.delete(0, tk.END)  # Clear the entry field

    checkWord(userWord.strip())

    historyLabel.config(text=wordBank[wordsCounter + 1]) 
    wordsCounter += 1
    print(wordsCounter)
    

# Initialize the main frame
def initFrame():
    global inputBox, historyLabel
    frame.title("My Frame")
    frame.geometry("500x500")

    # Create and pack the label that initially displays "Hello World"
    label = tk.Label(frame, text="Hello World", font=("Arial", 24))
    label.pack()

    # Create a label that will display the submitted word
    inputBox = tk.Label(frame, text="", font=("Arial", 16))
    inputBox.pack(pady=20)

    # Create a label to display the history of submitted words
    historyLabel = tk.Label(frame, text="Submitted Words History:", font=("Arial", 14))
    historyLabel.pack(pady=10)

    # Initialize input box (entry widget)
    initInput()

    frame.mainloop()

# Function to set the label text for the word from the word bank
def setLabelText(newText):
    historyLabel.config(text=newText)

# Initialize the entry widget and bind spacebar event
def initInput():
    entry.pack()
    entry.bind("<space>", onSpace)  # Bind spacebar key to submit word
    entry.focus_set()  # Set focus to entry field so user can type immediately

def hasWon():
    global wordsCounter
    if wordsCounter >= len(wordBank):
        print("You have won!")
        return True

def checkWord(userWord):
    print("IS CHECHING")
    global wordsCounter

    if userWord == wordBank[wordsCounter]:
        print("Correct")
    print("AFTER CHECHING")
    print (wordBank[wordsCounter])

def main():
    print(wordBank)  # Print the word bank
    initFrame()
main()
