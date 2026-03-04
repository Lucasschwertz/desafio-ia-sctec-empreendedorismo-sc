# desafio-ia-sctec-empreendedorismo-sc

## 1. Introducao

Este projeto em Python foi criado para analisar dados publicos do Mapa de Empresas com foco no estado de Santa Catarina. A proposta e transformar um arquivo Excel bruto em uma base organizada para leitura analitica, permitindo observar como os estabelecimentos estao distribuidos entre os municipios catarinenses. O fluxo foi pensado para ser simples, reproduzivel e facil de adaptar a novas versoes do arquivo, mantendo a separacao entre dados brutos, dados tratados, notebook de analise e artefatos de saida.

## 2. Objetivo da analise

O principal objetivo e identificar padroes de empreendedorismo em Santa Catarina a partir da quantidade de estabelecimentos por municipio. Para isso, a analise realiza a leitura do arquivo Excel, padroniza os nomes das colunas, separa o campo de municipio em cidade e UF, ordena os registros pelo numero de estabelecimentos e calcula a participacao percentual de cada municipio no total. Com isso, torna-se possivel construir rankings, visualizar concentracao economica e apoiar interpretacoes exploratorias sobre os polos de maior dinamismo empresarial no estado.

## 3. Fonte dos dados

A base utilizada neste projeto vem de dados publicos do Mapa de Empresas, em arquivo Excel fornecido pelo usuario para analise. O schema considerado no notebook corresponde as colunas reais `[Municipio]` e `Estabelecimentos `, sem inventar atributos adicionais. A unica derivacao aplicada sobre o dado original e a separacao do campo de municipio em duas partes: `cidade` e `uf`, preservando a coerencia com o conteudo efetivamente disponivel na planilha.

## 4. Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

O projeto tambem utiliza a leitura de arquivos Excel via `pandas.read_excel`, com suporte da dependencia `openpyxl` no ambiente.

## 5. Estrutura do projeto

```text
.
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── outputs/
│   ├── graficos/
│   └── tabelas/
├── requirements.txt
└── README.md
```

Descricao resumida das pastas:

- `data/raw`: armazena o arquivo Excel original.
- `data/processed`: pode armazenar bases tratadas para reuso.
- `notebooks`: contem o notebook principal da analise exploratoria.
- `src`: funcoes auxiliares de limpeza, metricas e geracao de graficos.
- `outputs/graficos`: imagens geradas durante a analise.
- `outputs/tabelas`: rankings e tabelas exportadas em CSV.

## 6. Etapas da analise de dados

1. Carregamento do arquivo Excel com `pandas.read_excel`.
2. Normalizacao dos nomes das colunas, removendo colchetes e excessos de espaco.
3. Renomeacao das colunas para `municipio` e `estabelecimentos`.
4. Separacao de `municipio` em `cidade` e `uf` com base no padrao `Cidade - UF`.
5. Conversao da coluna `estabelecimentos` para tipo numerico.
6. Ordenacao dos dados em ordem decrescente pelo numero de estabelecimentos.
7. Calculo do ranking municipal.
8. Calculo do percentual que cada municipio representa no total.
9. Calculo da participacao acumulada dos 10 primeiros municipios.
10. Geracao de grafico de barras para os 15 municipios com maior numero de estabelecimentos.
11. Exportacao da tabela final para CSV em `outputs/tabelas/ranking_municipios.csv`.
12. Salvamento do grafico em `outputs/graficos/top_15_municipios.png`.

## 7. Principais insights encontrados

A analise foi estruturada para evidenciar, de forma objetiva, tres tipos principais de insight:

- quais municipios concentram o maior volume de estabelecimentos no estado;
- quanto cada municipio representa no total analisado;
- qual o nivel de concentracao economica observado quando se soma a participacao dos principais polos.

Em leituras desse tipo, normalmente o ranking evidencia forte concentracao nos maiores centros urbanos, enquanto municipios menores aparecem com menor participacao relativa. A participacao acumulada do top 10 ajuda a medir essa concentracao de maneira direta: quanto maior esse indicador, maior o peso dos principais municipios sobre o total estadual.

## 8. Como executar o projeto

1. Acesse a pasta do projeto.
2. Crie um ambiente virtual:

```bash
python -m venv .venv
```

3. Ative o ambiente virtual.

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Instale as dependencias:

```bash
pip install -r requirements.txt
```

5. Coloque o arquivo Excel em `data/raw/`, utilizando o nome esperado no notebook.
6. Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

7. Abra `notebooks/analise_empreendedorismo_sc.ipynb` e execute as celulas em sequencia.

Ao final, o projeto deve gerar:

- `outputs/tabelas/ranking_municipios.csv`
- `outputs/graficos/top_15_municipios.png`

## 9. Organizacao do repositorio

O repositorio foi organizado para separar claramente entrada, transformacao, analise e saida. O notebook centraliza a exploracao e a interpretacao dos resultados, enquanto a pasta `src` concentra funcoes reutilizaveis para limpeza e visualizacao. Essa estrutura facilita manutencao, reprodutibilidade e evolucao futura do projeto, inclusive para novas analises baseadas em outras recortes geograficos, periodos ou indicadores do mesmo conjunto de dados.
