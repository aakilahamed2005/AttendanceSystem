from dark_theme_1 import*
import sqlite3

'''
student_index_no INT(48) NOT NULL,
student_name VARCHAR(255) NOT NULL,
number_of_school_days INT(300) NOT NULL,
number_of_present_days INT(300)
'''





class my_class():

    def search_student(self):
        student_index_no = self.studentIndexNo.value()
        try:
            sqliteConnection = sqlite3.connect('student.db')
            cursor = sqliteConnection.cursor()

            cursor.execute(f"SELECT * FROM student WHERE student_index_no = {student_index_no}")
            output = cursor.fetchall()
            for row in output:
                self.label_9.setText(row[1])
                self.numberOfSchoolDays.setValue(row[2])
                self.numberOfPresentDays.setValue(row[3])
  
            sqliteConnection.commit()
            sqliteConnection.close() 

            number_of_school_days = self.numberOfSchoolDays.value()
            number_of_present_days = self.numberOfPresentDays.value()

            percentage_calc = (number_of_present_days / number_of_school_days)* 100
            percentage_calc = round(percentage_calc, 2)
            self.percentageValue.setText(str(percentage_calc) + '%')


        except:
            pass


    def update_data(self):
        student_index_no = self.studentIndexNo.value()
        number_of_school_days = self.numberOfSchoolDays.value()
        number_of_present_days = self.numberOfPresentDays.value()

        percentage_calc = (number_of_present_days / number_of_school_days)* 100
        percentage_calc = round(percentage_calc, 2)
        self.percentageValue.setText(str(percentage_calc) + '%')

        try:
            sqliteConnection = sqlite3.connect('student.db')
            cursor = sqliteConnection.cursor()

            cursor.execute(f'''UPDATE student SET number_of_school_days = {number_of_school_days}, number_of_present_days = {number_of_present_days} WHERE student_index_no = {student_index_no};''')
            sqliteConnection.commit()
            sqliteConnection.close() 

        except:
            pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AttendanceSystem()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

