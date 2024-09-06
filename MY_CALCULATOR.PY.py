import tkinter as tk



# C FUNCTION TO DELETE ONE VALUE
def cfunction():
    if editor.get("1.0", tk.END).strip():
        editor.delete("end - 2c", "end - 1c")


# AC FUNCTION TO CLEAR ALL
def all_clear():
    editor.delete(1.0, tk.END)


# FUNCTION TO EVALUATE INSERT EDIT
def bottonclick(value):
    if value == "=":
        try:
            result = eval(editor.get("1.0", tk.END).strip())

            editor.delete(1.0, tk.END)
            editor.insert(tk.END, str(result))

        except Exception as e:
            editor.delete(1.0, tk.END)

            editor.insert(tk.END, "Error")
    else:
        editor.insert(tk.END, value)


app = tk.Tk()
app.title(" VICENTIA CALCULATOR")
app.geometry("700x600+200+150")
app.resizable(width=True, height=True)
frame = tk.Frame(app, padx=25, pady=25, bg="blue")
frame.pack(side="top", fill="both", expand=True)

# EDITOR
editor = tk.Text(frame, fg="blue", font=("Times New Roman", 12), height=12)
editor.pack(side="top", fill="both", expand=True)

# BUTTON FRAME
bf = tk.Frame(frame)
bf.pack(side="top", fill="both", expand=True)

# VARIOUS BUTTONS AND THEIR PLACE BUTTON
bt1 = tk.Button(bf, text="C", background="yellow", fg="black", font=("times new roman", 15), width=15, height=2,
                command=cfunction)
bt1.grid(row=0, column=0)

bt2 = tk.Button(bf, text="AC", background="yellow", fg="black", font=("times new roman", 15), width=15, height=2,
                command=all_clear)
bt2.grid(row=0, column=1)

bt3 = tk.Button(bf, text="(", background="black", fg="white", font=("times new roman", 15), width=15, height=2,
                command=lambda: bottonclick("("))
bt3.grid(row=0, column=2)

bt4 = tk.Button(bf, text=")", background="black", fg="white", font=("times new roman", 15), width=15, height=2,
                command=lambda: bottonclick(")"))
bt4.grid(row=0, column=3)

bt5 = tk.Button(bf, text="1", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                command=lambda: bottonclick("1"))
bt5.grid(row=1, column=0)

bt6 = tk.Button(bf, text="2", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                command=lambda: bottonclick("2"))
bt6.grid(row=1, column=1)

bt7 = tk.Button(bf, text="3", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                command=lambda: bottonclick("3"))
bt7.grid(row=1, column=2)

bt8 = tk.Button(bf, text="+", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                command=lambda: bottonclick("+"))
bt8.grid(row=1, column=3)

bt9 = tk.Button(bf, text="4", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                command=lambda: bottonclick("4"))
bt9.grid(row=2, column=0)

bt10 = tk.Button(bf, text="5", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("5"))
bt10.grid(row=2, column=1)

bt11 = tk.Button(bf, text="6", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("6"))
bt11.grid(row=2, column=2)

bt12 = tk.Button(bf, text="-", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("-"))
bt12.grid(row=2, column=3)

bt13 = tk.Button(bf, text="7", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("7"))
bt13.grid(row=3, column=0)

bt14 = tk.Button(bf, text="8", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("8"))
bt14.grid(row=3, column=1)

bt15 = tk.Button(bf, text="9", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("9"))
bt15.grid(row=3, column=2)

bt16 = tk.Button(bf, text="*", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("*"))
bt16.grid(row=3, column=3)

bt17 = tk.Button(bf, text=".", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("."))
bt17.grid(row=4, column=0)

bt18 = tk.Button(bf, text="0", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("0"))
bt18.grid(row=4, column=1)

bt19 = tk.Button(bf, text="/", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("/"))
bt19.grid(row=4, column=2)

bt20 = tk.Button(bf, text="=", background="white", fg="black", font=("times new roman", 15), width=15, height=2,
                 command=lambda: bottonclick("="))
bt20.grid(row=4, column=3)

app.mainloop()