# 📞 Histórico de Telefonia - Krolik

Ferramenta de busca e reprodução offline para o backup de gravações telefônicas da antiga operadora Krolik.
Este projeto foi desenvolvido para garantir acesso fácil e rápido aos arquivos de áudio hospedados no SharePoint/OneDrive da **Lancers**, sem depender de sistemas externos.

## 🚀 Funcionalidades

- **Busca Offline:** Indexação local via arquivo JSON estático.
- **Player Integrado:** Reprodução direta no navegador usando caminhos relativos.
- **Filtros:** Por data, número de telefone/ramal e tipo (Entrada/Saída).
- **Sem Servidor:** Funciona rodando apenas um arquivo HTML, ideal para compartilhar via OneDrive.

## 📂 Estrutura do Projeto

O projeto deve ser mantido na mesma estrutura de diretórios do backup de áudio:

```text
/OneDrive - Lancers/TI - Gravações Telefonia Krolik/
│
├── gravacoes_2024/       # (Dados Brutos - Não versionados)
├── gravacoes_2025/       # (Dados Brutos - Não versionados)
│
└── app/                  # (ESTE REPOSITÓRIO)
    ├── logos/            # Imagens da interface
    ├── gerar_indice.py   # Script gerador da base de dados
    ├── index.html        # Interface para o usuário final
    ├── banco_dados.js    # Base de dados gerada (GitIgnored)
    └── README.md         # Documentação

