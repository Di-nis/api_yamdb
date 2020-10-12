import datetime

from django.core.exceptions import ValidationError


def validate_year(year):
    current_year = datetime.date.today().year
    if year > current_year:
        raise ValidationError(
            'Год произведения не может быть больше текущего')


def validate_score(score):
    if score < 1 or score > 10:
        raise ValidationError('Оценка должна быть в диапазоне от 1 до 10')
