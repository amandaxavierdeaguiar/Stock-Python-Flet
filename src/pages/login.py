import flet as ft
from flet_core.types import CrossAxisAlignment, MainAxisAlignment

from components.button.button import Button
from components.text_input.text_input import TextInput
from app.page.app_header import AppHeader

class LoginPage(ft.View):
    def __init__(self, page):
        super().__init__()

        def login(_):
            page.session.set("user", "admin")  # Simula um login
            page.go("/dashboard")

        # TODO ARRANJAR HEADER
        self.appbar = AppHeader(page).app_bar
        self.bgcolor = ft.colors.GREY_400  if page.theme_mode == "light"  else ft.colors.GREY_900
        self.vertical_alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.controls = [
            ft.Container(
                width=400,
                height=450,
                padding=20,
                alignment=ft.alignment.center,
                border_radius=20,
                bgcolor= "white" if page.theme_mode == "light" else ft.colors.GREY_800,
                content=ft.Column(
                    controls=[
                        ft.Column(
                            controls=[
                                # TODO FAZER COMPONENT DE IMAGEM
                                ft.Image(src="icons/login.png", width=150, height=150)
                            ]
                        ),
                        ft.Column(
                            controls=[
                                TextInput("Email", ft.icons.EMAIL),
                                TextInput("Password", ft.icons.LOCK, is_password=True),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                Button("Entrar", on_click=login),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        ]
