"""Testes comportamentais dos cinco exercícios, executáveis sem bibliotecas externas."""
import subprocess
import importlib.util
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

    def test_diferenca_reutilizavel_e_importavel_sem_ler_stdin(self):
        caminho = RAIZ / "calculadoraNumeroInteiro.py"
        spec = importlib.util.spec_from_file_location("diferenca_edn1", caminho)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        self.assertEqual(-10, modulo.diferenca_produtos(1, 2, 3, 4))
        self.assertEqual(28, modulo.diferenca_produtos(5, 6, 1, 2))
        self.assertEqual(-2, modulo.diferenca_produtos(-2, 3, -1, 4))
        self.assertEqual(10**60, modulo.diferenca_produtos(10**30, 10**30, 0, 5))
        for errado in (True, 1.0, None, "1"):
            with self.subTest(errado=errado), self.assertRaises(ValueError):
                modulo.diferenca_produtos(errado, 1, 1, 1)

    def test_cli_diferenca_rejeita_entrada_invalida_sem_traceback(self):
        for stdin in ("1\\n2\\n", "1\\n2\\na\\n4\\n"):
            with self.subTest(entrada=stdin):
                p = subprocess.run(
                    [sys.executable, str(RAIZ / "calculadoraNumeroInteiro.py")],
                    input=stdin, text=True, capture_output=True, timeout=5, cwd=RAIZ
                )
                self.assertNotEqual(0, p.returncode)
                self.assertIn("Erro:", p.stderr)
                self.assertNotIn("Traceback", p.stderr)

    def test_diferenca_com_entradas(self):
        self.assertTrue(
            executar("calculadoraNumeroInteiro.py", "1\n2\n3\n4\n").endswith("DIFERENCA = -10")
        )
        self.assertTrue(
            executar("calculadoraNumeroInteiro.py", "5\n6\n1\n2\n").endswith("DIFERENCA = 28")
        )


if __name__ == "__main__":
    unittest.main()
