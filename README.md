# Скипт для правок электронного дневника школы.

Скрипт исправляет оценки, удаляет замечания и добавляет похвалу.

## Как запустить.

* Положите файл `scripts.py` в корень проекта.
* Запустите shell командой `python manage.py shell`
* Импортируйте модули:
```python
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.models import Lesson, Schoolkid, Chastisement, Mark, Commendation
import random
from scripts.py import *
```
## Как пользоваться.

### Как исправить оценки.
```python
fix_marks('Терентьева Агата')
```
Вставьте нужное имя

### Как удалить все замечания.
```python
remove_chastisements('Терентьева Агата')
```
Вставьте нужное имя

### Как добавить похвалу.
```python
create_commendation('Терентьева Агата', 'Математика')
```
Вставьте нужное имя и предмет

