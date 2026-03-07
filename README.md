# Analise de Empreendedorismo em Santa Catarina

## Descricao do problema

Este projeto analisa a distribuicao de estabelecimentos por municipio no estado de Santa Catarina a partir de dados publicos do Mapa de Empresas. O problema investigado e a concentracao da atividade empreendedora no territorio catarinense: quais municipios concentram mais estabelecimentos, qual o peso relativo de cada um no total estadual e como essa distribuicao pode ser observada de forma clara por meio de tabelas e graficos.

## Objetivo

O objetivo da solucao e transformar um arquivo Excel bruto em um fluxo reprodutivel de analise exploratoria. A partir da base original, o projeto padroniza colunas, separa cidade e UF, organiza um ranking municipal, calcula participacao percentual e gera saidas visuais para apoiar a interpretacao dos principais polos economicos de Santa Catarina.

## Origem dos dados

A base utilizada no projeto esta armazenada localmente em `data/raw/dados_mapa_empresas.xlsx` e foi extraida a partir do Mapa de Empresas do Governo Federal. Referencia oficial do programa e dos paineis publicos:

- https://www.gov.br/empresas-e-negocios/pt-br/mapa-de-empresas
- https://www.gov.br/empresas-e-negocios/pt-br/mapa-de-empresas/painel-mapa-de-empresas

O notebook trabalha apenas com as colunas reais da base utilizadas nesta entrega: `[Municipio]` e `Estabelecimentos `.

## Etapas de tratamento

1. Leitura do arquivo Excel com `pandas.read_excel`.
2. Normalizacao dos nomes das colunas para reduzir inconsistencias de formato.
3. Remocao de colchetes e ajustes de espacos residuais nos nomes das colunas.
4. Renomeacao para `municipio` e `estabelecimentos`.
5. Tratamento de valores ausentes e linhas vazias.
6. Separacao do campo `municipio` em `cidade` e `uf` com base no padrao `Cidade - UF`.
7. Conversao da coluna `estabelecimentos` para formato numerico.
8. Ordenacao dos registros em ordem decrescente.
9. Calculo do percentual que cada municipio representa no total.
10. Geracao do ranking final e da participacao acumulada dos 10 principais municipios.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook
- openpyxl

## Resultados gerados

O repositorio produz artefatos prontos para avaliacao e publicacao:

- `outputs/tabelas/ranking_municipios.csv` com o ranking consolidado;
- `outputs/graficos/top_15_municipios.png` com os 15 municipios de maior volume;
- `outputs/graficos/participacao_top10.png` com a participacao percentual dos 10 principais polos.

Esses arquivos permitem avaliar rapidamente a concentracao economica e identificar os municipios de maior relevancia no conjunto de dados analisado.

## Estrutura do projeto

```text
desafio-ia-sctec-empreendedorismo-sc/
├── data/
│   └── raw/
│       └── dados_mapa_empresas.xlsx
├── notebooks/
│   └── analise_empreendedorismo_sc.ipynb
├── outputs/
│   ├── graficos/
│   │   ├── top_15_municipios.png
│   │   └── participacao_top10.png
│   └── tabelas/
│       └── ranking_municipios.csv
├── src/
│   ├── clean.py
│   ├── metrics.py
│   └── plots.py
├── README.md
├── requirements.txt
└── .gitignore
```

Descricao das pastas:

- `data`: contem o arquivo bruto utilizado na analise.
- `notebooks`: concentra o notebook principal da entrega.
- `outputs`: guarda tabelas e graficos gerados pelo fluxo analitico.
- `src`: reune funcoes auxiliares de limpeza, metricas e visualizacao.

## Instrucoes de execucao

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

Abra o arquivo abaixo e execute todas as celulas em ordem:

```text
notebooks/analise_empreendedorismo_sc.ipynb
```

Ao final da execucao, o projeto deve atualizar o ranking em CSV e os graficos na pasta `outputs/`.

## Link do video pitch

https://www.youtube.com/watch?v=e70t6kh-nZA

