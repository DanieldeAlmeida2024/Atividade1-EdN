# Variáveis, cálculos e saídas fixas em Python

**Versão do documento:** 1.0.0 | **Data:** 11/11/2026 | **Commit auditado:** `701df1ea81e9d1d378fff2164c5f2218e245b3ab` | **Estado:** análise estática, testes de execução ainda não confirmados.

## Contexto de engenharia
Este repositório contém 5 exercícios Python independentes, executados diretamente no terminal. Cada arquivo representa uma competência distinta; não foi introduzida uma arquitetura de microserviços ou aplicação web artificial.

## Inventário por arquivo e contrato
| Arquivo de origem | Comportamento implementado | Regra ou exemplo de aceitação |
|---|---|---|
| `saudacao.py` | Imprime Hello World! | stdout exatamente Hello World! |
| `calculadoraSoma.py` | Exercício de soma entre variáveis | Conferir parcelas/resultados dos literais |
| `calculadoraNumeroInteiro.py` | Operações e tipos inteiros | Resultado correto sem conversão implícita indesejada |
| `calculadoraDeDimensao.py` | Volume retangular 12 × 14 × 20 cm | Volume 3360 cm³ |
| `calculadoraPrecoTotalCompra.py` | Cadeira Infantil: R$12,40 × 3 | Total R$37,20 com duas casas |

## Decisões e limitações observadas
Os programas não aceitam entrada e cada um imprime direto. Não são APIs ou classes de domínio; não há validação de valores negativos nem persistência.

## Como executar
```powershell
python calculadoraDeDimensao.py
python -m unittest discover -s tests -v
```

O segundo comando valida principalmente documentação existente; ele não substitui testes de saídas dos scripts. Para refatorar, primeiro isole cálculos em funções de Python com parâmetros explícitos e preserve os exemplos antes/depois.
