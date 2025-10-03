import tkinter as tk
from Calculadora import Calculadora

class CalculadoraTK:

    def __init__(self, calculadora):
        self.calculadora = calculadora
        self.ventana, self.pantalla = self._crear_interfaz()

    def _crear_interfaz(self):
        # creamos la ventana y le damos un título y un tamaño
        ventana = tk.Tk()
        ventana.title('La Calculadora de Código Pitón')
        ventana.geometry('700x700')

        # configuramos un grid de 5 x 5
        for i in range(0, 5):
            ventana.rowconfigure(i, weight=10)
            ventana.columnconfigure(i, weight=10, uniform='grupo')

        # pantalla
        pantalla = tk.Label(ventana, text='0', anchor=tk.E, relief='sunken', background='#ffffff',
                            font=('Helvetica', 24), padx=15)
        pantalla.grid(column=0, row=0, columnspan=5, padx=5, pady=5, sticky='nesw')

        # botones
        botones_digito = [tk.Button(ventana, text=digito, command=lambda x=digito: self.presionar_digito(x))
                          for digito in '.0123456789']
        botones_operador = [tk.Button(ventana, text=operador, command=lambda x=operador: self.presionar_operador(x))
                            for operador in '*/+-']
        boton_cambio_signo = tk.Button(ventana, text='±', command=lambda: self.presionar_operador('s'))
        boton_raiz = tk.Button(ventana, text='√', command=lambda: self.presionar_operador('r'))
        boton_calcular = tk.Button(ventana, text='=', command=self.presionar_calcular)
        boton_reset = tk.Button(ventana, text='AC', command=self.presionar_reset)

        # fuente
        botones_todos = botones_digito + botones_operador + [boton_cambio_signo, boton_raiz, boton_calcular, boton_reset]
        for boton in botones_todos:
            boton.config(font=('Helvetica', 17))

        # ubicación en cuadrícula
        botones_cuadricula = botones_digito[0:2][::-1] + [boton_cambio_signo] + botones_digito[2:]
        for fila in range(0, 4):
            for columna in range(0, 3):
                botones_cuadricula[3 * (3 - fila) + columna].grid(row=fila + 1, column=columna, padx=5, pady=5,
                                                                  sticky='nesw')

        boton_raiz.grid(row=1, column=3, padx=5, pady=5, sticky='nesw')
        boton_reset.grid(row=1, column=4, padx=5, pady=5, sticky='nesw')

        iterador = iter(botones_operador[0:4])
        for fila in (2, 3):
            for columna in (3, 4):
                next(iterador).grid(row=fila, column=columna, padx=5, pady=5, sticky='nesw')

        boton_calcular.grid(row=4, column=3, padx=5, pady=5, sticky='nesw', columnspan=2)

        return ventana, pantalla

    def actualizar_pantalla(self, valor, eliminar_ceros_derecha=False):
        valor_pantalla = str(valor)
        if eliminar_ceros_derecha:
            valor_pantalla = valor_pantalla.rstrip('0').rstrip('.')
        self.pantalla.configure(text=valor_pantalla)

    def presionar_digito(self, digito):
        self.calculadora.introducir_digito(digito)
        self.actualizar_pantalla(self.calculadora.valor_actual())

    def presionar_operador(self, operador):
        self.calculadora.introducir_operador(operador)
        self.actualizar_pantalla(self.calculadora.valor_actual(), True)

    def presionar_calcular(self):
        self.calculadora.calcular()
        self.actualizar_pantalla(self.calculadora.valor_actual(), True)

    def presionar_reset(self):
        self.calculadora.reset()
        self.actualizar_pantalla(self.calculadora.valor_actual())

    def mostrar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    calc = Calculadora()
    app = CalculadoraTK(calc)
    app.mostrar()
