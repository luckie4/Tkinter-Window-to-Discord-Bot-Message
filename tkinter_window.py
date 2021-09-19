import tkinter as tk

# Tkinter Window
root = tk.Tk()
root.title("Discord message caller")
root.geometry("600x600")
frame = tk.Frame(root)
frame.pack()

# Run the bot script
def run():
    root.destroy() # Destroys the window, otherwise it will crash
    import discord_bot # Imports the Bot
    print("Completed, exiting.")

# Packing the Button
button = tk.Button(frame, width=500, height=500, text="Send Message", fg="darkblue", command=run)
button.pack(side=tk.LEFT)

# Running the window
root.mainloop()
