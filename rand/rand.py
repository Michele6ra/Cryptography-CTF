import binascii


rand1= "63-3b-6d-07-65-1a-09-31-7a-4f-b4-aa-ef-3f-7a-55-d0-33-93-52-1e-81-fb-63-11-26-ed-9e-8e-a7-10-f6-63-9d-eb-92-90-eb-76-0b-90-5a-eb-b4-75-d3-a1-cf-d2-91-39-c1-89-32-84-22-12-4e-77-57-4d-25-85-98"
rand2= "92-05-d8-b5-fa-85-97-b6-22-f4-bd-26-11-cf-79-8c-db-4a-28-27-bb-d3-31-56-74-16-df-cb-f5-61-a7-9d-18-c2-63-92-f1-cb-c3-6d-2b-77-19-aa-21-07-8e-fe-8b-1a-4f-7d-70-6e-a4-7b-c8-68-30-43-12-50-30-1e"


rand1_pulita=rand1.split("-")
rand2_pulita=rand2.split("-")

rand1_bin  = binascii.unhexlify("".join(rand1_pulita))
rand2_bin  = binascii.unhexlify("".join(rand2_pulita))

'''for elemento1, elemento2  in zip(rand1_bin, rand2_bin):
    k1=k1+(elemento1 | elemento2)
    k2=k2+(elemento1 & elemento2)


for el1, el2 in zip(k1, k2):
    flag=flag+(el1 ^ el2)
'''
rand1_bin1 = int.from_bytes(rand1_bin, byteorder='big')
rand2_bin1 = int.from_bytes(rand2_bin, byteorder='big')

k1= rand1_bin1 | rand2_bin1
k2= rand1_bin1 & rand2_bin1
flag = k1 ^ k2
flag2 = hex(flag)


stringa_con_dash = '-'.join([flag2[i:i+2] for i in range(0, len(flag2), 2)])
print(stringa_con_dash)
