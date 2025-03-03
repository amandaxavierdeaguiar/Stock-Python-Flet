from pages.home import HomePage
from pages.dashboard import DashboardPage
from pages.login import LoginPage

# Simulação de rotas Laravel
routes = {
    "/": HomePage,
    "/dashboard": DashboardPage,
    "/login": LoginPage
}

def get_route(page, route):
    """ Retorna a página correspondente à rota """
    if route in routes:
        return routes[route](page)
    return HomePage(page)  # Rota padrão (404 pode ser implementado)