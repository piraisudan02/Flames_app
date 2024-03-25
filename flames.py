import tkinter as tk
from tkinter import messagebox

def calculate_relationship():
    s1 = entry_male_name.get().lower()
    s2 = entry_second_name.get().lower()
    if s1==s2=='':
        messagebox.showerror("Oops...","Enter both names.")
        return
    if s1==s2:
        messagebox.showerror("Oops...","No same names are allowed...")
        return
    if s1=='':
        messagebox.showerror("Oops...","Enter Male name")
        return
    if s2=='':
        messagebox.showerror("Oops...","Enter Female name")
        return
    n = [0] * 26
    for i in range(len(s1)):
        if 'a' <= s1[i] <= 'z':
            n[ord(s1[i]) - 97] += 1
    for i in range(len(s2)):
        if 'a' <= s2[i] <= 'z':
            n[ord(s2[i]) - 97] -= 1

    num = 0
    for i in range(26):
        num += abs(n[i])

    relationships = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Sister']
    c = 1
    for i in range(5):
        counter = 1
        while True:
            if counter == num:
                relationships.remove(relationships[c - 1])
                break
            if c >= len(relationships):
                c = c - len(relationships)
            c += 1
            counter += 1

    messagebox.showinfo("Relationship Prediction", relationships[0])

root = tk.Tk()
root.title("Relationship Predictor")
root.configure(background='pink')

bold_font = ('Helvetica', 15, 'bold')
label_male_name = tk.Label(root, text="Enter the Male name:", bg="pink", font=bold_font)
label_second_name = tk.Label(root, text="Enter the Female name:", bg="pink", font=bold_font)
entry_male_name = tk.Entry(root, bg="white")
entry_second_name = tk.Entry(root, bg="white")

label_male_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
label_second_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_male_name.grid(row=0, column=1, padx=10, pady=5)
entry_second_name.grid(row=1, column=1, padx=10, pady=5)

def on_enter(event):
    calculate_button.config(bg="violet", fg="black")

def on_leave(event):
    calculate_button.config(bg="black", fg="violet")

calculate_button = tk.Button(root, text="Predict", command=calculate_relationship, bg="black", fg="violet", height=1, width=15)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)
calculate_button.bind("<Enter>", on_enter)
calculate_button.bind("<Leave>", on_leave)

# Set window size and make it non-resizable
root.geometry("400x150")
root.resizable(False, False)

root.mainloop()
