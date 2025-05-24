# 📍 Leitura e Conversão de Memorial SIGEF para Excel/Word

Este projeto extrai e converte dados geoespaciais de 
**Memoriais Descritivos SIGEF em PDF** para formato **tabular** (Excel `.xlsx` ou Word `.docx`)

---

## 📁 Estrutura do Projeto

```bash
LeituraPDF/
├── main.py                      # Arquivo principal para execução
├── exporters/                   # Estratégias de exportação (Strategy Pattern)
│   ├── __init__.py              # Fábrica de exportadores
│   ├── adobe_pdf.py             # Exportação em PDF (.pdf)
│   ├── base.py                  # Interface abstrata (Exporter)
│   ├── excel_xlsx.py            # Exportação em Excel (.xlsx)
│   ├── web_html.py              # Exportação em HTML (.html)
│   └── word_docx.py             # Exportação em Word (.docx)
├── builder.py                   # Responsável por montar o DataFrame
├── extractor.py                 # Leitura e parsing do PDF (usando regex)
├── model.py                     # Objeto de domínio (VérticeRegistro)
```

---

## 🧠 Arquitetura / Padrões Utilizados

Este projeto foi desenhado com foco em manutenibilidade e escalabilidade.

| Padrão                    | Papel                                                          |
| ------------------------- |----------------------------------------------------------------|
| **Strategy Pattern**      | Escolha da forma de exportação (Excel, Word, CSV, etc.)        |
| **Factory Pattern**       | Criação de objetos exportadores com base no formato solicitado |
| **Single Responsibility** | Cada módulo tem uma única responsabilidade                     |
| **Data Wrapping**         | Objeto `VerticeRegistro` encapsula lógica dos dados            |

---

## 🚀 Como Executar

1) Crie um virtual env
2) Instale o requirements.txt
3) Ajuste o arquivo main com os parâmetros almejados

---

## 🔄 Estendendo o projeto

Quer adicionar um novo formato? Siga os passos:

1) Crie um novo arquivo, por exemplo json_exporter.py
2) Implemente a interface Exporter
3) Registre-o em exporters/__init__.py na ExporterFactory