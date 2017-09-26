# coding=utf-8

import unittest
from ejercicios import Ejercicios


class EjerciciosTest(unittest.TestCase):
    # Test fixtures

    def setUp(self):
        self.ejercicios = Ejercicios()

    def tearDown(self):
        pass

    # Pruebas del ejercicio 1
    def test_base500_v1_200_v2_300_v3_500(self):
        self.assertEqual(self.ejercicios.get_sueldo_total(
            500, 200, 300, 500), 600)

    def test_base1000_v1_20_v2_1000_v3_40(self):
        self.assertEqual(self.ejercicios.get_sueldo_total(
            1000, 20, 1000, 40), 1106)

    def test_base60_v1_500_v2_600_v3_700(self):
        self.assertEqual(self.ejercicios.get_sueldo_total(
            60, 500, 600, 700), 240)

    # Pruebas del ejercicio 3
    def test_ex1_8_ex2_9_ex3_10(self):
        self.assertEqual(self.ejercicios.get_promedio_parciales(8, 9, 10), 9)

    def test_ex1_2_ex2_6_ex3_1(self):
        self.assertEqual(self.ejercicios.get_promedio_parciales(2, 6, 1), 3)

    def test_ex1_4_ex2_8_ex3_6(self):
        self.assertEqual(self.ejercicios.get_promedio_parciales(4, 8, 6), 6)

    # Pruebas del ejercicio 5
    def test_800_pesos_24_valor_dolar(self):
        self.assertEqual(self.ejercicios.get_pesos_dolar(800, 24), 33.33)

    def test_1850_pesos_18_valor_dolar(self):
        self.assertEqual(self.ejercicios.get_pesos_dolar(1850, 18), 102.78)

    def test_720_pesos_12_valor_dolar(self):
        self.assertEqual(self.ejercicios.get_pesos_dolar(720, 12), 60.0)

    # Pruebas del ejercicio 7
    def test_radio_10(self):
        self.assertEqual(self.ejercicios.get_area_circulo(10), 314)

    def test_radio_80(self):
        self.assertEqual(self.ejercicios.get_area_circulo(80), 20096)

    def test_radio_7(self):
        self.assertEqual(self.ejercicios.get_area_circulo(7), 153.86)

    # Pruebas del ejercicio 9
    def test_numero_3(self):
        self.assertEqual(self.ejercicios.get_cubo_numero(3), 27)

    def test_numero_9(self):
        self.assertEqual(self.ejercicios.get_cubo_numero(80), 512000)

    def test_numero_10(self):
        self.assertEqual(self.ejercicios.get_cubo_numero(7), 343)

    # Pruebas del ejercicio 2

    def test_e2_descuento_1(self):
        self.assertEqual(self.ejercicios.get_pago_con_descuento(100), 85)

    def test_e2_descuento_2(self):
        self.assertEqual(self.ejercicios.get_pago_con_descuento(2), 1.7)

    def test_e2_descuento_3(self):
        self.assertEqual(self.ejercicios.get_pago_con_descuento('a'),
                         'datos inválidos')

    # Pruebas del ejercicio 4
    def test_e4_porcentaje_1(self):
        self.assertEqual(self.ejercicios.get_porcentaje_hm(10, 5),
                         'Hombres: 66.666667%, Mujeres: 33.333333%')

    def test_e4_porcentaje_2(self):
        self.assertEqual(self.ejercicios.get_porcentaje_hm(23, 28),
                         'Hombres: 45.098039%, Mujeres: 54.901961%')

    def test_e4_porcentaje_3(self):
        self.assertEqual(self.ejercicios.get_porcentaje_hm('a', 28),
                         'datos inválidos')

    # Pruebas del ejercicio 6
    def test_e6_incremento_1(self):
        self.assertEqual(self.ejercicios.get_incremento(1900), 2375.0)

    def test_e6_incremento_2(self):
        self.assertEqual(self.ejercicios.get_incremento(5812), 7265.0)

    def test_e6_incremento_3(self):
        self.assertEqual(self.ejercicios.get_incremento('a'),
                         'datos inválidos')

    # Pruebas del ejercicio 8
    def test_e8_conversion_metros_1(self):
        self.assertEqual(self.ejercicios.get_metros_a_pulgadas_pies(1),
                         'Pies: 3.28084, Pulgadas: 39.3701')

    def test_e8_conversion_metros_2(self):
        self.assertEqual(self.ejercicios.get_metros_a_pulgadas_pies(150),
                         'Pies: 492.126, Pulgadas: 5905.52')

    def test_e8_conversion_metros_3(self):
        self.assertEqual(self.ejercicios.get_metros_a_pulgadas_pies('a'),
                         'datos inválidos')

    # Pruebas del ejercicio 10
    def test_e10_conversion_kilos_1(self):
        self.assertEqual(self.ejercicios.get_kg_a_gr_libras_toneladas(10),
                         'Gramos: 10000, Libras: 22.0462, Toneladas: 0.01')

    def test_e10_conversion_kilos_2(self):
        self.assertEqual(self.ejercicios.get_kg_a_gr_libras_toneladas(500),
                         'Gramos: 500000, Libras: 1102.31, Toneladas: 0.5')

    def test_e10_conversion_kilos_3(self):
        self.assertEqual(self.ejercicios.get_kg_a_gr_libras_toneladas('a'),
                         'datos inválidos')


# Ejecuta las pruebas implementadas
if __name__ == '__main__':  # pragma: no cover
    unittest.main()
