#두 수의 덧셈, 뺄셈, 나눗셈, 곱셈 함수를 포함하는 클래스를 만들고, 해당 클래스를 통해 객체를 생성하시오.

class Math :
    def add (self, a, b):
            result = a + b
            return result
    def mul (self, a, b):
        result = a * b
        return result
    def division (self, a, b):
        result = a / b
        return result
    def subtractive(self, a, b):
        result = a - b
        return result

app = Math()
app.add(3, 4)

