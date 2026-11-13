"""Testes comportamentais dos cinco exercícios, executáveis sem bibliotecas externas."""
import subprocess
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def executar(nome, entrada=""):
    resultado = subprocess.run(
        [sys.executable, str(RAIZ / nome)],
        input=entrada,
        text=True,
        capture_output=True,
        timeout=5,
        check=False,
        cwd=RAIZ,
    )
    if resultado.returncode != 0:
        raise AssertionError(f"{nome} falhou: {resultado.stderr}")
    return resultado.stdout.strip()


class TestesComportamento(unittest.TestCase):
    def test_saudacao(self):
        self.assertEqual(executar("saudacao.py"), "Hello World!")

    def test_soma(self):
        self.assertEqual(executar("calculadoraSoma.py"), "Resultado da soma: 26")

    def test_volume(self):
        self.assertEqual(
            executar("calculadoraDeDimensao.py"),
            "O volume da caixa retangular é: 3360 cm³",
        )

    def test_preco_total(self):
        saida = executar("calculadoraPrecoTotalCompra.py")
        self.assertIn("Preço Total da Compra: R$ 37.20", saida)
        self.assertIn("Quantidade Comprada: 3 unidades", saida)

    def test_diferenca_com_entradas(self):
        self.assertEqual(
            executar("calculadoraNumeroInteiro.py", "1\n2\n3\n4\n").splitlines()[-1],
            "DIFERENCA = -10",
        )
        self.assertEqual(
            executar("calculadoraNumeroInteiro.py", "5\n6\n1\n2\n").splitlines()[-1],
            "DIFERENCA = 28",
        )


if __name__ == "__main__":
    unittest.main()
