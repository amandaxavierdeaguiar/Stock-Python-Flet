import flet as ft

from components.button.style import button_style

class Button(ft.UserControl):
    def __init__(self, text: str, on_click=None):
        super().__init__()
        self.text = text
        self.on_click = on_click  # Função de clique

    def build(self):
        self.controls = [
            ft.ElevatedButton(
            text=self.text,
            on_click=self.on_click,
            width=140,
            style= button_style()
        )]
