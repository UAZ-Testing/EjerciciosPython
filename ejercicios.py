class Ejercicios:
    def validar_numero(self, numero):
        return isinstance(numero, (int, float))

    # Ejercicio 1
    def get_sueldo_total(self, sueldo_base, venta_1, venta_2, venta_3):
        return sueldo_base + 0.10 * venta_1 + 0.10 * venta_2 + 0.10 * venta_3

    # Ejercicio 3
    def get_promedio_parciales(self, examen_1, examen_2, examen_3):
        return (examen_1 + examen_2 + examen_3) / 3

    # Ejercicio 5
    def get_pesos_dolar(self, pesos, valor_dolar):
        return round(pesos / valor_dolar, 2)

    # Ejercicio 7
    def get_area_circulo(self, radio):
        return round(3.14 * radio**2, 2)

    # Ejercicio 9
    def get_cubo_numero(self, numero):
        return numero**3

    # Ejercicio 2
    def get_pago_con_descuento(self, pago):
        if self.validar_numero(pago):
            return pago - pago * 0.15
        else:
            return 'datos inválidos'

    # Ejercicio 4
    def get_porcentaje_hm(self, hombres, mujeres):
        if self.validar_numero(hombres) and self.validar_numero(mujeres):
            porc_hombres = hombres * 100 / (hombres + mujeres)
            porc_mujeres = mujeres * 100 / (hombres + mujeres)
            return 'Hombres: %f%%, Mujeres: %f%%' \
                   % (porc_hombres, porc_mujeres)
        else:
            return 'datos inválidos'

    # Ejercicio 6
    def get_incremento(self, pago):
        if self.validar_numero(pago):
            return pago + pago * 0.25
        else:
            return 'datos inválidos'

    # Ejercicio 8
    def get_metros_a_pulgadas_pies(self, metros):
        if self.validar_numero(metros):
            pies = metros * 3.28084
            pulgadas = metros * 39.3701
            return 'Pies: %g, Pulgadas: %g' % (pies, pulgadas)
        else:
            return 'datos inválidos'

    # Ejercicio 10
    def get_kg_a_gr_libras_toneladas(self, kilos):
        if self.validar_numero(kilos):
            gramos = kilos * 1000
            libras = kilos * 2.20462
            toneladas = kilos / 1000
            return 'Gramos: %g, Libras: %g, Toneladas: %g' \
                   % (gramos, libras, toneladas)
        else:
            return 'datos inválidos'
