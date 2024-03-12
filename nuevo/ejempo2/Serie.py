class Serie:
    def __init__(self, titulo, genero, calificacion, horas_estimadas=10, status='Sin reproducir'):
        self._titulo = titulo
        self._genero = genero
        self._calificacion = calificacion
        self._horas_estimadas = horas_estimadas
        self._status = status

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        self._genero = valor

    @property
    def calificacion(self):
        return self._calificacion

    @calificacion.setter
    def calificacion(self, valor):
        if 0 <= valor <= 10:
            self._calificacion = valor
        else:
            raise ValueError("La calificación debe estar entre 0 y 10.")

    @property
    def horas_estimadas(self):
        return self._horas_estimadas

    @horas_estimadas.setter
    def horas_estimadas(self, valor):
        self._horas_estimadas = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        self._status = valor

    def reproducir(self):
        return "Reproduciendo serie..."

    def agregar_a_mi_lista(self):
        return "Agregado a mi lista de series."

    def marcar_como_completada(self):
        self._status = 'Completada'
        return f"La serie {self._titulo} ha sido marcada como completada."

    def calificar(self, nueva_calificacion):
        self.calificacion = nueva_calificacion
        return f"La serie {self._titulo} ha sido calificada con {self._calificacion}."
    def __init__(self, titulo, genero, calificacion, horas_estimadas=10, status='Sin reproducir'):
        self._titulo = titulo
        self._genero = genero
        self._calificacion = calificacion
        self._horas_estimadas = horas_estimadas
        self._status = status

    def reproducir(self):
        self._status = 'Reproduciendo'
        return f"Reproduciendo {self._titulo}..."

    def agregar_a_mi_lista(self):
        return f"{self._titulo} agregado a mi lista."

    def marcar_como_completada(self):
        self._status = 'Completada'
        return f"{self._titulo} ha sido marcada como completada."

    def calificar(self, calificacion):
        self._calificacion = calificacion
        return f"{self._titulo} ha sido calificada con {self._calificacion}."
