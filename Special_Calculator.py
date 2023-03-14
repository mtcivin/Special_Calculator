import tkinter
from tkinter import messagebox

number = []
arif = []
med = []
real_max = []
real_min = []


def enter1():
    zero_2()
    label['text'] += '1'


def enter2():
    zero_2()
    label['text'] += '2'


def enter3():
    zero_2()
    label['text'] += '3'


def enter4():
    zero_2()
    label['text'] += '4'


def enter5():
    zero_2()
    label['text'] += '5'


def enter6():
    zero_2()
    label['text'] += '6'


def enter7():
    zero_2()
    label['text'] += '7'


def enter8():
    zero_2()
    label['text'] += '8'


def enter9():
    zero_2()
    label['text'] += '9'


def enter0():
    if label['text'] != '0':
        label['text'] += '0'


def enter_delete():
    label['text'] = '0'
    zero()


def control(event):
    if event.char == '1':
        enter1()
    elif event.char == '2':
        enter2()
    elif event.char == '3':
        enter3()
    elif event.char == '4':
        enter4()
    elif event.char == '5':
        enter5()
    elif event.char == '6':
        enter6()
    elif event.char == '7':
        enter7()
    elif event.char == '8':
        enter8()
    elif event.char == '9':
        enter9()
    elif event.char == '0':
        enter0()
    elif event.keysym == 'BackSpace':
        enter_delete()
    elif event.keysym == 'Return':
        real_enter()
    elif event.keysym == 'Delete':
        refact()
    elif event.keysym == 'minus':
        bad()
    elif event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
        point()
    elif event.keysym == 'F1':
        average()
    elif event.keysym == 'F2':
        median()
    elif event.keysym == 'Prior':
        find_max()
    elif event.keysym == 'Next':
        find_min()
    elif event.keysym == 'Home':
        e()
    else:
        print(event.keysym)


def not_zero():
    global number

    if number == []:
        messagebox.showinfo('Неправильное действие', 'Введите числа')
    if len(label['text']) >= 2:
        if label['text'][-1] == '.':
            label['text'] = label['text'][:-1]
        elif label['text'][-1] == '0' and label['text'][-2] == '.':
            label['text'] = label['text'][:-2]


def clear(diego: list[float]):
    y = list(str(diego))
    while "'" in y:
        y.remove("'")
    if '[' in y:
        y.remove('[')
        y.remove(']')
    y2 = ''.join(y)
    if len(y2) > 10:
        if len(y2) > 10 and '.' in y:
            for i in y:
                if i == '.':
                    y = y[:(y.index(i) + 2)]
                    if len(''.join(y)) <= 10:
                        return ''.join(y)
                    else:
                        messagebox.showinfo('Большой ответ', ''.join(y))
                        label['text'] = '0'
                        return ''.join(y)
        else:
            messagebox.showinfo('Большой ответ', y2)
            label['text'] = '0'
    else:
        return y2


def show():
    messagebox.showinfo('Информация', '1 - Чтобы записать число введите его и нажмите Enter - Enter \n'
                                      '2 - Чтобы очистить список чисел нажмите Refact - Delete \n'
                                      '3 - Чтобы посмотреть список чисел нажмите Number - Home\n'
                                      '4 - Чтобы вычислить некоторые свойства нажмите на кнопку с нужным вам'
                                      ' свойством - по порядку F1 F2 P_Up P_Down\n'
                                      '5 - Чтобы написать дроби и отрицательные числа нажмите соответствующие кнопки - '
                                      'Minus Shift')


def real_enter():
    global number
    if label['text'][-1] != '.':
        number.append(label['text'])
    elif label['text'][-1] == '.':
        number.append(label['text'][:-1])
    label['text'] = '0'


def average():
    global number, arif
    arif = []
    not_zero()

    summary = 0
    count = 0

    for j in number:
        summary += float(j)
        count += 1

    arif.append(summary / count)
    arif = clear(arif)
    label['text'] = arif
    not_zero()


def median():
    global number, med
    med = []
    not_zero()
    coolist_2 = sorted(number)
    coolist_1 = [float(j) for j in coolist_2]
    coolist = sorted(coolist_1)

    if len(coolist) % 2 == 1:
        med.append(coolist[len(coolist) // 2])
    else:
        one_number = coolist[(len(coolist) // 2 - 1)]
        two_number = coolist[(len(coolist) // 2)]
        med.append((float(one_number) + float(two_number)) / 2)
    med = clear(med)
    label['text'] = med
    not_zero()


def find_max():
    global number, real_max
    real_max = []
    not_zero()

    max_num = number[0]
    for j in number:
        if float(j) > float(max_num):
            max_num = float(j)
    real_max.append(max_num)
    real_max = clear(real_max)
    label['text'] = real_max
    not_zero()


def find_min():
    global number, real_min
    real_min = []
    not_zero()

    min_num = number[0]
    for j in number:
        if float(j) < float(min_num):
            min_num = float(j)
    real_min.append(min_num)
    if min_num != 0:
        real_min = clear(real_min)
    else:
        real_min = '0'
    label['text'] = real_min
    not_zero()


def bad():
    if label['text'][-1] in '.-':
        enter_delete()
    elif label['text'][-1] == '0':
        label['text'] = ''
    label['text'] += '-'


def point():
    if label['text'][-1] in '.-':
        enter_delete()
    label['text'] += '.'


def zero():
    if len(label['text']) < 1 or label['text'] == ' ':
        label['text'] = '0'
    else:
        pass


def zero_2():
    if label['text'] == '0':
        label['text'] = ''


def refact():
    global number, arif, med, real_max, real_min

    number = []
    arif = []
    med = []
    real_max = []
    real_min = []


def e():
    global number
    messagebox.showinfo('Информация', str(', '.join(number)))


corp = tkinter.Tk()
corp.title('Calculator')
corp.geometry('300x400')
corp.resizable(False, False)
corp.configure(bg='white')
corp.bind('<Key>', control)

button1 = tkinter.Button()
button1.configure(text='1', command=enter1, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button1.place(relx=0.2, rely=0.5, width=50, height=50, anchor='center')

button2 = tkinter.Button()
button2.configure(text='2', command=enter2, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button2.place(relx=0.38, rely=0.5, width=50, height=50, anchor='center')

button3 = tkinter.Button()
button3.configure(text='3', command=enter3, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button3.place(relx=0.56, rely=0.5, width=50, height=50, anchor='center')

button_back = tkinter.Button()
button_back.configure(text='<', command=enter_delete, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button_back.place(relx=0.77, rely=0.5, width=70, height=50, anchor='center')

button_find_max = tkinter.Button()
button_find_max.configure(text='max', command=find_max, bg='grey', font=('Futura Xblk BT', 11), fg='white')
button_find_max.place(relx=0.7095, rely=0.709, width=35, height=38, anchor='center')

button_find_min = tkinter.Button()
button_find_min.configure(text='min', command=find_min, bg='grey', font=('Futura Xblk BT', 11), fg='white')
button_find_min.place(relx=0.825, rely=0.709, width=35, height=38, anchor='center')

button_average = tkinter.Button()
button_average.configure(text='arif', command=average, bg='grey', font=('Futura Xblk BT', 11), fg='white')
button_average.place(relx=0.7095, rely=0.615, width=35, height=38, anchor='center')

button_median = tkinter.Button()
button_median.configure(text='med', command=median, bg='grey', font=('Futura Xblk BT', 11), fg='white')
button_median.place(relx=0.825, rely=0.615, width=35, height=38, anchor='center')

button_refact = tkinter.Button()
button_refact.configure(text='Refact', command=refact, bg='grey', font=('Futura Xblk BT', 12), fg='white')
button_refact.place(relx=0.77, rely=0.79, width=70, height=26, anchor='center')

button4 = tkinter.Button()
button4.configure(text='4', command=enter4, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button4.place(relx=0.2, rely=0.63, width=50, height=50, anchor='center')

button5 = tkinter.Button()
button5.configure(text='5', command=enter5, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button5.place(relx=0.38, rely=0.63, width=50, height=50, anchor='center')

button6 = tkinter.Button()
button6.configure(text='6', command=enter6, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button6.place(relx=0.56, rely=0.63, width=50, height=50, anchor='center')

button7 = tkinter.Button()
button7.configure(text='7', command=enter7, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button7.place(relx=0.2, rely=0.76, width=50, height=50, anchor='center')

button8 = tkinter.Button()
button8.configure(text='8', command=enter8, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button8.place(relx=0.38, rely=0.76, width=50, height=50, anchor='center')

button9 = tkinter.Button()
button9.configure(text='9', command=enter9, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button9.place(relx=0.56, rely=0.76, width=50, height=50, anchor='center')

button01 = tkinter.Button()
button01.configure(text='Enter', command=real_enter, bg='#5b7feb', font=('Futura Xblk BT', 12), fg='white')
button01.place(relx=0.2, rely=0.89, width=50, height=50, anchor='center')

button0 = tkinter.Button()
button0.configure(text='0', command=enter0, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button0.place(relx=0.38, rely=0.89, width=50, height=50, anchor='center')

button02 = tkinter.Button()
button02.configure(text='.', command=point, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button02.place(relx=0.515, rely=0.89, width=24, height=50, anchor='center')

button03 = tkinter.Button()
button03.configure(text='-', command=bad, bg='#5b7feb', font=('Time New Roman', 24), fg='white')
button03.place(relx=0.6, rely=0.89, width=24, height=50, anchor='center')

button_01 = tkinter.Button()
button_01.configure(text='Number', command=e, bg='#5b7feb', font=('Futura Xblk BT', 12), fg='white')
button_01.place(relx=0.77, rely=0.89, width=70, height=50, anchor='center')

button_01 = tkinter.Button()
button_01.configure(text='?', command=show, bg='#485e48', font=('Futura Xblk BT', 10), fg='white')
button_01.place(relx=0.9085, rely=0.932, width=15, height=15, anchor='center')

label = tkinter.Label()
label.configure(text='0', font=('Time New Roman', 24), anchor='e', bg='white')
label.place(relx=0.5, rely=0.2, width=230, height=90, anchor='center')

corp.mainloop()