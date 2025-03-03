import flet as ft

import os
from pathlib import Path
from shared.base.SharedControls import SharedControls
from app.app_style import title_pg, button
import hashlib

PATH = Path(__file__).parent.parent.parent.parent / "assets"


class InsertUser(SharedControls):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._input_name = self.name()
        self._input_login = self.login()
        self._input_password = self.password()
        self._check_password = self.check_password()
        self._type_access = self.type_access()
        self.button_submit_register: ft.ElevatedButton = self.button_submit_signup(
            data="signup_submit", ) # var_on_change=var, var_alert=self.show_password_alert
        # self.button_submit_register: ft.ElevatedButton = self.button_submit_signup(data="signup_submit") #var_on_change=var, var_alert=self.show_password_alert
        self.get_content(self._input_name, self._input_login, self._input_password,
                         self._check_password, self._type_access,
                         self.button_submit_register)

    @classmethod
    def name(cls):
        return ft.TextField(label="Digite o Nome:", width=300, prefix_icon=ft.icons.PERSON)

    @classmethod
    def login(cls):
        return ft.TextField(label="Digite o Login:", width=300, prefix_icon=ft.icons.EMAIL)

    @classmethod
    def password(cls):
        return ft.TextField(label="Digite a Password:", width=300, password=True,
                            can_reveal_password=True, prefix_icon=ft.icons.LOCK)

    @classmethod
    def check_password(cls):
        return ft.TextField(label="Repita a Password:", width=300, password=True,
                            can_reveal_password=True, prefix_icon=ft.icons.LOCK)

    @classmethod
    def type_access(cls):
        return ft.Dropdown(
            options=[
                ft.dropdown.Option("Admin"),
                ft.dropdown.Option("Sub_Admin"),
                ft.dropdown.Option("User"),
            ],
            width=300,
        )

    @classmethod
    def button_submit_signup(cls, data, var_on_change=None, var_alert=None):
        return ft.ElevatedButton(text='Cadastro', width=140, on_click=var_alert,
                                 data=data, on_animation_end=var_on_change)

    @classmethod
    def get_content(cls, name, login, password, check_password, type_access, signup) -> ft.Container:
        return ft.Container(
            width=400,
            height=450,
            padding=50,
            border_radius=20,
            bgcolor="white",
            content=ft.Column(
                controls=[ft.Column(
                    controls=[
                        name,
                        login,
                        password,
                        check_password,
                        type_access,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                    ft.Row(controls=[
                        signup,
                    ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    )
                ],
            )
        )




