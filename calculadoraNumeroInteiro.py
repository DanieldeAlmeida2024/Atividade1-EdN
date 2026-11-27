"""Diferença de produtos de quatro números inteiros (atividade 1)."""


def diferenca_produtos(a: int, b: int, c: int, d: int) -> int:
    """Calcula A × B − C × D, inclusive para inteiros negativos."""
    if any(type(valor) is not int for valor in (a, b, c, d)):
        raise ValueError("A, B, C e D devem ser números inteiros.")
    return a * b - c * d


def main() -> None:
    try:
        valores = [
            int(input(f"Digite o valor de {letra}:"))
            for letra in ("A", "B", "C", "D")
        ]
    except EOFError:
        raise SystemExit("Erro: entrada encerrada antes dos quatro números inteiros.") from None
    except ValueError:
        raise SystemExit("Erro: valor inválido. Informe quatro números inteiros.") from None
    print(f"DIFERENCA = {diferenca_produtos(*valores)}")


if __name__ == "__main__":
    main()
