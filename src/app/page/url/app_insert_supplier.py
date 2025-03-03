import flet as ft

import os
from pathlib import Path

from models.user.auth.UserAuthentication import UserAuthentication
from shared.base.SharedControls import SharedControls
from app.app_style import title_pg, button
import re

from views.Product.ProductView import ProductView

PATH = Path(__file__).parent.parent.parent.parent / "assets"


class InsertSupplier(SharedControls):
    title_supplier: ft.Text
    txt_name_supplier: ft.TextField
    txt_address_supplier: ft.TextField
    txt_phone_supplier: ft.TextField
    txt_email_supplier: ft.TextField
    button_enter: ft.ElevatedButton
    image_supplier: ft.Image
    btn_close_supplier: ft.IconButton
    container: ft.Container
    email: ft.TextField
    # validate_email = None

    ctrl_product_view = ProductView()

    _user: UserAuthentication

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.validate_email = self.user.validate_email


    @classmethod
    def get_content(cls, show=None):
        cls.title_supplier = ft.Text("Insira o Fornecedor", **title_pg())

        cls.txt_name_supplier = ft.TextField(label="Nome do Fornecedor: ", width=300, height=50)
        cls.txt_address_supplier = ft.TextField(label="Morada do Fornecedor: ", width=300, height=50)
        cls.txt_phone_supplier = ft.TextField(label="Telefone do Fornecedor: ", width=300, height=50,
                                              input_filter=ft.InputFilter(
                                                  allow=False, regex_string=r"[0-9+]", replacement_string=''))
        cls.txt_email_supplier = ft.TextField(label="Email", width=300, height=50, )
        # r"[0-9+]"
        # regex_string=r'^[a-zA-Z]+[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,7}
        cls.button_enter = ft.ElevatedButton("Insira o produto", **button(),
                                             on_click=cls.bd_supplier)
        # on_click=cls.bd_supplier
        # on_click=lambda _: cls.insert_supplier(cls.txt_email_supplier.value)

        cls.image_supplier = ft.Image(src=f"{PATH}/icons/supplier_insert.png", width=200, height=200,
                                      fit=ft.ImageFit.CONTAIN)

        container = ft.Container(
            width=600,
            height=400,
            padding=10,
            border_radius=20,
            bgcolor="white",
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Column(width=200, height=400,
                                      controls=[
                                          cls.image_supplier,
                                      ],
                                      alignment=ft.MainAxisAlignment.CENTER,
                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                      ),
                        ],
                        spacing=20,
                    ),
                    ft.Column(
                        controls=[
                            cls.title_supplier,
                            cls.txt_name_supplier,
                            cls.txt_address_supplier,
                            cls.txt_phone_supplier,
                            cls.txt_email_supplier,
                            cls.button_enter,
                        ],
                        spacing=30,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
        return container

    @classmethod
    def insert_supplier(cls, email):
        if not cls.validate_email(email):
            cls.txt_email_supplier.error_text = 'Email não válido!'
            print('Nao válido o email')
        else:
            cls.bd_supplier()

    @classmethod
    def validate_email(cls, email):
        pattern = r'^[a-zA-Z]+[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,7}$'

        if re.match(pattern, email):
            return True
        else:
            return False


    """def insert_supplier(self, email):
        if not self.validate_email(email):
            alert = ft.AlertDialog(
                title=ft.Text("Email Inválido"),
                content=ft.Text("Favor insira novamente!"),
            )
            self.page.dialog = alert
            alert.open = True
            self.page.update()
            print('Nao válido o email')
        else:
            self.bd_supplier()

    def validate_email(self, email):
        pattern = r'^[a-zA-Z]+[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,7}$'

        if re.match(pattern, email):
            return True
        else:
            return False"""

    @classmethod
    def bd_supplier(cls, e=None):
        print()
        new_data = {
            'name': cls.txt_name_supplier.value,
            'address': cls.txt_address_supplier.value,
            'phone': cls.txt_phone_supplier.value,
            'email': cls.txt_email_supplier.value,
        }

        cls.ctrl_product_view.add_supplier(new_data)



