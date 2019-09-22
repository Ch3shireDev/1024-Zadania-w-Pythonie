import sys
import re

class Exercise:
    question = None

    def __init__(self, raw_str):
        self.raw_data = raw_str.strip()
        s = re.search(r'Question:\n+(.*?)(Hints|Example):', self.raw_data, re.DOTALL)
        if s:
            self.question = s.groups(1)[0].strip()
        else:
            self.question = self.raw_data

    def tex_data(self):
        lines = self.question.split('\n')
        print('\\begin{zadanie}')

        for line in lines:
            print(line)

        print('\\end{zadanie}')

file = open(sys.argv[1], 'r', encoding='windows-1252')
data = file.read()
file.close()

exercises = []
exercise = None

i = 0

for line in data.split('\n'):
    if re.match('#-+#', line):
        if exercise is not None and exercise.strip():
            exercises.append(Exercise(exercise))
        exercise = ''
    elif exercise is not None:
        exercise += line+'\n'

for exercise in exercises:
    exercise.tex_data()