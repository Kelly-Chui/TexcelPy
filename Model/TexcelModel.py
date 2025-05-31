import os
import re
from datetime import datetime
from tkinter import messagebox
import pandas as pd
from Model import TexcelConfig

class TexcelModel:
    def __init__(self):
        self.config = TexcelConfig.Config()
        self.save_path = self.config.save_path
        self.load_path = self.config.load_path

    def set_last_paths(self, save_path, load_path):
        self.config.save_last_values(save_path, load_path)

    def _structured_key(self, filename):
        parts = filename.split('_')
        key = []
        for part in parts:
            if part.isdigit():
                key.append(int(part))
            else:
                nums = re.findall(r'\d+', part)
                key.extend(int(n) for n in nums)
        return key

    def _extract_number(self, value):
        if isinstance(value, str) and "=" in value:
            try:
                return float(value.split('=')[1])
            except ValueError:
                return "failed"
        return "failed"

    def make_excel_file(self):
        if not self.load_path or not self.save_path:
            messagebox.showwarning("Notice", "No valid directory has been selected. Please reselect")
            return

        txt_files = sorted(
            [f for f in os.listdir(self.load_path) if f.endswith(".txt")],
            key=self._structured_key
        )

        df_list = []
        for file in txt_files:
            with open(os.path.join(self.load_path, file), 'r') as txt_file:
                df = pd.read_csv(txt_file, header=None, names=None)
                df_list.append(df)

        if not df_list:
            messagebox.showwarning("Notice", "No .txt files found in the load path.")
            return

        result_df = pd.concat(df_list, axis=1)
        result_df = result_df.map(self._extract_number)

        now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        filename = f"result_{now}.xlsx"
        result_path = os.path.join(self.save_path, filename)

        with pd.ExcelWriter(result_path, engine="openpyxl") as writer:
            result_df.to_excel(writer, index=False, header=False)

        messagebox.showinfo("Complete", f"Saved to {result_path}")
