import sqlite3
import tkinter as tk
from tkinter import messagebox

class StudentManager:
    def __init__(self):
  
        self.conn = sqlite3.connect('student.db')
        self.cursor = self.conn.cursor()

      
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                father_name TEXT,
                national_code TEXT
            )
        ''')
        self.conn.commit()


        self.app = tk.Tk()
        self.app.title('مدیریت اطلاعات دانش آموزان')

        
        self.create_gui()

    def create_gui(self):
        self.label_first_name = tk.Label(self.app, text='نام:')
        self.label_last_name = tk.Label(self.app, text='نام خانوادگی:')
        self.label_father_name = tk.Label(self.app, text='نام پدر:')
        self.label_national_code = tk.Label(self.app, text='کد ملی:')

        self.entry_first_name = tk.Entry(self.app)
        self.entry_last_name = tk.Entry(self.app)
        self.entry_father_name = tk.Entry(self.app)
        self.entry_national_code = tk.Entry(self.app)

        self.btn_insert = tk.Button(self.app, text='درج', command=self.insert_data)
        self.btn_retrieve = tk.Button(self.app, text='بازیابی', command=self.retrieve_data)
        self.btn_delete = tk.Button(self.app, text='حذف', command=self.delete_data)

        self.label_first_name.grid(row=0, column=0, padx=10, pady=5)
        self.label_last_name.grid(row=1, column=0, padx=10, pady=5)
        self.label_father_name.grid(row=2, column=0, padx=10, pady=5)
        self.label_national_code.grid(row=3, column=0, padx=10, pady=5)

        self.entry_first_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_last_name.grid(row=1, column=1, padx=10, pady=5)
        self.entry_father_name.grid(row=2, column=1, padx=10, pady=5)
        self.entry_national_code.grid(row=3, column=1, padx=10, pady=5)

        self.btn_insert.grid(row=4, column=0, columnspan=2, pady=10)
        self.btn_retrieve.grid(row=5, column=0, columnspan=2, pady=10)
        self.btn_delete.grid(row=6, column=0, columnspan=2, pady=10)

    def insert_data(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        father_name = self.entry_father_name.get()
        national_code = self.entry_national_code.get()

        if not (first_name and last_name and father_name and national_code):
            messagebox.showerror('خطا', 'لطفاً تمام فیلدها را پر کنید.')
            return

        try:
            self.cursor.execute('INSERT INTO student (first_name, last_name, father_name, national_code) VALUES (?, ?, ?, ?)',
                           (first_name, last_name, father_name, national_code))
            self.conn.commit()
            messagebox.showinfo('موفقیت', 'اطلاعات با موفقیت ذخیره شد.')
            self.clear_entries()
        except Exception as e:
            messagebox.showerror('خطا', f'خطای زیر رخ داد:\n{str(e)}')

    def retrieve_data(self):
        national_code = self.entry_national_code.get()

        if not national_code:
            messagebox.showerror('خطا', 'لطفاً کد ملی را وارد کنید.')
            return

        try:
            self.cursor.execute('SELECT * FROM student WHERE national_code = ?', (national_code,))
            result = self.cursor.fetchone()

            if result:
                messagebox.showinfo('اطلاعات دانش آموز', f'نام: {result[1]}\nنام خانوادگی: {result[2]}\nنام پدر: {result[3]}')
            else:
                messagebox.showinfo('اطلاعات دانش آموز', 'اطلاعاتی یافت نشد.')
        except Exception as e:
            messagebox.showerror('خطا', f'خطای زیر رخ داد:\n{str(e)}')

    def delete_data(self):
        national_code = self.entry_national_code.get()

        if not national_code:
            messagebox.showerror('خطا', 'لطفاً کد ملی را وارد کنید.')
            return

        try:
            self.cursor.execute('DELETE FROM student WHERE national_code = ?', (national_code,))
            self.conn.commit()
            messagebox.showinfo('موفقیت', 'اطلاعات با موفقیت حذف شد.')
            self.clear_entries()
        except Exception as e:
            messagebox.showerror('خطا', f'خطای زیر رخ داد:\n{str(e)}')

    def clear_entries(self):
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_father_name.delete(0, tk.END)
        self.entry_national_code.delete(0, tk.END)

    def run(self):
        self.app.mainloop()

    def close_connection(self):
        self.conn.close()


student_manager = StudentManager()


student_manager.run()


student_manager.close_connection()
