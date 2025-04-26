#PENENTUAN PH ASAM BASA 
print('PENENTUAN PH AASAM BASA')
print('..................')
nilai=int(input('Nilai PH = '))

if nilai>=11:
   print('Basa Kuat')
elif nilai>=9:
   print('Basa Lemah')
elif nilai>=8:
   print('Basa Sangat Lemah')
elif nilai>=7:
   print('Netral')
elif nilai>=6:
   print('Asam Sangat Lemah')
elif nilai>=4:
   print('Asam Lemah')
else:
   print('Asam Kuat')
