
## Requisitos
- Python 3.8+
- Nenhuma dependência externa.

# Career Advisor – Sistema de Análise e Recomendação de Carreiras

Este projeto é um **sistema CLI em Python** para cadastrar perfis profissionais, avaliar competências e gerar recomendações de carreira com base em similaridade entre o perfil do usuário e os requisitos de cada carreira.

## Visão Geral

O sistema permite:

1. Criar perfis com competências avaliadas de 0 a 10.
2. Editar perfis existentes.
3. Recomendar carreiras com base na compatibilidade.
4. Exportar perfis para JSON.

Os dados são salvos automaticamente no arquivo `profiles.json`.

---

## Estrutura do Projeto

O código é dividido em:

* **Modelos (Profile e Career)**
* **Funções de apoio (menus, validação, persistência)**
* **Base fixa de carreiras**
* **Sistema de recomendação**
* **Interface CLI**

---

## Classe Profile

Representa um perfil do usuário.

### Atributos

* `name`: Nome do perfil.
* `role_interest`: Área de interesse (opcional).
* `competences`: Dicionário `{competência: nota}`.

### Principais Métodos

* **set_competence(name, score)**: Define ou atualiza a nota de uma competência.
* **get(name)**: Retorna nota da competência (ou 0, caso não exista).
* **to_dict() / from_dict()**: Serialização para JSON.
* ****str**()**: Exibição formatada do perfil.

---

## Classe Career

Representa uma carreira com seus requisitos.

### Atributos

* `name`: Nome da carreira.
* `reqs`: Competências desejadas.
* `desc`: Descrição.
* `resources`: Lista de materiais de estudo.

### Principais Métodos

* **similarity(profile)**: Calcula compatibilidade entre 0 e 1, ponderando cada competência pela nota desejada.
* **gaps(profile)**: Lista lacunas do usuário para aquela carreira.

---

## Persistência de Dados

### `load_profiles()`

Carrega perfis do arquivo `profiles.json`. Caso o arquivo não exista, retorna uma lista vazia.

### `save_profiles(profiles)`

Salva todos os perfis em formato JSON.

---

## Funções Utilitárias

### `prompt_float(text)`

Solicita notas entre 0 e 10, garantindo validade da entrada.

### `choose(items, msg)`

Menu simples para seleção de itens.

---

## Base de Carreiras

A função `careers()` retorna uma lista de carreiras pré-configuradas, incluindo:

* Cientista de Dados
* Engenheiro de Software
* Especialista em RPA
* Product Manager
* Cibersegurança

Cada carreira possui:

* Competências desejadas
* Descrição
* Recursos recomendados

---

## Sistema de Recomendação

A função `recommend(profile, all_careers, top=3)`:

1. Calcula compatibilidade com cada carreira.
2. Identifica lacunas.
3. Ordena as carreiras por melhor aderência.
4. Retorna as melhores recomendações.

A CLI mostra:

* Compatibilidade (%).
* Descrição da carreira.
* Lacunas específicas.
* Recursos recomendados.

---

## Interface CLI

Menu principal:

```
[1] Novo perfil
[2] Listar perfis
[3] Editar competências
[4] Recomendar carreiras
[5] Exportar JSON
[0] Sair
```

### Fluxo recomendado

1. Criar perfil.
2. Preencher competências.
3. Visualizar recomendações.
4. Editar competências quando quiser.

---

## Arquivos Gerados

* **profiles.json**: Banco de perfis usado pelo sistema.
* **export_profiles.json**: Exportação manual.

## EXCUÇÃO

```bash
python app.py
