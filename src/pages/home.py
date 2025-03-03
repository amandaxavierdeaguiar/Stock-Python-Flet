import flet as ft

class HomePage(ft.View):
    def __init__(self, page):
        super().__init__()
        self.controls = [
            ft.Text("Bem-vindo ao Home!"),
            ft.ElevatedButton("Ir para Dashboard", on_click=lambda _: page.go("/dashboard"))
        ]