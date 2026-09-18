import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import words

root = ctk.CTk()
word=words.get_word()

GREEN= "#6ca965"
YELLOW= "#c8b653"
GRAY= "#787c7f"
BLACK= "#000000"
WHITE= "#FFFFFF"

guessnum = 0

wordInput = ctk.CTkEntry(
    master=root,                            
    placeholder_text="Give word",      
    width=200,                             
    height=40,                             
    font=("Arial", 20),                    
    corner_radius=10                      
)

wordInput.grid(row=6, column=0, columnspan=5, pady=20) 

def getGuess(event=None):
    global word
    guess= wordInput.get()

    global guessnum
    

    if guessnum <=5:

        if len(guess) == 5:

            if word == guess: #swsth mantepsia
                msg=CTkMessagebox(title="YAY", message="You found it!", icon="check")
                msg.get()
                root.destroy()

            else: #lathos
                unmatched = []
                for i in range(5): #poia grammata DEN einai prasina
                    if guess[i] != word[i]:
                        unmatched.append(word[i])
                for i, letter in enumerate(guess):
            
                    label = ctk.CTkLabel(root, text=letter.upper(), width=40, height=40, corner_radius=5)
                    label.grid(row=guessnum, column=i, padx=10, pady=10)
                    
                    if letter == word[i]:
                        label.configure(fg_color=GREEN, text_color=BLACK)
                    elif letter in unmatched:
                        label.configure(fg_color=YELLOW, text_color=BLACK)
                        unmatched.remove(letter) #svhnw to gramma gia na mhn ginei ksana kitrino
                    else:
                        label.configure(fg_color=GRAY, text_color=WHITE)
                guessnum += 1
                wordInput.delete(0, 'end')
                if guessnum>=5:
                    msg=CTkMessagebox(title="Sorry", message= f"you lose :( the word was {word}", icon="cancel")  
                    msg.get()
                    root.destroy()
            
        else:
            CTkMessagebox(title="Error", message= "Please use 5 characters", icon="cancel")
   
                  


wordGuessButton= ctk.CTkButton(root, text="Guess", command=getGuess)
wordGuessButton.grid(row=999, column=3, columnspan=2)

root.bind('<Return>', getGuess)

root.mainloop()