from tkinter import *
from tkinter import messagebox
from random import *

FONT = 'Courier'
COLOR_BG = '#262A56'
COLOR_TEXT = '#E3CCAE'


#-----------------------ADD_DATA-------------------------------#

def add_data():
    """
    Transileration your name-sename
    """
    # беремо інформацію з введених полів у програмі
    sitename = entry_sitename.get()
    login = entry_login.get()
    password = entry_password.get()

    # popup check length of dates
    if len(sitename) == 0 or len(login) == 0 or len(password) < 12:
        messagebox.showerror('Ахтунг!', 'Не всі поля заповнені!')
    else:
        start_work = messagebox.askokcancel(title='Перевірка введених даних',
                                            message=f'Назва сайту: {sitename},\n'
                                             f'Логін: {login},\n'
                                             f'Пароль: {password}\n'
                                             'Все введено правильно?')
    # if it`s ok - start work
    if start_work:
        # save data to file data/short_data.txt
        with open('data/short_data.txt', 'a', encoding='utf-8') as result:
            result.write(f'{sitename} | {login} | {password} \n')
        # copy text to clipboard
        window.clipboard_clear()
        window.clipboard_append(entry_password.get("1.0",END))
        # popup when work is complete
        messagebox.showinfo(title='Вітаю', message='Форматування даних виконано успішно!')

#-----------------------PASSWORD_GENERATOR-------------------------------#

def password_generator():
    """
    Password generator. Return random 15 symbols
    """
    # get lists of alphabets, numbers and symbols
    letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 122)]
    numbers = [chr(i) for i in range(38, 58)]
    symbols = [chr(i) for i in range(33, 44)]
    result = [choice(letters) for _ in range(6)] + [choice(symbols) for _ in range(3)] + [choice(numbers) for _ in range(3)]
    # shuffle result
    shuffle(result)
    result = ''.join(result)
    entry_password.delete(0, END)
    entry_password.insert(0, f'{result}')
    # copy password to clipboard
    window.clipboard_clear()
    window.clipboard_append(entry_password.get())

#------------------------------UI-----------------------------------------#

window = Tk()
window.config(padx=40, pady=20, bg=COLOR_BG)
window.resizable(width=False, height=False)
window.title('Password Manager')

canvas = Canvas(window, width=200, height=200, bg=COLOR_BG, highlightthickness=0)
pass_logo = PhotoImage(file='data/logo.png')
canvas_logo = canvas.create_image(100, 100, image=pass_logo)
canvas.grid(row=0, column=0, columnspan=2)

label_logo = Label(text='Password Manager', font=(FONT, 13, 'bold'), bg=COLOR_BG, fg=COLOR_TEXT)
label_logo.grid(row=1, column=0, columnspan=2)

label_data = Label(text='Назва сайту', font=(FONT, 13), bg=COLOR_BG, fg=COLOR_TEXT, padx=10)
label_data.grid(row=3, column=0, sticky=W)
label_data = Label(text='Логін', font=(FONT, 13), bg=COLOR_BG, fg=COLOR_TEXT, padx=10)
label_data.grid(row=4, column=0, sticky=W)
label_data = Label(text='Пароль', font=(FONT, 13), bg=COLOR_BG, fg=COLOR_TEXT, padx=10)
label_data.grid(row=5, column=0, sticky=W)

entry_sitename = Entry(justify=LEFT, width=33)
entry_sitename.grid(row=3, column=1, columnspan=2, pady=10, sticky=W)
entry_sitename.focus()
entry_login = Entry(justify=LEFT, width=33)
entry_login.grid(row=4, column=1, columnspan=2, pady=10, sticky=W)
entry_password = Entry(justify=LEFT, width=15)
entry_password.grid(row=5, column=1, pady=10, sticky=W)

generate_button = Button(justify=RIGHT, width=10, height=1, text='Згенерувати', command=password_generator)
generate_button.grid(row=5, column=1, sticky=E)
configure_button = Button(justify=RIGHT, width=30, height=1, text='Додати', command=add_data)
configure_button.grid(row=6, column=1)

window.mainloop()
