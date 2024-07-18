#게임 캐릭터 만들기. 게임 캐릭터 생성 클래스는 아이디, 성별, 직업 정보를 갖으며, 기본 공격 함수를 갖는다.
#기본 공격 함수는 사용시 '공격!' 문자열을 화면에 출력한다.


class Game:
    def __init__(self, ID, sex, job):
        self.Game_ID = ID
        self.Game_sex = sex
        self.Game_job = job

    def attack(self):
        print(self.Game_ID + "공격!")


jiwoo = Game("pokemonmaster", "여" , "궁수")

jiwoo.attack()