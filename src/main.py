import flet
import flet as ft
from flet import Container, padding, Page, Text, AppBar, PopupMenuButton, PopupMenuItem, colors, icons, margin, Column
from App.app_layout import AppLayout


class App(SharedControls):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.appbar_items = [
            PopupMenuItem(text="Login"),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar_logo = flet.Image(src="icons/logo-stock.png",
                                      width=30, height=30, fit=ft.ImageFit.CONTAIN, tooltip="Logo")
        self.appbar = AppBar(
            leading=self.appbar_logo,
            leading_width=50,
            title=Text("Stock Management", size=30, text_align="start"),
            center_title=False,
            toolbar_height=65,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                ),
            ],
        )
        self.view = Container(
            width=1000,
            padding=padding.all(0),
            margin=margin.all(0),
            expand=True,
            expand_loose=True,
            content=AppLayout(self, page)
        )
        self.page.add(self.view)
        self.page.appbar = self.appbar
        self.page.update()


def main(page: ft.Page):
    page.title = "Stock Management"
    page.window_min_width = 600
    page.window_min_height = 400
    page.window_width = 856
    page.window_height = 645
    page.padding = padding.all(0)
    page.margin = margin.all(0)
<<<<<<< HEAD
    page.bgcolor = ft.colors.GREY_300
=======
    # page.bgcolor = ft.colors.GREY_200
    page.bgcolor = ft.colors.GREY_400
    page.fonts = {
        "font_app": "assets/fonts/Roboto-Medium.ttf",
        "font_header": "assets/fonts/coolvetica rg.otf",
    }
    page.theme = ft.Theme(font_family="font_app")
    page.theme_mode = ft.ThemeMode.LIGHT
>>>>>>> a94351d (Update no Design)

    app = App(page)
    page.add(app)


if __name__ == "__main__":
    ft.app(target=main, view=flet.FLET_APP_WEB, assets_dir="./assets")
