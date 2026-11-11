# Plano de testes — Atividade1-EdN

**Versão do documento:** 1.0.0 | **Data:** 11/11/2026 | **Commit auditado:** `701df1ea81e9d1d378fff2164c5f2218e245b3ab` | **Estado:** análise estática, testes de execução ainda não confirmados.

Os IDs abaixo são **casos propostos**; o repositório tem `tests/test_documentacao.py`, mas não uma suíte dedicada cobrindo os resultados de todos esses scripts. Não marcar como aprovado sem registrar stdout/entrada por commit.

| Caso | Script | Procedimento e resultado esperado | Situação |
|---|---|---|---|
| EDT-01 | `saudacao.py` | stdout exatamente Hello World! | Planejado |
| EDT-02 | `calculadoraSoma.py` | Conferir parcelas/resultados dos literais | Planejado |
| EDT-03 | `calculadoraNumeroInteiro.py` | Resultado correto sem conversão implícita indesejada | Planejado |
| EDT-04 | `calculadoraDeDimensao.py` | Volume 3360 cm³ | Planejado |
| EDT-05 | `calculadoraPrecoTotalCompra.py` | Total R$37,20 com duas casas | Planejado |

## Testes negativos
N-01: executar scripts com entrada não numérica quando houver `input()` e registrar exceção/mensagem. N-02: valores zero e negativos conforme contrato de cada exercício. N-03: verificar formatação local (vírgula decimal, unidade e R$). N-04: comparar saída Python em duas versões suportadas e documentar diferenças.

## Evidências e execução
Rodar `python calculadoraDeDimensao.py` para o exemplo principal, depois cada arquivo individualmente. Testes automáticos futuros devem usar `subprocess.run` e capturar saída. Registrar: SHA, Python version, entrada, stdout, expected, status. A mera presença de um arquivo de teste documental não comprova a aritmética.
