class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama
    
    def perkenalan(self):
        print(self.nama, "Beragama", self.agama )

class Islam(Agama):
    def __init__(self, nama, agama, sholat):
        Agama.__init__(self, nama, agama)
        self.sholat = sholat

class katholik(Agama):
    def __init__(self, nama, agama, sembayang):
        Agama.__init__(self, nama, agama)
        self.sembayang = sembayang

hisyam = Islam('kevin', 'Islam', 'Sholat')
hisyam.perkenalan()
print(f'{hisyam.nama} beribadah dengan melakukan {hisyam.sholat}')

jupai = katholik('jupai', 'Budha', 'Sembayang')
jupai.perkenalan()
print(f'{jupai.nama} beribadah dengan melakukan {jupai.sembayang}')