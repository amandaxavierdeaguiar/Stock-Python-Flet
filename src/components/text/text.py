import flet as ft

class Text(ft.UserControl):
    def __init__(self, placehold: str):
        super().__init__()
        self.placehold = placehold

    def build(self):
        self.controls =[
            ft.Text(self.placehold)
        ]
