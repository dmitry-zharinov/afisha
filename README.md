# Афиша: Куда пойти

Сайт с интерактивной картой интересных мест и развлечений. Выбрав место на карте, получите подробную информацию об этом месте.

## Как установить
Предварительно должен быть установлен Python 3 версии.
Скачайте код с GitHub. Перейдите в основной каталог и установите зависимости:
```sh
$ pip install -r requirements.txt
```
Далее необходимо накатить миграции, после чего можно запускать сервер:
```sh
$ python manage.py migrate
$ python manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с manage.py и запишите туда данные в формате: `ПЕРЕМЕННАЯ=значение`.
- `DEBUG` — режим отладки, по умолчанию `False`. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ `Django`


## Доступ к панели администратора
С помощью панели администратора можно добавлять новые места, заполнять информацию и загружать картинки.

Необходимо создать нового пользователя с правами администратора:
```sh
$ python manage.py createsuperuser
```
Перейдите по ссылке [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) (убедитесь что сервер запущен).