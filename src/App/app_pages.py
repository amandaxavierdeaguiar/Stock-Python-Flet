import flet as ft
from flet import Text, Column, Card, Row, Container, UserControl, icons

from App.app_table import AppTable
from App.app_menu import AppMenu
from Views.Product.ListProduct import table_data as db_product
from Views.Supplier.ListSupplier import table_data as db_supplier
from Views.User.ListUser import table_data as db_user

list_tables = {
    0: db_product,
    1: db_supplier,
    2: db_user,
}


class AppPages(UserControl):
    """

    """

    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__()
        self.page = page
        self.app_menu = AppMenu(self.page)
        pages = [
            (
                self.app_menu.create_menu_btn(label_='Stock', icon_=icons.WAREHOUSE_OUTLINED),
                self.create_content(0),
            ),
            (
                self.app_menu.create_menu_btn(label_='Supplier', icon_=icons.PERSON_2),
                self.create_content(1),
            ),
            (
                self.app_menu.create_menu_btn(label_='Use', icon_=icons.PERSON),
                self.create_content(2),
            ),
        ]
        self.navigation_items = [navigation_item for navigation_item, _ in pages]
        self.navigation_rail = self.app_menu.build_navigation_rail(self._navigation_change)
        self.update_destinations()
        self._menu_extended = True
        self.navigation_rail.extended = True

        self.menu_panel = self.app_menu.get_menu(self.navigation_rail)

        page_contents = [page_content for _, [page_content, list_view] in pages]
        self.content_area = Column(controls=page_contents, expand=True)

        self.set_content()
        self._change_displayed_page()

    def select_page(self, page_number):
        self.navigation_rail.selected_index = page_number
        self._change_displayed_page()

    def _navigation_change(self, e):
        self._change_displayed_page()
        self.page.update()

    def _change_displayed_page(self):
        page_number = self.navigation_rail.selected_index
        for i, content_page in enumerate(self.content_area.controls):
            # update selected page
            content_page.visible = page_number == i

    def update_destinations(self):
        self.navigation_rail.destinations = self.navigation_items
        self.navigation_rail.label_type = ft.NavigationRailLabelType.ALL,

    def set_content(self, panel_=None):
        self.controls = [self.menu_panel, self.content_area]
        self.update_destinations()
        self.navigation_rail.extended = self._menu_extended
        if panel_:
            self.menu_panel.visible = panel_
        return self.controls

    @classmethod
    def create_content(cls, view=0):
        """

        :param view:
        :return:
        """
        list_view = ft.ListView(
            controls=[
                AppTable.get_table(list_tables[view]),
            ], spacing=10, padding=10, auto_scroll=False
        )
        content = Container(
            border_radius=5,
            padding=ft.padding.all(5),
            margin=ft.margin.all(10),
            expand=True,
            expand_loose=True,
            bgcolor=ft.colors.GREY_50,
            content=list_view,
            adaptive=True,
        )
        return content, list_view

    @classmethod
    def create_page(cls, title: str, body: str):
        """

        :param title:
        :param body:
        :return:
        """
        return Row(
            controls=[
                Column(
                    horizontal_alignment="stretch",
                    controls=[
                        Card(content=Container(Text(title, weight="bold"), padding=8)),
                        Text(body),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
