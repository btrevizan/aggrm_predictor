from tkinter.filedialog import askopenfilename
from src.utils import human_readable_methods
from src.predictor import Predictor
from tkinter.messagebox import *
import tkinter.font as tkFont
import tkinter as tk


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

        self.title_font = tkFont.Font(family='helvetica', size=18, weight='bold')

        chars_title = tk.Label(self, font=self.title_font, text="Dataset's characteristics")
        ranking_title = tk.Label(self, font=self.title_font, text="Recommended methods", width=45)

        self.filepicker_btn.grid(row=0, column=0, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.e_filepath.grid(row=0, column=1, pady=5)
        self.l_target_i.grid(row=1, column=0)
        self.e_target_i.grid(row=1, column=1, pady=5)
        self.l_header.grid(row=2, column=0)
        self.e_header.grid(row=2, column=1, pady=5)
        self.l_index_col.grid(row=3, column=0)
        self.e_index_col.grid(row=3, column=1, pady=5)
        self.process_btn.grid(row=4, column=0, columnspan=2, ipadx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)

        chars_title.grid(row=5, column=0, columnspan=2, pady=10)
        ranking_title.grid(row=0, column=2)

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

        dt_name_lb = tk.Label(self, text="Dataset")
        dt_value_lb = tk.Label(self, text=filepath.split('/')[-1])

        dt_name_lb.grid(row=6, column=0, padx=10, sticky=tk.W)
        dt_value_lb.grid(row=6, column=1, sticky=tk.E)

        chars = predictor.extract()
        for i, char_info in enumerate(chars.items()):
            char_name, char_value = char_info

            char_name_lb = tk.Label(self, text=char_name)
            char_value_lb = tk.Label(self, text=round(char_value, 3))

            char_name_lb.grid(row=7+i, column=0, padx=10, sticky=tk.W)
            char_value_lb.grid(row=7+i, column=1, sticky=tk.E)

        ranking = predictor.predict()

        bold_font = tkFont.Font(family='helvetica', size=14, weight='bold')
        normal_font = tkFont.Font(family='helvetica', size=12, weight='normal')

        lf = tk.LabelFrame(self, bd=0)
        lf.grid(row=1, column=2, rowspan=40)

        readable = human_readable_methods()

        position = tk.Label(lf, text='#')
        method_lb = tk.Label(lf, text='Aggregation Method')
        f1_lb = tk.Label(lf, text='Mean F1-Score')

        position.grid(row=0, column=0, ipadx=30, sticky=tk.W, pady=10)
        method_lb.grid(row=0, column=1, sticky=tk.W, pady=10)
        f1_lb.grid(row=0, column=2, sticky=tk.E, pady=10)

        for i, rank_info in enumerate(ranking[:25]):
            method, f1 = rank_info

            p = i + 1
            font = bold_font if i <= 10 else 'default'

            position = tk.Label(lf, text=str(p) + '.')
            method_lb = tk.Label(lf, text=readable[method], font=font)
            f1_lb = tk.Label(lf, text=round(f1, 2))

            position.grid(row=i+1, column=0, ipadx=30, sticky=tk.W)
            method_lb.grid(row=i+1, column=1, sticky=tk.W)
            f1_lb.grid(row=i+1, column=2, sticky=tk.E)
