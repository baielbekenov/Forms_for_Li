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


class TableForms(forms.Form):
    name_of_disciplnes = forms.CharField() # Наименование дисциплин и других видов работ работ
    amount_of_credit = forms.IntegerField()  # количество кредитов
    group = forms.CharField()  # Группа
    amount_of_stud_budget = forms.IntegerField() # Количество бюджетных студентов
    amount_of_stud_contract = forms.IntegerField() # Количество контрактных студентов
    amount_of_all_students = forms.IntegerField() # Общее количество студентов
    semester = forms.IntegerField() # Семестер
    study_plan = forms.IntegerField()  # Лекции / По учебному плану
    nagruzka_kafedry = forms.IntegerField()  # Лекции / Зачитывается в нагрузку кафедры
    pract_study_plan = forms.IntegerField()  # Практические занятия / По учебному плану
    pract_nagruzka_kafedry = forms.IntegerField() # Практические занятия / Зачитывается в нагрузку кафедры
    lab_study_plan = forms.IntegerField() # Лаб. работы / По учебному плану
    lab_nagruzka_kafedry = forms.IntegerField() # Лаб. работы / Зачитывается в нагрузку кафедры
    rukovod = forms.IntegerField()  # Руковод. КРиКП
    recenzirov = forms.IntegerField()  #  Рецензирование. КР
    priem_SRS = forms.FloatField() #  Прием СРС
    prac_uchebnaya = forms.IntegerField() # Практика / Учебная
    prac_proizvodstnaya = forms.IntegerField() #  Практика / Произведственная
    prac_predkval = forms.IntegerField() #  Практика / Предкфалификационная
    prac_pedagog = forms.IntegerField() # Практика / Педагогическая
    prac_nauchno_isled = forms.IntegerField() #  Практика / научно-исследовательская
    control_current_1 = forms.FloatField() # Контроль / текущий 1
    control_current_2 = forms.FloatField()  #  Контроль / текущий 2
    control_current_3 = forms.FloatField() #  Контроль / текущий 3
    control_itogovyi = forms.FloatField() # Контроль / Итоговый (экзамен)
    zachita_rukovodstvo_VKR = forms.FloatField() #  Защита вып. квал работы / руководство ВКР
    zachita_consult = forms.FloatField()  #  Защита вып. квал работы / консульт по разделам
    zachita_recenzirovanie = forms.FloatField()  #  Защита вып. квал работы / Рецензирование
    zachita_uchastie_GAK = forms.FloatField() #  Защита вып. квал работы / участие в ГАК
    normokontr = forms.IntegerField()  # Нормконтр
    magister = forms.IntegerField() # Магистратура
    aspirantura_docturantura = forms.IntegerField()  # Аспирантура, докторонтура
    online = forms.IntegerField()  # Онлайн
    ofline = forms.IntegerField()  # Офлайн
    academ_sov = forms.IntegerField()  # Академ. сов
    rukovod_kafedroi = forms.IntegerField() #  Руководство кафедрой
    rukovod_dekanatom = forms.IntegerField()  # Руководство деканатом
    prochie = forms.IntegerField()  # Прочие
    all_education_time = forms.FloatField()  # Всего учебных часов по расчету
    name_of_teacher = forms.FloatField() # ФИО учителей
    budget = forms.FloatField()  # бюджет
    contract = forms.FloatField() # Контракт
    po_chasovoi_fond = forms.FloatField()  # По часовой фонд




