class Avtomobil:
    def __init__(self, model, yil, tezlik):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def malumot(self):
        """Avtomobil ma’lumotlarini qaytaradi"""
        return f"Model: {self.model}, Yil: {self.yil}, Tezlik: {self.tezlik} km/soat"

    def tezlik_oshir(self, qiymat):
        """Tezlikni oshiradi"""
        self.tezlik += qiymat
        return f"Yangi tezlik: {self.tezlik} km/soat"



avto1 = Avtomobil("Chevrolet Malibu", 2022, 120)
print(avto1.malumot())

print(avto1.tezlik_oshir(20))
print(avto1.malumot())
