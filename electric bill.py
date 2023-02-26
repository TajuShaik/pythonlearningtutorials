# electric bill

ebu=int(input('enter no.of units:'))
if ebu<=100:
    a1=(ebu*3.46)+(ebu*1.45)+100
    a2=a1+((a1/100)*16)
    print('Electricity bill of Andra pradesh')
    print(30*'=')
    print('Consumer name:****')
    print ('bill is :',a2)
elif ebu>=101 and ebu<=300:
    b1=(100*3.46)+((ebu-100)*7.43)+100+(ebu*1.45)
    b2=b1+((b1/100)*16)
    print('Electricity bill of Andra pradesh')
    print(30*'=')
    print('Consumer name:****')
    print ('bill is :',b2)
elif ebu>=301 and ebu<=500:
    c1=(100*3.46)+(200*7.43)+((ebu-300)*10.32)+100+(ebu*1.45)
    c2=c1+((c1/100)*16)
    print('Electricity bill of Andra pradesh')
    print(30*'=')
    print('Consumer name:****')
    print ('bill is rupees :',c2)
elif ebu>=501:
    d1=(100*3.46)+((ebu-500)*11.71)+(200*7.43)+(300*(10.32))+100+(ebu*1.45)
    d2=d1+((d1/100)*16)
    print('Electricity bill of Andra pradesh')
    print(30*'=')
    print('Consumer name:****')
    print ('bill is rupees :',d2)


    
    
    
    
    
