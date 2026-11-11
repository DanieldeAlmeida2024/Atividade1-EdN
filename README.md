# Atividade1-EdN — atividades Python

Exercícios iniciais de Python: saudação, soma, dimensões, preço de compra e diferença de produtos.

## Requisitos
Python 3.10+ e terminal local; não há serviço HTTP ou banco de dados obrigatório nesta atividade.

## Executar
```bash
python saudacao.py
```

Cada script é um exercício independente. Outros arquivos existentes: `saudacao.py, calculadoraSoma.py, calculadoraDeDimensao.py, calculadoraPrecoTotalCompra.py, calculadoraNumeroInteiro.py`.

## Testes
```bash
python -m unittest discover -s tests -v
```

Os testes adicionados verificam presença de arquivos, documentação e sintaxe de código; para validar comportamento, é necessário comparar a entrada e saída de cada exercício com o enunciado original.

## Documentação
[Requisitos](docs/REQUISITOS.md) · [Arquitetura](docs/ARQUITETURA.md) · [UML](docs/UML.puml) · [Plano de testes](docs/PLANO_TESTES.md) · [Guia de IA](AGENTS.md).

---

## Enunciados anteriores preservados

## Atividade Prática 01
### 1- Programa de Saudação

Crie um programa que imprima a mensagem "Hello, world!" na tela.

### 2- Calculadora de Soma

Desenvolva um programa que soma dois números.
Use as variáveis numero1 = 12 e numero2 = 14. 
O programa deve calcular a soma e exibir o resultado.

### 3- Calculadora de Volume

Crie um programa que calcule o volume de uma caixa retangular. Use as seguintes dimensões:
Comprimento: 12 cm
Largura: 14 cm
Altura: 20 cm 
O programa deve calcular o volume e exibir o resultado em cm³.

### 4- Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

### 5- Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

## Documentação específica (v1.0.0)

[Especificação](docs/projeto/ESPECIFICACAO.md) · [Diagramas](docs/uml/README.md) · [Plano de testes](docs/testes/PLANO_DE_TESTES.md) · [Versões](docs/controle/VERSIONAMENTO.md)
