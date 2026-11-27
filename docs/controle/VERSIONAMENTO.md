> **Referência histórica (11/11/2026):** os resultados atuais de CI e as regras vigentes constam no README e em `docs/PLANO_TESTES.md`. Casos não executados neste documento não devem ser anunciados como aprovados.

# Controle documental — Atividade1-EdN

Versão **1.0.0**, 11/11/2026. Código analisado: `701df1ea81e9d1d378fff2164c5f2218e245b3ab`. Histórico: criação dos documentos de projeto, dois UML e casos de teste rastreados por script.

| ID | Artefato | Versão |
|---|---|---|
| Atividade1-EdN-PROJ | [Especificação](../projeto/ESPECIFICACAO.md) | 1.0.0 |
| Atividade1-EdN-UML | [Diagramas](../uml/README.md) | 1.0.0 |
| Atividade1-EdN-TEST | [Plano de testes](../testes/PLANO_DE_TESTES.md) | 1.0.0 |

**MAJOR** quando mudar entrada/saída de programa; **MINOR** para exercícios/funcionalidades novos; **PATCH** para correção editorial. Atualize IDs de testes quando alterar regras.

## Reconciliação documental de 14/11/2026

Recuperada modelagem específica de cada script e UML, com indicação explícita de que a revisão anterior é histórica. Preservados código, fixtures e testes já aprovados da main. O CI vigente, e não a matriz histórica, comprova execução.

## Revisão 1.0.1 do plano vigente · 27/11/2026

CT-04 agora distingue entrada incompleta de valor inválido na calculadora de diferença. Python 3.11.9 executou nove testes em `6cb7143729da996b485d59c390ea341b7f0a3a47`, além dos cinco exemplos de terminal.
