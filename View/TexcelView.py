import tkinter as tk
from tkinter import filedialog, ttk, messagebox

class TexcelView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # 콜백 핸들러
        self.on_select_load = None
        self.on_select_save = None
        self.on_run = None
        self.on_open_save = None

        # UI 컴포넌트 구성
        load_path_frame = ttk.Frame(self)
        save_path_frame = ttk.Frame(self)

        self.load_path_label = ttk.Label(load_path_frame, text="Select load path", width=40)
        self.save_path_label = ttk.Label(save_path_frame, text="Select save path", width=40)

        load_path_select_button = ttk.Button(load_path_frame, text="..", width=5, command=self._select_load_clicked)
        save_path_select_button = ttk.Button(save_path_frame, text="..", width=5, command=self._select_save_clicked)
        self.run_button = ttk.Button(self, text="Run", width=10, command=self._run_clicked)
        open_save_button = ttk.Button(self, text="open result folder", width=15, command=self._open_save_clicked)

        # 스타일
        style = ttk.Style()
        style.configure("runButton.TButton", foreground="green", focuscolor="none", padding=(0, 10))
        self.run_button.config(style="runButton.TButton")

        style.configure("pathLabel.TLabel", background="white", justify="center")
        self.load_path_label.config(style="pathLabel.TLabel")
        self.save_path_label.config(style="pathLabel.TLabel")

        # 배치
        load_path_frame.grid(row=0, column=0)
        save_path_frame.grid(row=1, column=0)

        self.run_button.grid(row=0, column=1)
        open_save_button.grid(row=1, column=1)

        self.load_path_label.grid(row=0, column=0, padx=5, pady=5)
        load_path_select_button.grid(row=0, column=1, padx=5, pady=5)
        self.save_path_label.grid(row=0, column=0, padx=5, pady=5)
        save_path_select_button.grid(row=0, column=1, padx=5, pady=5)

    # 이벤트 콜백 등록 메서드
    def set_on_select_load(self, callback): self.on_select_load = callback
    def set_on_select_save(self, callback): self.on_select_save = callback
    def set_on_run(self, callback): self.on_run = callback
    def set_on_open_save(self, callback): self.on_open_save = callback

    # 내부 버튼 이벤트 처리기
    def _select_load_clicked(self):
        if self.on_select_load:
            self.on_select_load()

    def _select_save_clicked(self):
        if self.on_select_save:
            self.on_select_save()

    def _run_clicked(self):
        if self.on_run:
            self.on_run()

    def _open_save_clicked(self):
        if self.on_open_save:
            self.on_open_save()
