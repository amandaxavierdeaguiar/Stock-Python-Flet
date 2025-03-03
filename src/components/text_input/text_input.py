import flet as ft

class TextInput(ft.UserControl):
    def __init__(self, placehold: str, icon: str, is_password:bool=False, on_click=None):
        super().__init__()
        self.placehold = placehold
        self.icon = icon
        self.on_click = on_click
        self.is_password= is_password

    def build(self):
        self.controls =[
            ft.TextField(
                label=self.placehold,
                width=300,
                password=self.is_password,
                can_reveal_password=True,
                prefix_icon=self.icon,
                on_change=self.on_click,
            )
        ]
