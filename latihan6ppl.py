# jenis enkapulasi : public , protected , private

# membuat public class

from ast import alias
from mimetypes import init


class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi;
        
        
#instansisasi
segitiga_besar = segitiga(100, 50)

print("ini adalah public class")
print(f'alas : {segitiga_besar.alas}')
print(f'tinggi : {segitiga_besar.tinggi}')
print(f'luas : {segitiga_besar.luas}\n')        


#membuat protected class

class mobil:
    def __init__(self, merk):
        self._merk = merk 
        
class mobilefwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear
        
    def pamer(self):
        print(f'ini adalah mobil {self._merk} dengan total gear nya {self._total_gear}\n')
        
        

#instansiasi
print("ini adalah protected class")
ferrari = mobilefwan('ferrari',8)
ferrari.pamer() 




# membuat private class

class motor:
    def __init__(self, merk):
        self.__merk = merk
        
    def tampilkan_merk(self):
        print(f'merk motornya : {self.__merk}')
        
        
#instansiasi
print("ini adalah private class")
moge = motor('harley')
moge.tampilkan_merk()
       