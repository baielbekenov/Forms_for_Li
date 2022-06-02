from django import forms


class TableForm(forms.Form):
    name_cycle = forms.CharField(max_length=100)
    name_lesson = forms.CharField(max_length=100)
    department = forms.CharField()
    credits = forms.IntegerField()
    hours = forms.IntegerField()
    total = forms.IntegerField()
    lectures = forms.IntegerField()
    laboratory = forms.IntegerField()
    practical = forms.IntegerField()
    independent_work = forms.IntegerField()
    St_1sem_lcc = forms.IntegerField()   # 1st year study / 1 sem (AS) - 16 weeks
    St_1sem_lab = forms.IntegerField()   # 1st year study / 1 sem (AS) - 16 weeks
    St_1sem_prac = forms.IntegerField()  # 1st year study / 1 sem (AS) - 16 weeks
    St_1sem_Credit = forms.IntegerField()  # 1st year study / 1 sem (AS) - 16 weeks
    St_2sem_lcc = forms.IntegerField()  # 1st year study / 2 sem (AS) - 16 weeks
    St_2sem_lab = forms.IntegerField()  # 1st year study / 2 sem (AS) - 16 weeks
    St_2sem_prac = forms.IntegerField()  # 1st year study / 2 sem (AS) - 16 weeks
    St_2sem_Credit = forms.IntegerField()  # 1st year study / 2 sem (AS) - 16 weeks
    nd2_1sem_lcc = forms.IntegerField()  # 2nd year study / 1 sem (AS) - 16 weeks
    nd2_1sem_lab = forms.IntegerField()  # 2nd year study / 1 sem (AS) - 16 weeks
    nd2_1sem_prac = forms.IntegerField() # 2nd year study / 1 sem (AS) - 16 weeks
    nd2_1sem_Credit = forms.IntegerField()  # 2nd year study / 1 sem (AS) - 16 weeks
    nd2_2sem_lcc = forms.IntegerField()  # 2nd year study / 2 sem (AS) - 16 weeks
    nd2_2sem_lab = forms.IntegerField()  # 2nd year study / 2 sem (AS) - 16 weeks
    nd2_2sem_prac = forms.IntegerField()  # 2nd year study / 2 sem (AS) - 16 weeks
    nd2_2sem_Credit = forms.IntegerField()  # 2nd year study / 2 sem (AS) - 16 weeks
    rd3_1sem_lcc = forms.IntegerField()  # 3rd year study / 1 sem (AS) - 16 weeks
    rd3_1sem_lab = forms.IntegerField()  # 3rd year study / 1 sem (AS) - 16 weeks
    rd3_1sem_prac = forms.IntegerField()  # 3rd year study / 1 sem (AS) - 16 weeks
    rd3_1sem_Credit = forms.IntegerField()  # 3rd year study / 1 sem (AS) - 16 weeks
    rd3_2sem_lcc = forms.IntegerField()  # 3rd year study / 2 sem (AS) - 16 weeks
    rd3_2sem_lab = forms.IntegerField() # 3rd year study / 2 sem (AS) - 16 weeks
    rd3_2sem_prac = forms.IntegerField() # 3rd year study / 2 sem (AS) - 16 weeks
    rd3_2sem_Credit = forms.IntegerField() # 3rd year study / 2 sem (AS) - 16 weeks
    th4_1sem_lcc = forms.IntegerField()   # 4th year study / 1 sem (AS) - 16 weeks
    th4_1sem_lab = forms.IntegerField()  # 4th year study / 1 sem (AS) - 16 weeks
    th4_1sem_prac = forms.IntegerField()  # 4th year study / 1 sem (AS) - 16 weeks
    th4_1sem_Credit = forms.IntegerField()  # 4th year study / 1 sem (AS) - 16 weeks
    th4_2sem_lcc = forms.IntegerField()  # 4th year study / 2 sem (AS) - 16 weeks
    th4_2sem_lab = forms.IntegerField()  # 4th year study / 2 sem (AS) - 16 weeks
    th4_2sem_prac = forms.IntegerField() # 4th year study / 2 sem (AS) - 16 weeks
    th4_2sem_Credit = forms.IntegerField() # 4th year study / 2 sem (AS) - 16 weeks
    Semesters_report_exam = forms.IntegerField()
    Semesters_report_credits_zachet = forms.IntegerField()
    Semesters_report_CW_CP = forms.IntegerField()
    Semesters_report_State_exam = forms.IntegerField()




