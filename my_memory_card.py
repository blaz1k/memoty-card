#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QButtonGroup, QApplication,QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
from random import shuffle, randint
#f,fj,f абоба абоб  абобаабобаабобаабобаабобаабобаабобаа
class Question():
    def __init__(self, quest, right_answer, wr1, wr2, wr3):
        self.quest = quest
        self.right_answer = right_answer
        self.wr1 = wr1
        self.wr2 = wr2
        self.wr3 = wr3
question_list = list()
question_list.append(
    Question("Какая страна развалилась в 2008?", 'Югославия', 'СССР', 'Бравл старс', 'ОАР'))
question_list.append(Question(
    'Какая площадь есть в СПБ?', 'Дворцовая', "Лубянская", 'Манежская', "Революции"))
question_list.append(Question(
    "Какой век- эпоха Рококо", 'XVIII', 'XX', 'XIX', 'XVII'))
question_list.append(Question(
    'Определите способ выражения дополнения в предложении: \n Я удивленно поглядел на вошедшего.', "причастие", 'существительное','глагол','наречие'))
question_list.append(Question(
    'Какой буквой обозначают химический элемент «азот»?', 'N', 'Na', 'Az', 'A'))
question_list.append(Question(
    'В каком году образовалась Российская империя?', '1721', '1703', '1701', '1722'))
question_list.append(Question(
    'У какой страны в флаге национальный язык- Английский', 'Англия', 'Россия', 'Германия', 'Япония'))
question_list.append(Question(
    'В каком году была отечественная война?', '1812', '1703', '2077', '1941'))
#дание приложенисозя и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Приложение Memory Card')
main_win.resize(400, 200)
main_win.total = 0
main_win.score = 0
#Ввиджеты
button = QPushButton('Ответить')
question = QLabel('Вопрос')
groupBox = QGroupBox('Варианты ответов')
button1 =QRadioButton('Вариант 1')
button2 =QRadioButton('Вариант 2')
button3 =QRadioButton('Вариант 3')
button4 =QRadioButton('Вариант 4')
#Лейауты
question_lineH = QHBoxLayout()
groupBoxlineH = QHBoxLayout()
pushButtonH = QHBoxLayout()

buttonH = QHBoxLayout()
buttonV1 = QVBoxLayout()
buttonV2 = QVBoxLayout()

buttonV1.addWidget(button1)
buttonV1.addWidget(button2)
buttonV2.addWidget(button3)
buttonV2.addWidget(button4)

buttonH.addLayout(buttonV1)
buttonH.addLayout(buttonV2)

groupBox.setLayout(buttonH)

layout_card = QVBoxLayout()

question_lineH.addWidget(question, alignment = Qt.AlignCenter)
groupBoxlineH.addWidget(groupBox, alignment = Qt.AlignCenter)
pushButtonH.addStretch(1)
pushButtonH.addWidget(button, stretch=2)
pushButtonH.addStretch(1)

layout_card.addLayout(question_lineH)
layout_card.addLayout(groupBoxlineH)
layout_card.addLayout(buttonH)
layout_card.addLayout(pushButtonH)
layout_card.setSpacing(5)
#вывод ответа
ansCorrect = QLabel('Правильный ответ!')
ans2 = QLabel('Правильно/Неправильно')
ansGroupBox = QGroupBox('Результат теста')

labelLineAnsV = QVBoxLayout()

labelLineAnsV.addWidget(ans2, alignment= Qt.AlignLeft | Qt.AlignTop)
labelLineAnsV.addWidget(ansCorrect, alignment= Qt.AlignCenter)
ansGroupBox.setLayout(labelLineAnsV)
groupBoxlineH.addWidget(ansGroupBox)
ansGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)
#обработка нажатий на кнопку

ans = [button1, button2, button3, button4]


def show_result():
    groupBox.hide()
    ansGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)
    groupBox.show()
    ansGroupBox.hide()
    button.setText('Ответить')

def ask(q: Question):
    shuffle(ans)
    ans[0].setText(q.right_answer)
    ans[1].setText(q.wr1)
    ans[2].setText(q.wr2)
    ans[3].setText(q.wr3)
    question.setText(q.quest)
    ansCorrect.setText(q.right_answer)
    show_question()

def show_correct(res):
    ans2.setText(res)
    show_result()

def checked_answer():
    if ans[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
        show_correct('Неправильно!😡😡')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Рейтинг', str(round(main_win.score/main_win.total * 100,2)) + '%')
def next_question():
    if len(question_list) > 0:
        cur_question = randint(0, len(question_list)- 1)
        ask(question_list[cur_question])
        main_win.total += 1
        question_list.remove(question_list[cur_question])
    else:
        print('Тест завершен!')
        button.hide()
        ansCorrect.setText("Рейтинг:"+ str(round(main_win.score/main_win.total * 100, 2)) + '%\nВсего вопросов:' + str(main_win.total) + '\nПравыильных ответов:'+ str(main_win.score))
        ans2.setText('Результат:')
        question.setText('Тест пройден')
def click_OK():
    if button.text() == 'Ответить':
        checked_answer()
    else:
        next_question()



button.clicked.connect(click_OK)
#коккшккшкшкшшк
main_win.setLayout(layout_card)
next_question()
main_win.show()
app.exec_()