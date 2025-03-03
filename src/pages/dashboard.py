import flet as ft

from app.page.app_header import AppHeader

class DashboardPage(ft.View):
    def __init__(self, page):
        super().__init__()

        self.appbar = AppHeader(page).app_bar
        self.bgcolor = ft.colors.GREY_400  if page.theme_mode == "light"  else ft.colors.GREY_900
        self.padding = 20
        self.controls = [
            # TODO ADICONAR TITULO PAGINA
            ft.Text("Titulo Pagina", size=36),
            ft.Container(
                padding = 5,
                expand = True,
                expand_loose= True,
                col = 12,
                bgcolor = "white"  if page.theme_mode == "light"  else ft.colors.GREY_800 ,
                border_radius = 20,
                adaptive=True,
                content=ft.Column(
                    controls=[
                        ft.Text("Painel do usuário"),
                        ft.ElevatedButton("Sair", on_click=lambda _: logout(page))
                    ]
                )
            ),
        ]

def logout(page):
    page.session.clear()
    page.go("/")
