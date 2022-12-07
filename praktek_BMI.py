class Input():
    def __init__(self):
        print("=======================================")
        
        self.tinggi_badan = int(input("masukan tinggi badan anda = "))
        self.berat_badan = int(input("masukan berat badan anda = "))
        self.umur = int(input("masukan umur anda = "))
        self.nama = input("masukan nama anda = " )
        self.jenis_kelamin = input("masukan jenis kalamin anda = ")
        self.tinggi_badan = self.tinggi_badan/100
        
    
        
class perkenalan:
    def nama(self):
        print('NAMA ANDA = ',obj1.nama)
    def rumus(self):
        print('NILAI BMI anda = ', obj1.berat_badan / (obj1.tinggi_badan**2)  ) 
    def rumus1(self):
        print(obj1.berat_badan / (obj1.tinggi_badan**2) )
    
    
    
             
obj1 = Input()
obj2 = perkenalan()
obj2.nama()
obj2.rumus()


if obj1.berat_badan / (obj1.tinggi_badan**2)  < 18.5:
	print('Berat badan anda kurang ')
elif  obj1.berat_badan / (obj1.tinggi_badan**2) > 18.5 and obj1.berat_badan / (obj1.tinggi_badan**2)  < 24.9:
	print('Berat badan anda normal')
elif  obj1.berat_badan / (obj1.tinggi_badan**2) > 25 and  obj1.berat_badan / (obj1.tinggi_badan**2) < 29.9:
	print('Anda kelebihan berat badan')
elif  obj1.berat_badan / (obj1.tinggi_badan**2) > 30:
	print('Anda obesitas')


print("=======================================")







 

