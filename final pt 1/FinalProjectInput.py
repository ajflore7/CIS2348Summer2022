# Anthony Flores 1792816
import csv
import datetime

class StudentAcademics:  # class that has all the requirements for student academics

    def __init__(self, student_id, last_name, first_name, major, disciplinary_action, gpa, graduation_date):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.disciplinary_action = disciplinary_action
        self.gpa = gpa
        self.graduation_date = graduation_date


class Roster:  # dict for the students

    def __init__(self):
        self.students = {}

    def get_student(self, student_id):
        return self.students[student_id]

    def add_student(self, student):
        self.students[student.student_id] = student

    def get_all_students(self):
        all_students = []
        for student_id in self.students:
            student = self.students[student_id]
            all_students.append(student)

        return all_students

    def get_students_using_gpa(self):
        gpa_list = []
        student_list = []
        for student in self.students.values():
            if float(student.gpa) not in gpa_list:
                gpa_list.append(float(student.gpa))
        gpa_list.sort(reverse=True)
        for gpa in gpa_list:
            for student in self.students.values():
                if float(student.gpa) == gpa:
                    student_list.append(student)
        return student_list

    def get_students_using_major(self, major):
        students_in_major = {}
        for student_id in self.students:
            student = self.students[student_id]
            if student.major == major:
                students_in_major[student_id] = student
        return students_in_major

    def get_students_by_grad_date(self):
        grad_date_list = []
        student_list = []
        for student in self.students.values():
            student_date = datetime.datetime.strptime(student.graduation_date, '%m/%d/%Y').date()
            if student_date not in grad_date_list:
                grad_date_list.append(student_date)
        grad_date_list.sort()
        for graduation_date in grad_date_list:
            for student in self.students.values():
                student_date = datetime.datetime.strptime(student.graduation_date, '%m/%d/%Y').date()
                if student_date == graduation_date:
                    student_list.append(student)
        return student_list


    def get_students_using_last_name(self):
        last_names = []
        student_list = []
        for student in self.students.values():
            if student.last_name not in last_names:
                last_names.append(student.last_name)
        last_names.sort()
        for last_name in last_names:
            for student in self.students.values():
                if student.last_name == last_name:
                    student_list.append(student)
        return student_list


if __name__ == '__main__':
    roster = Roster()

    with open('StudentsMajorsList.csv', mode = 'r') as csvfile:  # reads csv file
        reader = csv.reader(csvfile)
        for row in reader:
            # row = line.split(',')
            student_id = row[0]
            ln = row[1]
            fn = row[2]
            major = row[3]
            gpa = None
            grad_date = None
            disciplinary_action = row[4]
            student = StudentAcademics(student_id, ln, fn, major, disciplinary_action, gpa, grad_date)
            roster.add_student(student)  # adds to roster

    with open('GPAList.csv', mode = 'r') as csvfile:  # reads csv file
        reader = csv.reader(csvfile)
        for row in reader:
            student_id = row[0]
            gpa = row[1]
            student = roster.get_student(student_id)  # adds to roster
            student.gpa = gpa

    with open('GraduationDatesList.csv', mode= 'r') as csvfile:  # reads csv file
        reader = csv.reader(csvfile)
        for row in reader:
            student_id = row[0]
            graduation_date = row[1]
            student = roster.get_student(student_id)
            student.graduation_date = graduation_date


    with open('FullRoster.csv',
              mode='w', newline='') as csvfile:  # the student objects from the read files above are written in this file
        fieldnames = ['student_id', 'last_name', 'first_name', 'major', 'gpa', 'graduation_date', 'disciplinary_action']
        writer = csv.writer(csvfile)
        all_students = roster.get_students_using_last_name()
        for student in all_students:
            row = [student.student_id,
                   student.first_name,
                   student.last_name,
                   student.major,
                   student.gpa,
                   student.graduation_date,
                   student.disciplinary_action]
            writer.writerow(row)

    majors = set()
    for student_id in roster.students:
        student = roster.students[student_id]
        majors.add(student.major)

    for major in majors:    # left commas in the output because instructions state to indicate behaviors
        students_in_major = roster.get_students_using_major(major)
        file_name = major.replace(" ", "") + 'Students.csv'  # replaces the spaces in the file
        with open(file_name, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for student_ID in sorted(students_in_major.keys()):
                student = roster.students[student_ID]
                row = [student.student_id, student.last_name,
                       student.graduation_date, student.disciplinary_action]
                writer.writerow(row)  # updates the majors for the roster

    with open('ScholarshipCandidates.csv',
              mode='w',newline='') as csvfile:  # writes data for students who meet scholarship criteria
        writer = csv.writer(csvfile)

        for student in roster.get_students_using_gpa():
            student_date = datetime.datetime.strptime(student.graduation_date, '%m/%d/%Y').date() # compares date by a specific format as stated
            if (float(student.gpa) >= 3.8) and (student_date > datetime.date.today()) and (student.disciplinary_action != 'Y'):
                row = [student.student_id, student.last_name,
                       student.first_name,
                       student.major, student.gpa]
                writer.writerow(row)  # also updates the roster if disciplined students is none

    with open('DisciplinedStudents.csv',
              mode='w', newline='') as csvfile:  # writes data for students who have been disciplined and write into a new file
        writer = csv.writer(csvfile)

        for student in roster.get_students_by_grad_date():
            if student.disciplinary_action == 'Y':
                row = [student.student_id, student.last_name,
                       student.first_name, student.graduation_date]
                writer.writerow(row)  # updates the roster with the new disciplined students
