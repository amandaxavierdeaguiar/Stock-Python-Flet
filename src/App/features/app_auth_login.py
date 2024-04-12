import flet as ft
import hashlib
import re
from flet import UserControl, TextField, Image
from flet_core import LoginEvent

from Views.User.ListUser import table_data as db_user


class AuthLogin(UserControl):
    def __init__(self, user, page, select_page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.user_Auth = user

        self._image: Image = self.image()
        self._input_login: TextField = self.login(self.validate)
        self._input_password: TextField = self.password(self.validate)
        self._checkbox_signup = self.checkbox_signup(self.validate)
        self._button_submit: ft.ElevatedButton = self.button_submit(var_on_click=self.login_alert)
        self.button_signup: ft.ElevatedButton = self.create_button_signup(data="login_signup",
                                                                          var_on_change=select_page)
        self.content = self.get_login(self._image, self._input_login,
                                      self._input_password, self._checkbox_signup,
                                      self._button_submit, self.button_signup)

    def validate(self, e: ft.ControlEvent) -> None:
        if all([self._input_login.value, self._input_password.value, self._checkbox_signup.value]):
            self._button_submit.disabled = False
        else:
            self._button_submit.disabled = True

        self.page.update()

    @classmethod
    def image(cls):
        return ft.Image(src="icons/login.png", width=150, height=150)

    @classmethod
    def login(cls, var_on_change=None):
        return ft.TextField(label="Digite seu email", width=300, prefix_icon=ft.icons.EMAIL, on_change=var_on_change)

    @classmethod
    def password(cls, var_on_change=None):
        return ft.TextField(label="Digite sua Password", width=300, password=True,
                            can_reveal_password=True,
                            prefix_icon=ft.icons.LOCK,
                            on_change=var_on_change)

    @classmethod
    def checkbox_signup(cls, var_on_change=None):
        return ft.Checkbox(label='Aceito os termos de uso', value=False, on_change=var_on_change)

    @classmethod
    def button_submit(cls, var_on_click):
        return ft.ElevatedButton(text='Entre', width=140, disabled=True, on_click=var_on_click, data='login')

    @classmethod
    def create_button_signup(cls, data, var_on_change=None):
        return ft.ElevatedButton(text='Cadastra-se', width=140, on_click=var_on_change, data=data)

    @classmethod
    def get_login(cls, image, login, password, checkbox, submit, signup):
        return ft.Container(
            width=400,
            height=450,
            padding=20,
            border_radius=20,
            bgcolor="white",
            content=ft.Column(
                controls=[ft.Column(
                    controls=[
                        image,
                        login,
                        password,
                        checkbox,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                    ft.Row(controls=[
                        signup,
                        submit,
                    ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    )
                ],
            )
        )

    def login_alert(self, event):
        user = next((item for item in db_user if item['login'] == self._input_login.value), None)
        if user is None:
            dlg = ft.AlertDialog(
                title=ft.Text("Email Inválido"),
                content=ft.Text("Digite novamente os dados!"),
            )
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
        else:
            self.user_Auth.is_login = True
            self.page.logout()