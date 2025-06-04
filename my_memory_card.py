#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel,QButtonGroup
)

class Question():
    def __init__(
        self,question,right_answer,
        wrong1, wrong2,  wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []

questions_list.append(Question('2+2=???', '4', '2','3', '1'))
questions_list.append(Question('Форма земли???', 'круглая','квадратная','треугольная','прямоугольная'))
questions_list.append(Question('сколько пальцев на руках???', '10', '5','4', '42'))



app =   QApplication([])

Window = QWidget()
Window.resize(400,300)
Window.setWindowTitle('Memo Card')


btn_OK = QPushButton('Ответить')
lb_Question = QLabel('кто самй крутой')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)



layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результат')
lb_Result =QLabel('Правильно/Неправильно')
lb_Correct = QLabel('ОТВЕТ')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment= Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter ))
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

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)



answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:  Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()



def show_correct(res):
    lb_Result.setText(res)
    show_result()

# def check_answer():
#     if answers[0].isChecked():
#         show_correct('ПРАВИЛЬНО')
#     else:
#         if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
#             show_correct('Неверно')

def next_question():
    Window.total += 1
    Window.cur_question = Window.cur_question + 1
    if Window.cur_question >= len(questions_list):
        Window.cur_question = 0
    q = questions_list[Window.cur_question]
    ask(q)



def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

Window.score = 0
Window.total = 0



def check_answer():
    if answers[0].isChecked():
        show_correct('Праильно!')
        Window.score += 1
    else:
        show_correct('Не правильно!!')



Window.setLayout(layout_card)
Window.setWindowTitle('memo card')
# ask('кто самй крутой','Энцы*','Смурфы','Чулымцы','Алеуты'  )


Window.cur_question = -1



btn_OK.clicked.connect(click_OK)
Window.score = 0
Window.total = 0
next_question()

Window.show()

app.exec()
