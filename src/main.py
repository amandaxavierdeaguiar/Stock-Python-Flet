import flet as ft

from flet import Container, padding, margin
from routes.routes import get_route
from middleware.middlewares import auth_middleware
from app.app_window import AppWindow
from shared.base.SharedControls import SharedControls


class App(SharedControls):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.app_view = Container(
            expand=True,
            expand_loose=True,
            padding=padding.all(0),
            margin=margin.all(0),
            alignment=ft.alignment.center,
            content=AppWindow(self.page),
        )
        self.page.add(self.app_view)
        self.page.update()


# def main(page: ft.Page):
#     page.title = "Stock Management"
#     page.window_min_width = 600
#     page.window_min_height = 400
#     page.window_width = 856
#     page.window_height = 645
#     page.padding = padding.all(0)
#     page.margin = margin.all(0)
#     # page.bgcolor = ft.colors.GREY_200
#     page.bgcolor = ft.colors.GREY_400
#     page.fonts = {
#         "font_app": "assets/fonts/Roboto-Medium.ttf",
#         "font_header": "assets/fonts/coolvetica rg.otf",
#     }
#     page.theme = ft.Theme(font_family="font_app")
#
#     app = App(page)
#     page.add(app)

def main(page: ft.Page):
    page.title = "Stock Management"
    page.window_min_width = 600
    page.window_min_height = 400
    page.window_width = 856
    page.window_height = 645
    page.padding = padding.all(0)
    page.bgcolor = ft.colors.GREY_400
    page.fonts = {
        "font_app": "assets/fonts/Roboto-Medium.ttf",
        "font_header": "assets/fonts/coolvetica rg.otf",
    }
    page.theme = ft.Theme(font_family="font_app")

    def route_change(route):
        if auth_middleware(page, route):
            page.views.clear()
            page.views.append(get_route(page, route))
            page.update()

    page.on_route_change = lambda e: route_change(e.route)
    page.go("/")  # Define a rota inicial


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="./assets")
