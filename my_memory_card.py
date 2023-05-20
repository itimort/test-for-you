from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году была основана Москва?')
RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты ли нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана

from random import *
answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)      
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
    print('Стаитистика')
    print('Всего вопросов', window.total)
    print('Правильных ответов', window.score)
    print('Рейтинг', window.score/window.total*100, '%')

def next_question():
    window.total+=1
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() =='Ответить':
        check_answer()
    else:
        next_question()
window.total = 0
window.score = 0
window.cur_question = -1
question_list = []
question_list.append(Question('Выбери перевод слова "переменная" ', 'variable', 'variation', 'variant', 'changing'))
question_list.append(Question('Выбери перевод слова "черепаха" ', 'turtle', 'parrot', 'school', 'cherepaha'))
question_list.append(Question('Выбери перевод слова "человек" ', 'person', 'portal', 'weather', 'qwerty'))
question_list.append(Question('Какого цвета нет на флаге Россиии? ', 'голубой', 'синий', 'белый', 'красный'))
question_list.append(Question('Государственный язык США ', 'английский', 'русский', 'португальский', 'американский'))
question_list.append(Question('Самый большой океан ', 'Тихий', 'Индийский', 'Атлантический', 'Северный Ледовитый Океан'))
question_list.append(Question('Какая планета ближе к солнцу? ', 'Меркурий', 'Марс', 'Нептун', 'Земля'))
question_list.append(Question('Сколько пар ходильных ног у ракообразных? ', '5 пар', '2 пары', '10 пар', '4 пары'))
question_list.append(Question('Сколько дней в году ', '365 дней', '100 дней', 'бесконечно', '487 дней'))
question_list.append(Question('Самый большой материк ', 'Евразия', 'Северная Америка', 'Африка', 'Австралия'))
next_question()
btn_OK.clicked.connect(click_OK)
window.setLayout(layout_card)
window.show()
app.exec_()

