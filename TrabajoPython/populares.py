class Popular:
    def __init__(self, mes, estrellas, cantidad):
        self.mes = mes
        self.estrellas = estrellas
        self.cantidad = cantidad

    def __str__(self):
        res = f"┣━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━━━┫\n" \
              f"┃   {str(self.mes):<2}  ┃     {str(self.estrellas):<2}    ┃      {str(self.cantidad):<6} ┃"
        return res
