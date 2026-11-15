# EDN01-INT-02 — Entradas inteiras e unidade testável

**Data:** 15/11/2026 · Arquivo `calculadoraNumeroInteiro.py`

## Problema
O exercício dependia de quatro chamadas `input()` executadas no import e gerava traceback para entrada encerrada ou não numérica, dificultando execução por outro módulo e diagnóstico em CI.

## Contrato novo
- `diferenca_produtos(a,b,c,d)` é uma função pura e rejeita strings, booleanos e valores não inteiros.
- Aceita inteiros negativos e inteiros grandes, conforme a aritmética inteira do Python.
- O script só lê stdin em `main()`; para dados válidos, mantém exatamente a linha `DIFERENCA = ...`.
- Em EOF ou erro de conversão, encerra com mensagem `Erro:` e código não zero, sem traceback.
- Casos novos importam a função e executam o script com entrada incompleta.

**Limites:** não foram introduzidas dependências ou serviço. Os demais exercícios preservam os valores fixos do enunciado; não se transforma a atividade didática em sistema financeiro.
