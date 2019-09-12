from gui.app import Application
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    app = Application(master=root, width=800, height=650)
    app.master.title("Aggregation Method Predictor")
    app.master.size()
    app.mainloop()
