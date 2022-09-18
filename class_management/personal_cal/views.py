from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from personal_cal.models import *
from django.conf import settings
from django.core.mail import send_mail   

# data processing packages
import pandas as pd
from datetime import datetime
from datetime import date

# function
def home_cal(request):
    tlp = loader.get_template('weekcal.html')
    return HttpResponse(tlp.render({}, request))


def email(request):
    if request.method == 'POST':
        # get study schedule data
        cal_db = time_table.objects.all().values()
        df = pd.DataFrame(cal_db, columns = ['stt', 'hp', 'si_so', 'buoi', 'thu', 'giang_duong'])
        df['giang_duong'] = df['giang_duong'].astype(str)

        def get_date(weekday):
            today_year = datetime.today().isocalendar().year
            today_week = datetime.today().isocalendar().week
            today_weekday = datetime.today().weekday()
            if today_weekday + 1 <= weekday:
                return date.fromisocalendar(today_year, today_week, weekday)
            elif today_weekday + 1 > weekday:
                return date.fromisocalendar(today_year, today_week + 1, weekday)

        df['ngay_tiep'] = df.apply(lambda x: get_date(x['thu']), axis = 1)
        df = df.sort_values(by = 'ngay_tiep').reset_index(drop = True)

        ## message building
        subject = "Nhắc nhở về lịch học sắp tới"
        opening = """\
            Chào bạn,
            Bạn sắp có các môn học sau đây vào những ngày gần nhất:
            """

        main_content = ""
        for i in range(0, 2):
            hp = df['hp'][i]
            buoi = df['buoi'][i]
            ngay = df['ngay_tiep'][i]
            phong = df['giang_duong'][i]
            thu = df['thu'][i]

            subjects_content = """\
                Môn học: {hp}
                Thứ: {thu}, ngày {ngay}
                Buổi: {buoi}
                Giảng đường: {phong}            
                """.format( hp = hp, thu = thu, ngay = ngay, buoi = buoi, phong = phong)
            
            main_content = main_content + "\n" + subjects_content

        ending = """
            Chúc bạn một tuần học tập hiệu quả nhé.
        """        

        mess = opening + main_content + "\n" + ending

        # get recipient_list data
        user_db = users.objects.all().filter(category = "Sinh Vien").values()
        user_df = pd.DataFrame(user_db, columns = ['stt', 'username', 'email', 'category'])
        recipient_list = list(user_df['email'])

        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, mess, email_from, recipient_list)

        # context = {
        #     'send_button' : send
        # }
    else: pass

    return render(request, 'email.html',{} )