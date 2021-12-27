import random as rand
import string

class Question:
  def __init__(self):
    ''' Choose 3 random letter'''
    self.var_x = rand.choice(list(string.ascii_lowercase))
    self.var_y = rand.choice(list(string.ascii_lowercase))
    self.var_z = rand.choice(list(string.ascii_lowercase))
    self.int_a = rand.randint(1,3)
    self.int_b = rand.randint(1,3)
    self.int_x = rand.randint(0,9)
    self.int_y = rand.randint(0,9)
    self.int_z = rand.randint(1,5)
    self.operator = rand.choice(['+','-'])
    self.shapes = rand.sample(['\\circ', '\\Delta',  '\\Box', '\\Diamond'], k=2)
  
  def qTemplate(self):
    ''' Return template of problem'''
    return f'Diketahui ${self.var_x},{self.var_y},{self.var_z}$ dan sebuah fungsi yang didefinisikan sebagai berikut $ {self.var_x} {self.shapes[0]} {self.var_y} {self.shapes[1]} {self.var_z} = '
  
  def qTemplate_2(self):
    qTemp_2 = f'({self.int_a}{self.var_x} {self.operator} {self.int_b}{self.var_y})^{self.var_z}$'
    qTemp_2.replace("1","")
    return qTemp_2

  def question_1(self):
    ''' Return question for answer key'''


    quest = f'({self.int_a}*{self.int_x} {self.operator} {self.int_b}*{self.int_y})**{self.int_z} $'

    return quest

  def question_2(self):
    '''Return Half of Question'''
    quest_2 = f'${self.int_x} {self.shapes[0]} {self.int_y} {self.shapes[1]} {self.int_z}$'
    return quest_2

  def answer(self):
    '''Reutrn the Answer'''
    quest = f'({self.int_a}*{self.int_x} {self.operator} {self.int_b}*{self.int_y})**{self.int_z}'
    return eval(quest)

  def __str__(self) -> str:
    return f'\item {self.qTemplate()} {self.qTemplate_2()} nilai dari {self.question_2()} adalah'

  def __repr__(self) -> str:
    return self.__str__()


for i in range(80):
  q = Question()
  if q.answer() <=150 and q.answer() != 1 and q.answer() != 0 and q.answer() >=-150:
    print(q)
    print()
    print(q.answer())
