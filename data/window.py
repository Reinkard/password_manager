from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import json

FONT = 'Courier'
COLOR_BG = '#262A56'
COLOR_TEXT = '#E3CCAE'

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.config(padx=40, pady=20, bg=COLOR_BG)
        self.resizable(width=False, height=False)
        self.title('Password Manager')

    def logo_picture(self):
        self.canvas = Canvas(width=200, height=200, bg=COLOR_BG, highlightthickness=0)
        self.pass_logo = PhotoImage(file='data/logo.png')
        self.canvas_logo = self.canvas.create_image(100, 100, image=self.pass_logo)
        self.canvas.grid(row=0, column=0, columnspan=2)
    
    def labels(self):
        self.logo = Label(text='Password Manager', font=(FONT, 13, 'bold'), bg=COLOR_BG, fg=COLOR_TEXT)
        self.logo.grid(row=1, column=0, columnspan=2)
        self.name = Label(text='Назва сайту', font=(FONT, 13), bg=COLOR_BG, fg=COLOR_TEXT, padx=10)
        self.name.grid(row=3, column=0, sticky=W)
        self.login = Label(text='Логін', font=(FONT, 13), bg=COLOR_BG, fg=COLOR_TEXT, padx=10)
        self.login.grid(row=4, column=0, sticky=W)
        self.password = Label(text='Пароль', font=(FONT, 13), bg=COLOR_BG, fg=COLOR_TEXT, padx=10)
        self.password.grid(row=5, column=0, sticky=W)

    def entries(self):
        self.entry_sitename = Entry(justify=LEFT, width=15)
        self.entry_sitename.grid(row=3, column=1, pady=10, sticky=W)
        self.entry_sitename.focus()
        self.entry_login = Entry(justify=LEFT, width=33)
        self.entry_login.grid(row=4, column=1, columnspan=2, pady=10, sticky=W)
        self.entry_password = Entry(justify=LEFT, width=15)
        self.entry_password.grid(row=5, column=1, pady=10, sticky=W)

    def buttons(self):
        self.search_button = Button(justify=RIGHT, width=13, height=1, text='Пошук', command=self.check)
        self.search_button.grid(row=3, column=1, sticky=E)
        self.generate_button = Button(justify=RIGHT, width=13, height=1, text='Згенерувати', command=self.password_generator)
        self.generate_button.grid(row=5, column=1, sticky=E)
        self.configure_button = Button(justify=RIGHT, width=30, height=1, text='Додати', command=self.add_data)
        self.configure_button.grid(row=6, column=1)
        
    def add_data(self):
        """
        add data to txt file
        """
        # беремо інформацію з введених полів у програмі
        sitename = self.entry_sitename.get()
        login = self.entry_login.get()
        password = self.entry_password.get()
        new_data = {
            sitename: {
                    'login': login,
                    'password': password
            }
        }

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
            # save data to file data/short_data.json
            try:
                with open('data/short_data.json', 'r', encoding='utf-8') as data_read:
                    # reading old data
                    data = json.load(data_read)
                    # updating old data with new data
                    data.update(new_data)
                with open('data/short_data.json', 'w', encoding='utf-8') as data_write:
                    # saving updated data
                    json.dump(data, data_write, indent=4)
            except json.decoder.JSONDecodeError:
                with open('data/short_data.json', 'w', encoding='utf-8') as data_write:
                    # saving updated data
                    json.dump(new_data, data_write, indent=4)
            # copy text to clipboard
            self.clipboard_clear()
            self.clipboard_append(self.entry_password.get())
            # popup when work is complete
            messagebox.showinfo(title='Вітаю', message='Форматування даних виконано успішно!')
    
    def check(self):
        try:
            with open('data/short_data.json', 'r', encoding='utf-8') as data_file:
                data = json.load(data_file)
            if self.entry_sitename.get() in data:
                messagebox.showinfo(title='Вітаю!', message=f"Даний сайт уже існує у списку,\n"
                                     f"логін {data[self.entry_sitename.get()]['login']}\n"
                                     f"пароль {data[self.entry_sitename.get()]['password']}\n")
            else:
                messagebox.showinfo(title='Упс!', message='Даного сайту немає у списку')
        except json.decoder.JSONDecodeError:
            messagebox.showinfo(title='Вітаю!', message='У БД порожньо!(')

            
    def password_generator(self):
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
        self.entry_password.delete(0, END)
        self.entry_password.insert(0, f'{result}')
        # copy password to clipboard
        self.clipboard_clear()
        self.clipboard_append(self.entry_password.get())


if __name__ == '__main__':
    app = MainWindow
    app.mainloop(self)