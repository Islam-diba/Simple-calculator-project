from tkinter import *
from math import sqrt
from decimal import Decimal


#//////////////////////////////////////////////////////////////////////////////////////////////

def check_char(screen, screen_2):
    ns = '1234567890.'
    check = screen.get()
    for i in range(len(check)):
        if check[i] not in ns:
            screen.delete(0, END)
            return
    check = screen_2.get()
    for i in range(len(check)):
        if check[i] not in ns:
            screen_2.delete(0, END)
            return

def button_color(button):
    button['fg'] = 'white'
    button['bg'] = '#001d26'
    button['bd'] = 10,
    button['highlightthickness'] = 4,
    button['highlightcolor'] = "#37d3ff",
    button['highlightbackground'] = "#37d3ff",
    button['borderwidth'] = 4
    button.bind("<Enter>", func=lambda e: button.config(
        background='#528AAE'))
    button.bind("<Leave>", func=lambda e: button.config(
        background='#001d26'))
    return button


#//////////////////////////////////////////////////////////////////////////////////////////////
def screen_2nd(root):
    screen_2 = Entry(root, font='Gill 18')
    screen_2.grid(row=0, column=0, columnspan=4, sticky='news')
    screen_2.config(background='#001d26')
    screen_2.config(foreground='white')
    return screen_2

def screen_input(root):
    screen = Entry(root, font='Gill 18')
    screen.grid(row=1, column=0, columnspan=4, ipady=33, sticky='news')
    screen.insert(0, "0")
    screen.config(background='#001d26')
    screen.config(foreground='white')
    return screen


#//////////////////////////////////////////////////////////////////////////////////////////////
def set_num_buttons(index, root, screen):
    button = Button(root, text=str(index), padx=40, pady=20, command=lambda: numeric_buttons_f(str(index), screen),
                    font='Gill 16')
    button = button_color(button)
    return button


def numeric_buttons(root, screen):
    n_buttons = []
    for i in range(10):
        n_buttons.append(set_num_buttons(i, root, screen))
    n = 7
    r = 4
    while n != -2:
        for c in range(3):
            n_buttons[n].grid(row=r, column=c, sticky='news')
            n += 1
        r += 1
        n -= 6
    n_buttons[0].grid(row=7, column=1, sticky='news')
    n_buttons.append(Button(root, text='.', padx=40, pady=20, command=lambda: numeric_buttons_f('.', screen),
                            font='Gill 16'))
    n_buttons[10].grid(row=7, column=2, sticky='news')
    n_buttons.append(Button(root, text='+/-', padx=40, pady=20, command=lambda: numeric_buttons_f('+/-', screen),
                            font='Gill 16'))
    n_buttons[11].grid(row=7, column=0, sticky='news')
    n_buttons[10] = button_color(n_buttons[10])
    n_buttons[11] = button_color(n_buttons[11])


def numeric_buttons_f(i, screen):
    if '.' in screen.get():
        if i == '.':
            return

    if screen.get() == '0' and i == '0':
        return
    elif i == '+/-':
        if screen.get() == '' or screen.get() == '0':
            return
        if '-' in screen.get():
            aj = screen.get()[1:]
            screen.delete(0, END)
            screen.insert(0, aj)
        else:
            if screen.get() == '' or screen.get() == '0':
                return
            aj = '-' + screen.get()
            screen.delete(0, END)
            screen.insert(0, aj)
    else:
        temp = screen.get() + i
        if temp[0] == '0':
            temp = i
        screen.delete(0, END)
        screen.insert(0, temp)
#//////////////////////////////////////////////////////////////////////////////////////////////


def set_opera_buttons(index, root, screen,  screen_2, operational_signs):
    button = Button(root, padx=40, pady=20, text=operational_signs[index],
                    command=lambda: operational_buttons_f(operational_signs[index], screen,  screen_2),
                    font='Gill 16')
    button = button_color(button)
    return button


def operational_buttons(root, screen, screen_2):
    o_buttons = []
    operational_signs = ['+', '-', 'x', '÷', '%']
    for i in range(5):
        o_buttons.append(set_opera_buttons(i, root, screen, screen_2, operational_signs))
    i = 3
    for r in range(3, 7):
        o_buttons[i].grid(row=r, column=3, sticky='news')
        i -= 1
    o_buttons[4].grid(row=2, column=0, sticky='news')


def op_order(op, screen,  screen_2):
    temp1 = screen.get()
    temp2 = screen_2.get()
    op_signs = ['+', '-', 'x', '÷', '%']
    if temp2 != '':
        if op in op_signs:
            if temp2[-1] in op_signs:
                if temp1 == '':
                    return
    screen.delete(0, END)
    screen_2.delete(0, END)
    if temp2 == '':
        temp3 = temp1 + op
    else:
        temp3 = temp2 + temp1+ op
    screen_2.insert(0, temp3)


def operational_buttons_f(op, screen,  screen_2):
    if screen.get() == '.':
        return
    check_char(screen, screen_2)
    if screen.get() == '':
        return
    if op == '+':
        op_order(op, screen, screen_2)
    elif op == '-':
        op_order(op, screen, screen_2)
    elif op == 'x':
        op_order(op, screen, screen_2)
    elif op == '÷':
        op_order(op, screen, screen_2)
    elif op == '%':
        op_order(op, screen, screen_2)
#//////////////////////////////////////////////////////////////////////////////////////////////


def set_x_buttons(index, root, screen,  screen_2, x_signs):
    button = Button(root, padx=40, pady=20, text=x_signs[index],
                    command=lambda: x_buttons_f(x_signs[index], screen, screen_2), font='Gill 16')
    button = button_color(button)
    return button


def x_buttons(root, screen, screen_2):
    xs_buttons = []
    x_signs = ['1/x', 'x²', '√x']
    for i in range(3):
        xs_buttons.append(set_x_buttons(i, root, screen,  screen_2, x_signs))
    for c in range(3):
        xs_buttons[c].grid(row=3, column=c, sticky='news')


def x_buttons_f(xs, screen,  screen_2):
    if xs == '1/x':
        if screen.get() == '0':
            screen.delete(0, END)
            return
        temp = screen.get()
        temp2 = float(temp)
        temp2 = 1 / temp2
        temp = str(temp2)
        screen.delete(0, END)
        screen.insert(0, temp)
    elif xs == 'x²':
        if screen.get() == '':
            return
        temp = screen.get()
        temp2 = float(temp)
        temp2 = temp2 * temp2
        if temp2 - int(temp2) == 0:
            temp2 = int(temp2)
        temp = str(temp2)
        screen.delete(0, END)
        screen.insert(0, temp)
    elif xs == '√x':
        if screen.get() == '':
            return
        temp = screen.get()
        temp2 = float(temp)
        temp2 = sqrt(temp2)
        if temp2 - int(temp2) == 0:
            temp2 = int(temp2)
        temp = str(temp2)
        screen.delete(0, END)
        screen.insert(0, temp)

#//////////////////////////////////////////////////////////////////////////////////////////////


def set_del_buttons(index, root, screen,  screen_2, del_signs):
    button = Button(root, padx=40, pady=20, text=del_signs[index],
                    command=lambda: del_buttons_f(del_signs[index], screen,  screen_2), font='Gill 16')
    button = button_color(button)
    return button


def delete_buttons(root, screen, screen_2):
    del_buttons = []
    del_signs = ['CE', 'C', '⌫']
    for i in range(3):
        #del_buttons.append(Button(root, padx=40, pady=20, text=del_signs[i]))
        del_buttons.append(set_del_buttons(i, root, screen, screen_2, del_signs))
    for c in range(3):
        del_buttons[c].grid(row=2, column=c+1, sticky='news')


def del_buttons_f(del_s, screen,  screen_2):
    if del_s == 'CE':
        screen.delete(0, END)
    elif del_s == 'C':
        screen.delete(0, END)
        screen_2.delete(0, END)
    elif del_s == '⌫':
        temp = screen.get()[:-1]
        screen.delete(0, END)
        screen.insert(0, temp)
#//////////////////////////////////////////////////////////////////////////////////////////////


def equal_button(root, screen,  screen_2):
    el_button = Button(root, padx=40, pady=20, text='=', command=lambda: eql_buttons_f(screen,  screen_2),
                       font='Gill 16')
    el_button = button_color(el_button)
    el_button.grid(row=7, column=3, sticky='news')


def eql_buttons_f(screen,  screen_2):
    signs = ['+', '-', 'x', '÷', '%']
    check_char(screen, screen_2)
    if screen_2.get() == '':
        return
    if screen_2.get()[-1] in signs:
        if screen.get() in signs:
            return
    temp1 = screen_2.get() + screen.get()
    temp2 = convert_signs(temp1)
    screen.delete(0, END)
    screen_2.delete(0, END)
    screen.insert(0, temp2)


def convert_signs(ops):
    all_signs = ['+', '-', 'x', '÷', '%']
    signs = ['x', '÷', '%']
    ops_list = []
    num_list = []
    adj_ops = []
    for o in range(len(ops)):
        adj_ops.append(ops[o])
    for i in range(len(adj_ops)):
        try:
            if adj_ops[i] == '-' and adj_ops[i+1] == '-':
                adj_ops[i] = '+'
                adj_ops.pop(i+1)
            elif adj_ops[i] == '+' and adj_ops[i+1] == '-':
                adj_ops[i] = '-'
                adj_ops.pop(i+1)
        except:
            break
    new_ops = ''
    for s in adj_ops:
        new_ops += s
    # extract operators
    for s in range(len(new_ops)):
        if new_ops[s] in all_signs:
            ops_list.append(new_ops[s])
    low = 0
    # extract numbers
    for i in range(len(new_ops)):
        if new_ops[i] in all_signs:
            if low == i-1:
                num_list.append(new_ops[low])
                low = i+1
            else:
                num_list.append(new_ops[low:i])
                low = i+1
    num_list.append(new_ops[low:]) # extract the last number
    num_list = ' '.join(num_list)
    st1 = ''
    for s in num_list:
        st1 += s
    data = list(map(Decimal, st1.split()))
    for i in range(len(ops_list)):
        if ops_list[i] == 'x':
            try:
                data[i] = data[i] * data[i+1]
                data.pop(i+1)
            except:
                data[i] = data[i-1] * data[i]
                data.pop(i-1)
        if ops_list[i] == '%':
            try:
                data[i] = data[i] % data[i+1]
                data.pop(i+1)
            except:
                data[i] = data[i-1] % data[i]
                data.pop(i-1)
        if ops_list[i] == '÷':
            try:
                data[i] = data[i] / data[i+1]
                data.pop(i+1)
            except:
                data[i] = data[i-1] / data[i]
                data.pop(i-1)
    new_op = []
    for i in ops_list:
        if i not in signs:
            new_op.append(i)
    for i in range(len(new_op)):
        if new_op[i] == '+':
            data[0] = data[0] + data[1]
            data.pop(1)
        elif new_op[i] == '-':
            data[0] = data[0] - data[1]
            data.pop(1)
    return str(data[0])


#//////////////////////////////////////////////////////////////////////////////////////////////
def main():
    root = Tk()
    root.attributes('-alpha', 0.7)
    root.title("Standard Calculator")
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)
    screen = screen_input(root)
    screen_2 = screen_2nd(root)
    numeric_buttons(root, screen)
    operational_buttons(root, screen, screen_2)
    x_buttons(root, screen, screen_2)
    delete_buttons(root, screen, screen_2)
    equal_button(root, screen,  screen_2)
    root.mainloop()


if __name__ == '__main__':
    main()
