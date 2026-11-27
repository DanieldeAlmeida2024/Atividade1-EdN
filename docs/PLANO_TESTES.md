# Plano de testes — Atividade1-EdN

- CT-01 Arquivos do exercício presentes.
- CT-02 Todos os scripts .py compilam sintaticamente via ast.parse, sem executar.
- CT-03 Comparar manualmente os exemplos do README com as saídas.
- CT-04 Testar dados inválidos quando especificado no enunciado.

Executar `python -m unittest discover -s tests -v`. Os casos estruturais CT-01 e CT-02 ficam em `test_documentacao.py`. CT-03 e CT-04 têm exemplos executados como subprocessos em `test_comportamento.py`.

Em CT-04, duas entradas distintas chegam ao terceiro valor: uma termina após dois inteiros e a outra fornece texto onde se espera um inteiro. Ambas terminam com código 1, mensagens em português que identificam a causa e nenhum resultado parcial.
