#사용자의 이름, 나이, 연락처를 입력 받아서 화면에 '입력하신 이름은 000이며, 나이는 000, 그리고
#연락처는 0000-0000-0000입니다.' 를 출력하는 클래스를 작성하시오.



class informaiton:
    def __init__(self, name, age, phone_number):
        self.information_name = name
        self.information_age = age
        self.information_phone_number = phone_number

    def information(self):
        print(self.information_name,self.information_age, self.information_phone_number)

data1 = input('이름을 입력하세요.')
data2 = input('나이를 입력하세요.')
data3 = input('연락처를 입력하세요.')

x= informaiton(data1, data2, data3)

x.information()