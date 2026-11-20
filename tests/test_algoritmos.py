import unittest

from src.guloso import troco_guloso


class TestTrocoGuloso(unittest.TestCase):

    def test_troco_185_centavos(self):
        resultado = troco_guloso(185)

        self.assertEqual(
            resultado,
            {100: 1, 50: 1, 25: 1, 10: 1}
        )

    def test_quantidade_minima_de_moedas(self):
        resultado = troco_guloso(185)

        quantidade = sum(resultado.values())

        self.assertEqual(quantidade, 4)

    def test_troco_de_100_centavos(self):
        resultado = troco_guloso(100)

        self.assertEqual(resultado, {100: 1})

    def test_troco_de_75_centavos(self):
        resultado = troco_guloso(75)

        self.assertEqual(resultado, {50: 1, 25: 1})

    def test_valor_zero(self):
        resultado = troco_guloso(0)

        self.assertEqual(resultado, {})

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            troco_guloso(-10)

    def test_moedas_fora_de_ordem(self):
        with self.assertRaises(ValueError):
            troco_guloso(30, (1, 10, 25))

    
    def test_exemplo_em_que_guloso_nao_e_otimo(self):
        resultado = troco_guloso(6, (4, 3, 1))

        quantidade = sum(resultado.values())

        self.assertEqual(quantidade, 3)

if __name__ == "__main__":
    unittest.main()
