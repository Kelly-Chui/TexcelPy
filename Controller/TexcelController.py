import webbrowser
from tkinter import filedialog

class TexcelController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # 이벤트 콜백 등록
        self.view.set_on_select_load(self.select_load_clicked)
        self.view.set_on_select_save(self.select_save_clicked)
        self.view.set_on_run(self.run_clicked)
        self.view.set_on_open_save(self.open_save_clicked)

        # 초기 라벨 텍스트 설정
        self.view.load_path_label.config(text=self.model.load_path)
        self.view.save_path_label.config(text=self.model.save_path)

    def select_load_clicked(self):
        folder_path = filedialog.askdirectory(initialdir=".", title="Select load folder")
        if folder_path:
            self.model.load_path = folder_path
            self.view.load_path_label.config(text=folder_path)

    def select_save_clicked(self):
        folder_path = filedialog.askdirectory(initialdir=".", title="Select save folder")
        if folder_path:
            self.model.save_path = folder_path
            self.view.save_path_label.config(text=folder_path)

    def run_clicked(self):
        self.model.make_excel_file()
        self.model.set_last_paths(self.model.save_path, self.model.load_path)

    def open_save_clicked(self):
        path = self.model.save_path.replace("\\", "/")
        if path:
            webbrowser.open("file://" + path)
