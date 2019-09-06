import tkinter as tk
from src.predictor import Predictor
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *


class Application(tk.Frame):

    def __init__(self, master=None, width=800, height=800, bg='#212429'):
        super().__init__(master)
        self.master = master

        self.master.minsize(width, height)
        self.pack(fill='both', expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.filepicker_btn = tk.Button(self,
                                        text="Get path",
                                        command=self.__load_file)

        self.filepath = tk.StringVar()
        self.target_i = tk.StringVar()
        self.header = tk.StringVar()
        self.index_col = tk.StringVar()

        self.l_target_i = tk.Label(self, text="Target column (number):")
        self.l_header = tk.Label(self, text="Header rows (i.e. 0,2,4):")
        self.l_index_col = tk.Label(self, text="Index columns (i.e. 0,2,4):")

        self.e_filepath = tk.Entry(self, textvariable=self.filepath, state=tk.DISABLED)
        self.e_target_i = tk.Entry(self, textvariable=self.target_i)
        self.e_header = tk.Entry(self, textvariable=self.header)
        self.e_index_col = tk.Entry(self, textvariable=self.index_col)

        self.process_btn = tk.Button(self, text="Predict", command=self.__process)

        self.filepicker_btn.grid(row=0, column=0, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.e_filepath.grid(row=0, column=1, pady=5)
        self.l_target_i.grid(row=1, column=0)
        self.e_target_i.grid(row=1, column=1, pady=5)
        self.l_header.grid(row=2, column=0)
        self.e_header.grid(row=2, column=1, pady=5)
        self.l_index_col.grid(row=3, column=0)
        self.e_index_col.grid(row=3, column=1, pady=5)
        self.process_btn.grid(row=4, column=0, columnspan=2, ipadx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)

    def __load_file(self):
        self.filepath.set(askopenfilename(title='Choose a dataset'))

    def __process(self, *args):
        filepath = self.filepath.get()
        if not len(filepath):
            showwarning("", "Path is empty. Please, click on 'Get Path' and select a dataset.")
            return

        try:
            target_i = int(self.target_i.get())
        except ValueError:
            showwarning("", "Your target column must be an integer.")
            return

        try:
            header = self.header.get()
            if not len(header):
                header = None
            else:
                header = [int(row) for row in header.split(',')]
        except ValueError:
            showwarning("", "Your header row(s) must be an integer or a list of integers separated by comma.")
            return

        try:
            index_col = self.index_col.get()
            if not len(index_col):
                index_col = None
            else:
                index_col = [int(col) for col in index_col.split(',')]
        except ValueError:
            showwarning("", "Your index column(s) must be an integer or a list of integers separated by comma.")
            return

        predictor = Predictor(filepath, target_i, header, index_col)

        text = tk.Text()
        text.pack(side='top')

        text.insert(tk.INSERT, predictor.extract())
        text.insert(tk.END, predictor.predict())

