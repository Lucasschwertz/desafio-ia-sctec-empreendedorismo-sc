# Análise de Empreendedorismo em Santa Catarina

## Objetivo

Este projeto analisa a distribuição de estabelecimentos por município no estado de Santa Catarina a partir de dados públicos do Mapa de Empresas. O foco é transformar um arquivo Excel em uma base organizada para análise exploratória, permitindo identificar os municípios com maior concentração de estabelecimentos e medir a participação relativa de cada localidade no total observado.

## Fonte de Dados

O projeto utiliza um arquivo Excel com o número de estabelecimentos por município. A base é armazenada em `data/raw/dados_mapa_empresas.xlsx` e é lida diretamente no notebook principal, sem alteração do arquivo original.

## Metodologia

- leitura do Excel com `pandas`
- limpeza e padronização de colunas
- separação cidade/UF
- cálculo de participação percentual
- ranking de municípios
- visualização com gráficos

A lógica da análise preserva o schema real da base. O campo de município é tratado para separar `cidade` e `uf`, a coluna de estabelecimentos é convertida para valor numérico e os dados são ordenados de forma decrescente para formar o ranking municipal.

## Resultados

Os principais artefatos produzidos pelo projeto são:

- ranking de municípios por número de estabelecimentos
- gráfico Top 15 municípios
- participação percentual dos principais polos econômicos

Os resultados ficam salvos em arquivos prontos para consulta e publicação, com destaque para `outputs/tabelas/ranking_municipios.csv`, `outputs/graficos/top_15_municipios.png` e `outputs/graficos/participacao_top10.png`.

## Estrutura do Projeto

```text
desafio-ia-sctec-empreendedorismo-sc/
├ data/
│  └ raw/
│     └ dados_mapa_empresas.xlsx
├ notebooks/
│  └ analise_empreendedorismo_sc.ipynb
├ outputs/
│  ├ graficos/
│  │  ├ top_15_municipios.png
│  │  └ participacao_top10.png
│  └ tabelas/
│     └ ranking_municipios.csv
├ src/
│  ├ clean.py
│  ├ metrics.py
│  └ plots.py
├ README.md
├ requirements.txt
└ .gitignore
```

Descrição das pastas:

- `data`: armazena o arquivo bruto utilizado na análise.
- `notebooks`: contém o notebook principal com o fluxo analítico.
- `outputs`: guarda tabelas e gráficos gerados durante a exploração dos dados.
- `src`: concentra funções auxiliares de limpeza, métricas e visualização, mantendo o notebook mais organizado.

## Como Executar

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

Abra o arquivo:

```text
notebooks/analise_empreendedorismo_sc.ipynb
```

Execute todas as células na ordem. Ao final, o notebook irá gerar o ranking consolidado e os gráficos de apoio na pasta `outputs/`.
