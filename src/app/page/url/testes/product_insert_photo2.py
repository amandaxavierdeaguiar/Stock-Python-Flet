import os

import flet as ft
import base64
from flet import colors, icons, IconButton
from views.Product.ProductView import ProductView
from app.app_style import *


class ProductNew:
    ctrl_product_view = ProductView()
    title_product: ft.Text
    txt_name_product: ft.TextField
    txt_price: ft.TextField
    _product_category_input: ft.Dropdown
    _product_brand_input: ft.Dropdown
    button_enter: ft.ElevatedButton
    btn_close_img: IconButton
    img: ft.Image
    img_Container: ft.Stack
    file_picker: ft.FilePicker
    # button_image: ft.ElevatedButton
    btn: ft.ElevatedButton
    description_product: ft.TextField
    bar_cod: ft.TextField
    _product_quantity_type: ft.Dropdown

    def close_img(self, e):
        self.img_Container.visible = not self.img_Container.visible
        self.btn_close_img.visible = not self.btn_close_img.visible
        self.image_insert_product.visible = not self.image_insert_product.visible
        self.button_image.visible = not self.button_image.visible
        self.page.update()

    def validate(self, e):
        if self.txt_name_product.value:
            self.button_image.visible = True
            self.button_image.disabled = False
        else:
            self.button_image.visible = False
            self.button_image.disabled = True

        self.page.update()

    def __init__(self, page: ft.Page):
        self.page = page
        page.title = 'Produtos'
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.bgcolor = ft.colors.GREY_400

        self.title_product = ft.Text("Insira o produto", **title_pg())

        self.txt_price = ft.TextField(label="Valor do produto", width=300, ) #TRANSFORMAR DEPOIS PARA FLOAT

        self._product_category_input = self.product_category()
        self._product_brand_input = self.product_brandy()
        
        # self._product_quantity_type = self.quantity_type()

        self.button_enter = ft.ElevatedButton("Insira o produto", **button(), icon=icons.SAVE, on_click=self.on_submit)

        self.btn_close_img = IconButton(
            bgcolor=colors.BLACK26,
            top=10, right=10,
            icon=icons.CLOSE, icon_color=colors.WHITE54, selected=True,
            selected_icon=icons.CLOSE, on_click=self.close_img, visible=False)

        self.img = ft.Image(visible=False, fit=ft.ImageFit.CONTAIN)

        self.img_Container = ft.Stack(
            [
                self.img,
                self.btn_close_img,
            ],
            width=300,
            height=300,
            visible=False
        )

        def insert_img_product(e: ft.FilePickerResultEvent):
            if e.files and len(e.files):
                file_path = e.files[0].path
                with open(file_path, 'rb') as f:
                    image_content = f.read()

                    # Converte a imagem em base64 para exibição
                    img_base64 = base64.b64encode(image_content).decode('utf-8')
                    self.img.src_base64 = img_base64

                    # Obter a extensão do arquivo usando o método os.path.splitext
                    file_name, file_extension = os.path.splitext(file_path)

                    # Nome do produto em letras minúsculas, separado por _
                    name_text = self.txt_name_product.value.strip().lower().split()
                    name_separate = "_".join(name_text)
                    file_name = name_separate + file_extension

                    # Diretório de destino para salvar a imagem
                    directory = os.path.abspath('../../assets/products')
                    if not os.path.exists(directory):
                        os.makedirs(directory)

                    # Salvar o arquivo no diretório
                    with open(os.path.join(directory, file_name), 'wb') as w:
                        w.write(image_content)

                    # Atualiza a interface gráfica
                    self.img_Container.visible = True
                    self.btn_close_img.visible = True
                    self.img.visible = True
                    self.image_insert_product.visible = False
                    self.button_image.visible = False

                    page.update()

        file_picker = ft.FilePicker(on_result=insert_img_product)
        page.overlay.append(file_picker)

        self.txt_name_product = ft.TextField(label="Nome do Produto", width=300)

        self.button_image = ft.ElevatedButton(text='Insira a Imagem', **button(), icon=icons.UPLOAD_FILE,
                                              on_click=lambda _: file_picker.pick_files
                                              (allow_multiple=False, allowed_extensions=['jpg', 'jpeg', 'png']))

        self.validate(self)

        # Para declarar na funcao validate e esconder o botao até a inserção do nome
        self.txt_name_product.on_change = self.validate

        self.description_product = ft.TextField(label="Descrição do produto", multiline=True, max_lines=3)

        # Funcao que deixa a foto e caso adicione uma imagem, tira ela
        self.image_insert_product = ft.Image(src=f"../../App_Amanda/assets/icons/produtos.png", width=200, height=200, fit=ft.ImageFit.CONTAIN)

        page.add(
            ft.Container(
                width=650,
                height=480,
                padding=10,
                border_radius=20,
                bgcolor="white",
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                    ],

                                    spacing=5,
                                ),
                                ft.Column(width=200, height=400,
                                          controls=[
                                              self.image_insert_product,
                                              self.img_Container,
                                              self.button_image,
                                              self.button_enter
                                          ],
                                          spacing=20,
                                          alignment=ft.MainAxisAlignment.CENTER,
                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                          ),
                            ],
                            spacing=20,
                        ),
                        ft.Column(width=30,
                                  controls=[
                                  ],
                                  ),
                        ft.Column(
                            controls=[
                                self.title_product,
                                self.txt_name_product,
                                self.txt_price,
                                self._product_brand_input,
                                self._product_category_input,
                                self.description_product,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                        ),

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            )
        )

    @classmethod
    def product_brandy(cls):
        brandy = cls.ctrl_brand_view.get_name_brands()
        brandy_all = ft.Dropdown(label="Marca", width=300)
        for brandy in brandy:
            brandy_all.options.append(ft.dropdown.Option(brandy))

        return brandy_all

    @classmethod
    def product_category(cls):
        category = cls.ctrl_category_view.get_name_category()
        category_all = ft.Dropdown(label="Categoria", width=300)
        for category in category:
            category_all.options.append(ft.dropdown.Option(category))
        return category_all
    
    @classmethod
    def quantity_type(cls):
        test = QuantityType()
        quantity = ft.Dropdown(label="Tipo Quantidade", width=300)

    @classmethod
    def on_submit(cls, e):
        new_data = {
            'name': cls.txt_name_product.value,
            'photo': cls.img.src_base64,
            'Description': cls.description_product.value,
            'price': float(cls.txt_price.value),
            'brand_name': cls._product_brand_input.value,
            'category_name': cls._product_category_input.value,
            'quantity_type': cls._product_quantity_type,
        }

        cls.ctrl_product_view.add_product(new_data)
        
if __name__ == '__main__':
    
    ft.app(target=ProductNew, assets_dir="../../assets")
