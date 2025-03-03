Aqui está o markdown para o seu README.md:

```markdown
# Estrutura do Projeto Stock-Python-Flet

## Organização de Pastas

```
Stock-Python-Flet/
├── src/
│   ├── pages/            # Todas as páginas da aplicação
│   │   ├── products/     # Página de produtos
│   │   ├── stock/        # Página de estoque
│   │   └── home/         # Página inicial
│   │
│   ├── routes/           # Configuração de rotas
│   │   └── routes.py     # Definição das rotas
│   │
│   ├── components/       # Componentes reutilizáveis
│   │   ├── buttons/
│   │   ├── inputs/
│   │   └── layout/
│   │
│   ├── services/         # Lógica de negócio
│   │   ├── product_service.py
│   │   └── stock_service.py
│   │
│   ├── repositories/     # Acesso a dados
│   │   ├── product_repository.py
│   │   └── stock_repository.py
│   │
│   ├── models/          # Modelos/Entidades
│   │   └── product.py
│   │
│   ├── utils/           # Funções utilitárias
│   │   └── helpers.py
│   │
│   ├── assets/          # Recursos estáticos
│   │   ├── images/
│   │   └── styles/
│   │
│   └── main.py          # Entrada da aplicação
│
├── .devcontainer/        # Configuração Docker
├── poetry.lock          # Dependências
└── pyproject.toml       # Configuração do projeto
```

## Descrição das Pastas

### `/src`
Diretório principal do código fonte.

### `/src/pages`
Contém todas as páginas da aplicação, cada uma em seu próprio diretório.
- `/products` - Gestão de produtos
- `/stock` - Gestão de estoque
- `/home` - Página inicial

### `/src/routes`
Configuração e gestão de rotas da aplicação.
- `routes.py` - Define todas as rotas disponíveis

### `/src/components`
Componentes reutilizáveis da interface.
- `/buttons` - Botões customizados
- `/inputs` - Campos de entrada
- `/layout` - Componentes de layout

### `/src/services`
Camada de serviços contendo a lógica de negócio.
- `product_service.py` - Lógica relacionada a produtos
- `stock_service.py` - Lógica relacionada ao estoque

### `/src/repositories`
Camada de acesso a dados.
- `product_repository.py` - Acesso a dados de produtos
- `stock_repository.py` - Acesso a dados de estoque

### `/src/models`
Definição das entidades e modelos de dados.
- `product.py` - Modelo de produto

### `/src/utils`
Funções utilitárias e helpers.
- `helpers.py` - Funções auxiliares

### `/src/assets`
Recursos estáticos da aplicação.
- `/images` - Imagens
- `/styles` - Estilos

### `/src/main.py`
Ponto de entrada da aplicação.

## Arquivos de Configuração

- `.devcontainer/` - Configurações para desenvolvimento em container
- `poetry.lock` - Lock file das dependências
- `pyproject.toml` - Configuração do projeto e dependências
```

Este README fornece uma visão clara da estrutura do projeto e pode ser atualizado conforme necessário. Você pode adicionar mais seções como:
- Instruções de instalação
- Como rodar o projeto
- Dependências principais
- Padrões de código
- etc.
