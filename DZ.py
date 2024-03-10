import customtkinter
import tkinter.messagebox

root = tkinter.Tk()
w = root.winfo_screenwidth() / 2 - 225
h = root.winfo_screenheight() / 2 - 150
root.geometry(f'450x300+{int(w)}+{int(h)}')
root.resizable(width=False, height=False)
root.title('Кантор валют')
root['bg'] = 'grey60'


def f():
    try:
        comboGet1 = combo1.get()
        comboGet2 = combo2.get()
        amount = float(ent1.get())

        currencyRates = {
            'Гривня (UAH)': 1,
            'Долар (USD)': 0.026,
            'Євро (Euro)': 0.024,
            'Лев (BGN)': 0.047,
            'Злотий (PLN)': 0.10,
            'Стерлінги (GBP)': 0.020
        }

        res = amount * currencyRates[comboGet2] / currencyRates[comboGet1]
        lblInEnt2['text'] = res.__round__(3)
    except ValueError:
        tkinter.messagebox.showerror('Помилка', 'Введено не коректно сума конвертації')
    except KeyError:
        tkinter.messagebox.showerror('Помилка', 'Не обрано валюти')


lblMain1 = tkinter.Label(root, text='Ви даєте', font=('segoe ui black', 15), bg='grey60', fg='grey5')
lblMain1.place(x = 50, y = 10)
lblMain2 = tkinter.Label(root, text='Ви отримуєте', font=('segoe ui black', 15), bg='grey60', fg='grey5')
lblMain2.place(x = 270, y = 10)
lblMain3 = tkinter.Label(root, text='Ваша валюта', font=('segoe ui black', 14), bg='grey60', fg='grey5')
lblMain3.place(x = 30, y = 85)
lblMain4 = tkinter.Label(root, text='Валюта на обмін', font=('segoe ui black', 14), bg='grey60', fg='grey5')
lblMain4.place(x = 260, y = 85)

ent1 = customtkinter.CTkEntry(root, width=180, fg_color='grey90', height=30, font=(None, 15))
ent1.place(x = 10, y = 50)
ent2 = customtkinter.CTkFrame(root, width=180, height=27, fg_color='grey91', corner_radius=4)
ent2.place(x = 255, y = 52)
lblInEnt2 = tkinter.Label(ent2, text='', font=(None, 11), bg='grey90')
lblInEnt2.place(x = 2)

currency = ['Гривня (UAH)', 'Долар (USD)', 'Євро (Euro)', 'Лев (BGN)', 'Злотий (PLN)', 'Стерлінги (GBP)']
combo1 = customtkinter.CTkComboBox(root, values=currency, state='readonly', button_color='yellow3')
combo1.place(x = 30, y = 120)
combo2 = customtkinter.CTkComboBox(root, values=currency, state='readonly', button_color='yellow3')
combo2.place(x = 275, y = 120)

btnShowRes = customtkinter.CTkButton(root, text='Перевести', width=180, height=40, font=(None, 18), fg_color='yellow3',
                                     text_color='black', hover_color='yellow4', command=f)
btnShowRes.place(x = 130, y = 200)

root.mainloop()