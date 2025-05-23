class VerticeRegistro:
    def __init__(self, codigo, longitude, latitude, altitude, vante, azimute, distancia, confrontacao):
        self.codigo = codigo
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.vante = vante
        self.azimute = azimute
        self.distancia = distancia
        self.confrontacao = confrontacao

    def to_dict(self):
        return {
            "Vértice": self.codigo,
            "Longitude": self.longitude,
            "Latitude": self.latitude,
            "Altitude (m)": self.altitude,
            "Vante": self.vante,
            "Azimute": self.azimute,
            "Distância (m)": self.distancia,
            "Confrontações": self.confrontacao
        }
