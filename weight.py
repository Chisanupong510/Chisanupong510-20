x = float(input("โปรดใส่น้ำหนักของคุณ (KG) : "))
y = float(input("โปรดใส่ส่วนสูงของคุณ (M) : "))
z = float(x/y**2)
if(z<18.5):
    print('BMI is %.1f' %z)
    print("น้ำหนักน้อย")
elif(25>z>=18.5):
    print('BMI is %.1f' %z)
    print("มาตรฐาน")
elif(30>z>=25):
    print('BMI is %.1f' %z)
    print("น้ำหนักเกิน")
elif(z>=30):
    print('BMI is %.1f' %z)
    print("เสี่ยงโรคอ้วน")