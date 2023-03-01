print('latihan mandiri 4.1')
def cek_angka(a, b, c):
    if a != b or a != c or b != c:
       if a + b == c or a + c == b or b + c == a:
           return True
    return False 
print(cek_angka(5,2,3))
print(cek_angka(1,1,8))
print(cek_angka(1,2,4))

print(' ')

print('latihan mandiri 4.2')
def cek_digit_belakang(a, b, c):
    if (a % 10 == b % 10) or (a % 10 == c % 10) or (b % 10 == c % 10):
        return True
    return False  
print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))

print(' ')

print('latihan mandiri 4.3')
def fahrenheit(a=32):
    celcius = int(input('Suhu Celcius to Fahrenheit : '))
    suhu =(9/5)*celcius + 32
    print('Input C=',celcius,'. Output F= ',suhu)
def reamur(b):
    celcius = int(input('Suhu Celcius to Reamur : '))
    suhuu = 0.8*celcius
    print('Input C=',celcius,'. Output F= ',suhuu)
fahrenheit(100)
reamur(80)
fahrenheit(0)

print('Lambda Function')
celcius = int(input('Suhu Celcius to Fahrenheit : '))
fahrenheit = lambda a: (9/5)*celcius + 32
print(fahrenheit(celcius))
celcius = int(input('Suhu Celcius to Fahrenheit : '))
reamur = lambda b: 0.8*celcius
print(reamur(celcius))
celcius = int(input('Suhu Celcius to Fahrenheit : '))
fahrenheit = lambda a=32: (9/5)*celcius + 32
print(fahrenheit(celcius))