# Anthony Flores 1792816
import csv


class StudentAcademics:  # class that has all the requirements for student academics

    def __init__(self, student_id, last_name, first_name, major, disciplinary_action, gpa, graduation_date):
        self.student_id = student_id
        self.student_ln = last_name
        self.student_fn = first_name
        self.major = major
        self.disciplinary_action = disciplinary_action
        self.gpa = gpa
        self.grad_date = graduation_date


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
            all_students.appened(student)

        return all_students

    def get_students_using_gpa(self, gpa):
        students_with_gpa = []
        for student_id in self.students:
            student = self.students[student_id]
            if student.gpa == gpa:
                students_with_gpa.append(student)
            return students_with_gpa

    def get_students_using_major(self, major):
        students_in_major = []
        for student_id in self.students:
            student = self.students[student_id]
            if student.major == major:
                students_in_major.append(student)
        return students_in_major

    def get_students_by_grad_date(self, grad_date):
        students_by_grad_date = []
        for student_id in self.students:
            student = self.students[student_id]
            if student.grad_date == grad_date:
                students_by_grad_date.append(student)
            return students_by_grad_date

    def get_students_by_disciplinary_action(self, disciplinary_action):
        students_by_disciplinary_action = []
        for student_id in self.students:
            student = self.students[student_id]
            if student.disciplinary_action == disciplinary_action:
                students_by_disciplinary_action.append(student)
            return students_by_disciplinary_action


def main():
    roster = Roster()
    with open('StudentsMajorsList.csv') as csvfile:  # reads csv file
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_id = row['student_id']
            ln = row['last_name']
            fn = row['first_name']
            major = row['major']
            gpa = ['none']
            grad_date = ['none']
            disciplinary_action = ['none']
            student = StudentAcademics(student_id, ln, fn, major, gpa, grad_date, disciplinary_action)
            roster.add_student(student)

    with open('GPAList.csv') as csvfile:  # reads csv file
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_id = row['student_id']
            gpa = row['gpa']
            student = roster.get_student(student_id)
            student.gpa = gpa

    with open('GraduationDatesList.csv') as csvfile:  # reads csv file
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_id = row['student_id']
            grad_date = row['graduation_date']
            student = roster.get_student(student_id)
            student.graduation_date = grad_date

    with open('FullRoster.csv',
              mode='w') as csvfile:  # the student objects from the read files above are written in this file
        fieldnames = ['student_id', 'last_name', 'first_name', 'major', 'gpa', 'graduation_date', 'disciplinary_action']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        all_students = roster.get_all_students()
        for student in all_students:
            row = {'student_id': student.student_id,
                   'last_name': student.last_name,
                   'first_name': student.first_name,
                   'major': student.major,
                   'gpa': student.gpa,
                   'graduation_date': student.graduation_date,
                   'disciplinary_action': student.disciplinary_action}
            writer.writerow(row)
        majors = set()
        for student_id in roster.students:
            student = roster.students[student_id]
            majors.add(student.major)
        for major in majors:
            students_in_major = roster.get_students_using_major(major)
            file_name = major.replace(" ", "") + 'Students.csv'
            with open(file_name, mode='w') as csvfile:
                fieldnames = ['student_id', 'last_name', 'first_name', 'graduation_date', 'disciplinary_action']
                writer = csv.DictWriter(csv, fieldnames=fieldnames)
                writer.writeheader()
                for student in students_in_major:
                    row = {'student_id': student.student_id,
                           'first_name': student.last_name,
                           'graduation_date': student.graduation_date,
                           'disciplinary_action': student.disciplinary_action}
                    writer.writerow(row)

    with open('ScholarshipCandidates.csv',
              mode='w') as csvfile:  # writes data for students who meet scholarship critera
        fieldnames = ['student_id', 'last_name', 'first_name', 'major', 'gpa']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for student_id in roster.students:
            student = roster.students[student_id]
            if (student.gpa >= 3.8) and (student.graduation_date == None) and (student.disciplinary_action == None):
                row = {'student_id': student.student_id, 'last_name': student.last_name,
                       'first_name': student.first_name,
                       'major': student.major, 'gpa': student.gpa}
                writer.writerow(row)

    with open('DisciplinedStudents.csv',
              mode='w') as csvfile:  # writes data for students who have been disciplined and write into a new file
        fieldnames = ['student_id', 'last_name', 'first_name', 'graduation_date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student_id in roster.students:
            student = roster.students[student_id]
            if student.disciplinary_action == 'Y':
                row = {'student_id': student.student_id,
                       'last_name': student.last_name,
                       'first_name': student.first_name,
                       'graduation_date': student.graduation_date}
                writer.writerow(row)


