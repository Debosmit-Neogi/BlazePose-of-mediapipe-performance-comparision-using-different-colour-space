from tkinter import *

def login():
    username = entry_username.get()
    password = entry_password.get()

    # You can add your authentication logic here
    if username == "admin" and password == "password":
        label_result.config(text="Login successful!")
    else:
        label_result.config(text="Invalid username or password")

# Create the main window
root = Tk()
root.title("Login Page")

# Create username label and entry
label_username = Label(root, text="Username:")
label_username.pack()

entry_username = Entry(root)
entry_username.pack()

# Create password label and entry
label_password = Label(root, text="Password:")
label_password.pack()

entry_password = Entry(root, show="*")  # Show '*' for password input
entry_password.pack()

# Create login button
button_login = Button(root, text="Login", command=login)
button_login.pack()

# Display login result
label_result = Label(root, text="")
label_result.pack()

# Start the main loop
root.mainloop()
