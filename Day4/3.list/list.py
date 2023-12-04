# fruits = ['pear', 'apple', 'orange']

statesOfAmerica = ['Delaware', 'Pennsylvania', 
'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 
'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 
'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 
'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 
'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 
'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia',
 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana',
  'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona',
   'Alaska', 'Hawaii']

print(statesOfAmerica[0]) # 리스트에 적힌 것중 첫번째를 출력한다
print(statesOfAmerica[-3]) # 뒤에서 4번째를 가져온다.

statesOfAmerica[1] = 'Pencilvania'
print(statesOfAmerica) # 윗줄에서 두번째 항목을 수정한 대로 나온다.

statesOfAmerica.append('Angelaland')
print(statesOfAmerica) # 리스트에 안젤라랜드를 추가해서 나온다.

statesOfAmerica.extend(['Souel','Busan','Daegu'])
print(statesOfAmerica) # 리스트에 리스트를 추가한다.

# 프로그래밍은 오픈북 시험과 같다. 외울 생각보다 찾아보는게 현명하다!