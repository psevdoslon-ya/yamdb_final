![example workflow](https://github.com/psevdoslon-ya/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

#  Описание
**Проект YaMDb**

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

**Запуск проекта.**

Клонирование репозитория и переход в проект:
```bash
git clone https://github.com/psevdoslon-ya/infra_sp2.git
cd infra_sp2
```

Создание и активация виртуального окружения:
```bash
python3.7 -m venv venv
. venv/bin/activate
python3.7 -m pip install --upgrade pip
```

Создание зависимостей из requirements.txt:
```bash
pip install -r api_yamdb/requirements.txt
```

**Работа с DOCKER.**

Переход в папку с файлом docker-compose.yaml:
```bash
cd infra/
```

Создание контейнеров:
```bash
docker-compose up -d --build
```

Выполнение миграций:
```bash
docker-compose exec web python manage.py makemigrations reviews
```
```bash
docker-compose exec web python manage.py migrate
```

Создание суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

Сбор статики:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

**Работа с базой данных.**

Заполнение базы данных (файл не включен текущий репозиторий):
добавить <название файла> .json в папку с manage.py и выполнить комманду
```bash
docker-compose exec web python manage.py loaddata <название файла>.json
```

Создание дампа базы данных (не включен текущий репозиторий):
```bash
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```

Останавка и удаление контейнеров:
```bash
docker-compose down -v
```

### Шаблон наполнения .env файла. 
Расположенние в проекте: infra_sp2/infra/.env
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Документация API YaMDb
Документация доступна по эндпойнту: http://localhost/redoc/