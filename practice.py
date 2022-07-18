from random import *

#일반 유닛
class Unit:
    def __init__(self,name,hp,speed):
        self.name= name
        self.hp=hp
        self.speed=speed
        print('새로운 {0} 유닛이 생성되었습니다.'.format(self.name))
    def move(self,location):
        print('{0}: {1} 방향으로 이동합니다. 속도[{2}]'.format(self.name,location,self.speed))
#공격 유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage

    def attack(self,location):
        print('{0}:{1} 방향으로  적군을 공격합니다. [공격력:{2}]'.format(self.name,location,self.damage))

    def damaged(self,damage):
        print('{0}: 적군으로부터 {1}의 데미지를 받았습니다. '.format(self.name,damage))
        self.hp -= damage
        print('{0}의 현재 체력은 {1}입니다.'.format(self.name,self.hp))
        if self.hp <= 0:
            print('{0}은 파괴되었습니다.'.format(self.name))
#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,'마린',40,1,10)

    def stimpack(self):
        if self.hp > 10:
            self.hp -=10
            print("{0}:스팀팩을 사용합니다".format(self.name))
            self.damage +=5
            self.speed +=1
        else:
            print('{0}:체력이 일정 이하여서 사용 불가 합니다.'.format(self.name))
#탱크
class Tank(AttackUnit):

    seize_mode_develop = False

    def __init__(self):
        AttackUnit.__init__(self,'탱크',250,1,35)
        self.seize_mode= False

    def set_seize_mode(self):
        if self.seize_mode_develop == False:
            return
        if self.seize_mode==False: #시즈모드가 아닐 때
            print('{0}:시즈모드로 전환 합니다.'.format(self.name))
            self.damage *= 2
            self.seize_mode=True
        else: #시즈모드 일 때
            print("{0}:시즈모드를 해제합니다. ".format(self.name))
            self.damage /=2
            self.seize_mode=False

#날 수 있는 공중 유닛
class flyable:
    def __init__(self,flying_speed):
       self.flying_speed=flying_speed
        
    def fly(self,name,location):
        print('{0} : {1} 방향으로 날아갑니다. [속도: {2}] ' .format(name,location,self.flying_speed))

class FlyableAtaackUnit(AttackUnit,flyable):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage) #지상 스피드는 0
        flyable.__init__(self,flying_speed)
    def move(self,location):
        self.fly(self.name,location)
#레이스
class Wraith(FlyableAtaackUnit):
    def __init__(self):
        FlyableAtaackUnit.__init__(self,'레이스',70,20,1)
        self.cloked=False
    def cloking(self):
        if self.cloked==False:
            print('{0}: 클록킹 모드를 실행합니다.'.format(self.name))
            self.cloked=True
        else:
            print("{0}: 클록킹 모드를 해제합니다.".format(self.name))
            self.cloked=False

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("[Player] : GG")
    print("[Player]님이 퇴장하셨습니다.")


#실제 게임 진행

#게임시작
game_start()

#마린 3기
m1=Marine()
m2=Marine()
m3=Marine()

#탱크 2기
t1=Tank()
t2=Tank()

#레이스 1기
w1=Wraith()

#유닛 통합 제어
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move('1시')

#탱크 시즈모드 개발
Tank.seize_mode_develop=True
print('[알림] 탱크의 시즈모드 개발이 완료되었습니다.')

#공격 준비
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.cloking()

#전군 공격
for unit in attack_units:
    unit.attack('2시')


for unit in attack_units:
    unit.damaged(randint(2,51))

#게임 종료
game_over()
