# Logística Alpha - Automação de Cadastro de Fretes

Projeto de automação de entrada de dados desenvolvido em Python. O objetivo é eliminar o preenchimento manual de planilhas, garantindo a padronização e persistência dos dados para futura análise.

**Contexto:** Desenvolvido durante o Bootcamp de Análise de Dados da Generation Brasil.

---

## Visão Geral do Projeto

A aplicação resolve o problema de descentralização de informações logísticas. Ao invés de manipular arquivos CSV/Excel diretamente  o que é propenso a erros humanos , o usuário utiliza uma interface gráfica controlada.

**Principais Funcionalidades:**
* **Interface Gráfica (GUI):** Formulários de cadastro construídos com Tkinter.
* **Persistência de Dados:** Uso da biblioteca Pandas para gerenciar, estruturar e salvar os dados em arquivos CSV (`dados_frete.csv` e `dados_clientes.csv`).
* **Validação de Entrada:** Tratamento de exceções para impedir registros vazios ou corrupção de arquivos abertos.
* **Separação de Responsabilidades:** Código estruturado em módulo de interface (`main.py`) e módulo lógico (`funcoes.py`).

---

## Estrutura do Repositório

```text
/
├── main.py              # Interface do usuário (Front-end Desktop)
├── funcoes.py           # Lógica de manipulação de dados (Back-end/Pandas)
├── dados_frete.csv      # Base de dados de fretes (Gerado pelo sistema)
├── dados_clientes.csv   # Base de dados de clientes (Gerado pelo sistema)
└── requirements.txt     # Dependências do projeto
