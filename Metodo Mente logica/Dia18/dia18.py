# debugging
# identificar erros no codigo ou entender como o codigo esta funcionando

# pbd python debugger
import pdb
import unittest

def dividir(a, b):
    print(f"Dividindo {a} por {b}")
    if b == 0:
        print("Divisão por 0")
        return None

    resultado = a/b
    print(f"O resultado da divisão é {resultado}")
    return resultado


dividir(10, 2)
dividir(10, 0)


def dividir2(a, b):

    #pdb.set_trace()

    if b == 0:
        return None

    resultado = a/b
    return resultado


dividir2(10, 0)


# testes unitarios

def soma(a, b):
    return a + b


class TesteSomar(unittest.TestCase):
    def test_somar_positivos(self):
        self.assertEqual(soma(2, 3), 5)
    def test_somar_negativos(self):
        self.assertEqual(soma(-1, -3), -4)
    def test_somar_zero(self):
        self.assertEqual(soma(2, 0), 2)


if __name__ == "__main__":
    print("Iniciando testes de soma...")
    unittest.main()
