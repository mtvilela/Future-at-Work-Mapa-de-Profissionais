
## Requisitos
- Python 3.8+
- Nenhuma dependência externa.

## Execução
```bash
python app.py

# Career Advisor – Sistema de Análise e Recomendação de Carreiras

Este projeto é um **sistema CLI (linha de comando)** escrito em Python que permite cadastrar perfis profissionais, avaliar competências e gerar recomendações de carreira utilizando um modelo simples baseado em similaridade entre perfil e requisitos de cada profissão.

O objetivo é oferecer uma ferramenta organizada, objetiva e extensível para estudos de orientação profissional, análise de lacunas e sugestões personalizadas.

---

# 🚀 Visão Geral do Projeto

O projeto funciona em etapas:

1. **Cadastro de perfis** – Nome, área de interesse e avaliação de competências.
2. **Edição de perfis já existentes**.
3. **Recomendação de carreiras** – Baseada em um cálculo de similaridade entre o perfil do usuário e as competências desejadas para cada carreira.
4. **Exportação dos dados** para JSON.

Todos os perfis ficam armazenados no arquivo `profiles.json`.

---

# 🧱 Estrutura do Código

O projeto é dividido em blocos principais:

* **Modelos (classes Profile e Career)**
* **Funções de apoio para entrada, menus e persistência**
* **Base fixa de carreiras**
* **Sistema de recomendação**
* **Interface CLI**

A seguir, cada parte é explicada em detalhes.

---

# 🔹 Classe Profile

Representa um usuário do sistema.

### Atributos:

* `name` – Nome do perfil.
* `role_interest` – Interesse profissional (opcional).
* `competences` – Dicionário `{competência: nota}` com valores entre 0 e 10.

### Métodos importantes:

#### `set_competence(name, score)`

Adiciona ou atualiza a nota de uma competência.

#### `get(name)`

Retorna a nota de uma competência. Caso não exista, retorna **0**.

#### `to_dict()` / `from_dict()`

Serialização e desserialização para JSON.

#### `__str__()`

Formatação de impressão do perfil.

---

# 🔹 Classe Career

Representa uma carreira com seus requisitos.

### Atributos:

* `name` – Nome da carreira.
* `reqs` – Dicionário com notas desejadas por competência.
* `desc` – Descrição da área.
* `resources` – Lista de materiais de estudo recomendados.

### Métodos importantes:

#### `similarity(profile)`

Calcula o **índice de compatibilidade** entre o perfil e os requisitos da carreira.

* A lógica compara cada competência desejada com a nota que o perfil possui.
* O cálculo considera diferença proporcional e pesos baseados na importância (nota desejada).

Retorna um valor entre **0 e 1**, usado para ranquear recomendações.

#### `gaps(profile)`

Retorna um dicionário de lacunas:

```
{competência: quanto falta}
```

Usado para indicar o que o usuário precisa melhorar.

---

# 🔹 Persistência de Dados

O sistema salva e lê perfis em JSON.

### `load_profiles()`

* Carrega todos os perfis existentes do arquivo `profiles.json`.

### `save_profiles(profiles)`

* Salva a lista de perfis no mesmo arquivo.

Você nunca perde dados entre execuções.

---

# 🔹 Funções Utilitárias

### `prompt_float(text)`

Garante que entradas numéricas sejam válidas entre 0 e 10.

### `choose(items, msg)`

Menu simples para escolher itens da lista.

---

# 🔹 Base de Carreiras

O sistema inclui uma lista fixa de carreiras como:

* Cientista de Dados
* Engenheiro de Software
* Especialista em RPA
* Product Manager
* Cibersegurança

Cada uma possui:

* descrição
* requisitos
* lista de materiais recomendados

Essa lista pode ser estendida facilmente.

---

# 🔹 Sistema de Recomendação

A função `recommend(profile, careers, top=3)`:

1. Calcula similaridade do perfil com cada carreira.
2. Identifica lacunas do usuário.
3. Ordena por maior compatibilidade.
4. Retorna as melhores opções.

Na interface CLI, as recomendações exibem:

* porcentagem de compatibilidade
* lacunas
* descrição da área
* recursos para estudo

---

# 🖥️ Interface CLI

O `main()` fornece o menu principal:

```
[1] Novo perfil
[2] Listar perfis
[3] Editar competências
[4] Recomendar carreiras
[5] Exportar JSON
[0] Sair
```

### Fluxo de uso:

* Criar um novo perfil e avaliar competências
* Editar habilidades quando quiser
* Gerar recomendações
* Exportar perfis se necessário

---

# 📦 Arquivos Gerados

* `profiles.json` — Armazena todos os perfis criados.
* `export_profiles.json` — Exportação manual via menu.

---

# 🔧 Como Executar

Certifique-se de ter Python 3 instalado.

No terminal:

```
python3 nome_do_arquivo.py
```

---

# 🧩 Possíveis Extensões Futuras

* Interface gráfica (Tkinter / PyQt)
* Sistema de pesos customizáveis
* Inclusão de testes automatizados
* Dashboard com gráficos
* API REST

---

# ✔️ Conclusão

Este sistema demonstra uma arquitetura limpa e organizada para análise de competências e recomendação de carreiras. É facilmente expansível e serve como base para projetos mais avançados de orientação profissional, análise de dados ou aprendizagem de Python orientado a objetos.

