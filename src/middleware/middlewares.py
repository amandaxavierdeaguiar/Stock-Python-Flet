def auth_middleware(page, route):
    """ Middleware de autenticação """
    protected_routes = ["/dashboard"]  # Rotas protegidas

    if route in protected_routes and not page.session.get("user"):
        page.go("/login")  # Redireciona para login
        return False  # Bloqueia o acesso
    return True  # Permite acesso