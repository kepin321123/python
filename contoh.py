# Mendapatkan informasi dari input pengguna
berat_badan = int(input('Berat Badan (kg) : '))
tinggi_badan = int(input('Tinggi Badan (cm) : '))
umur = int(input('Masukan umur anda : '))

# Konversi tinggi badan ke meter
tinggi_badan = tinggi_badan/100

# Rumus BMI = berat badan(kg) / (tinggi badan(m) ^ 2)
nilai_bmi = berat_badan / (tinggi_badan**2)

print('Nilai BMI anda : ',nilai_bmi)
# Sistem logika dengan if else
if nilai_bmi < 18.5:
	print('Berat badan anda kurang ')
elif nilai_bmi > 18.5 and nilai_bmi < 24.9:
	print('Berat badan anda normal')
elif nilai_bmi > 25 and nilai_bmi < 29.9:
	print('Anda kelebihan berat badan')
elif nilai_bmi > 30:
	print('Anda obesitas')