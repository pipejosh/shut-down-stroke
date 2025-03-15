import tkinter as tk
import getWords as words

entry = tk.Entry()
frame = tk.Tk()

wordBank = words.getWords()
inputBox = None


def on_space(event):
    word = entry.get()  # Get text from input field
    if word.strip():  # Only submit if it's not empty
        inputBox.config(text=f"Submitted: {word}")  # Update label with submitted word
        entry.delete(0, tk.END)  # Clear input field

def initFrame():
    frame.title("My Frame")
    frame.geometry("500x500")

    label = tk.Label(frame, text="Hello World", font=("Arial", 24))
    label.pack()

    # Create a label to display the submitted word
    inputBox = tk.Label(frame, text="", font=("Arial", 16))
    inputBox.pack(pady=20)

    initInput()

    frame.mainloop()

def initInput():
    entry.pack()
    entry.bind("<space>", on_space)  # Bind spacebar key to submit word
    entry.focus_set()  # Focus on entry widget so user can type immediately

initFrame()
