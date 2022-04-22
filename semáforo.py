
flag = True

while flag == True:
  color = input('Escriba el color del semáforo (rojo, verde, amarillo)')
  if color == 'rojo' or color == 'amarillo' or color == 'verde':
    flag = False
  else:
    print ('Color equivocado')

if color == 'rojo':
  print('No, No, No, no puedes pasar.')

if color == 'amarillo':
  print('Pasar pero con mucho cuidado.')
  
if color == 'verde':
  print('Puedes pasar.. bieeeennnn')
