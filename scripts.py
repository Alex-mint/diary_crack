from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.models import Lesson, Schoolkid, Chastisement, Mark, Commendation
import random


def check_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except ObjectDoesNotExist:
        print(f'{schoolkid_name} не найден')
    except MultipleObjectsReturned:
        print(f'Hайдено больше 1ого ученика с именем {schoolkid_name}')


def fix_marks(schoolkid_name):
    schoolkid = check_schoolkid(schoolkid_name)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid,
                                    points__in=[1, 2, 3])
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    print(f'У "{schoolkid.full_name}" не осталось плохих отметок')


def remove_chastisements(schoolkid_name):
    schoolkid = check_schoolkid(schoolkid_name)
    schoolkid_chastisements = Chastisement.objects.filter(
        schoolkid=schoolkid)
    schoolkid_chastisements.delete()
    print(f'У {schoolkid.full_name} удалены все замечания')
    


def create_commendation(schoolkid_name, subject_name):
    commendations = ['Молодец!', 'Отлично!', 'Хорошо!',
                     'Гораздо лучше, чем я ожидал!',
                     'Ты меня приятно удивил!',
                     'Великолепно!', 'Прекрасно!',
                     'Ты меня очень обрадовал!',
                     'Именно этого я давно ждал от тебя!',
                     'Сказано здорово – просто и ясно!',
                     'Ты, как всегда, точен!', 'Очень хороший ответ!',
                     'Талантливо!',
                     'Ты сегодня прыгнул выше головы!', 'Я поражен!',
                     'Уже существенно лучше!', 'Потрясающе!',
                     'Замечательно!', 'Прекрасное начало!',
                     'Так держать!', 'Ты на верном пути!', 'Здорово!',
                     'Это как раз то, что нужно!', 'Я тобой горжусь!',
                     'С каждым разом у тебя получается всё лучше!',
                     'Мы с тобой не зря поработали!',
                     'Я вижу, как ты стараешься!',
                     'Ты растешь над собой!',
                     'Ты многое сделал, я это вижу!',
                     'Теперь у тебя точно все получится!']

    schoolkid = check_schoolkid(schoolkid_name)
    lessons = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                    group_letter=schoolkid.group_letter,
                                    subject__title=subject_name).order_by(
        '-date')
    lesson = lessons.first()
    commendation = random.choice(commendations)
    if lesson:
        Commendation.objects.create(
            schoolkid=schoolkid,
            created=lesson.date,
            subject=lesson.subject,
            teacher=lesson.teacher,
            text=commendation
        )
        print(f'Создана похвала: "{commendation}"')
