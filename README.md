# Афиша: Куда пойти

Сайт с интерактивной картой интересных мест и развлечений. Выбрав место на карте, получите подробную информацию об этом месте.

[Онлайн демо-версия](http://dwreaper.pythonanywhere.com/)

![изображение](https://user-images.githubusercontent.com/16899464/183261939-c8c64d31-1a02-4638-b161-81c97423e113.png)


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
- `ALLOWED_HOSTS` — один или несколько хостов/доменов, которые может обслуживать данный Django-сайт, разделённые запятой. [Документация](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Доступ к панели администратора
С помощью панели администратора можно добавлять новые места, заполнять информацию и загружать картинки.

Необходимо создать нового пользователя с правами администратора:
```sh
$ python manage.py createsuperuser
```
Перейдите по ссылке [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) (убедитесь что сервер запущен).

## Загрузка мест из json
Для добавления новых мест, можно воспользоваться командой
```sh
$ python manage.py load_place http://адрес/файла.json
```

Файл json должен иметь следующий формат ([пример](https://gist.github.com/dmitry-zharinov/52601d899d97fa948d0864984c24ccf5)):
```json
{
    "title": "Название",
    "imgs": [
        "ссылка на картинку 1",
        "ссылка на картинку 2"
    ],
    "description_short": "Краткое описание",
    "description_long": "Длинное описание",
    "coordinates": {
        "lng": "долгота",
        "lat": "широта"
    }
}
```
