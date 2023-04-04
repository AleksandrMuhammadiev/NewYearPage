# -------------------------------- 4 урок 1го месяца --------------------------------------
#  Задачи:
#  1. Сделать вывод карточек при нажатии на категорию
#  2. Создать тег(функция которая будит рабротать в HTML) что бы не дублировать код в функциях
#  3. Разбитие на компоненты
#  4. Сделать страницу Детали новости

# 1. Пеерйти во views.py и сделать функцию def category_view() для вывода статей по категориям
# 2. Что бы заработала функция category_view() в urls.py прописать путь
# 3. Перейти в index.html в тег <a class="p-2> в href прописать {% url 'category' category.pk %}
#    В цикле {% for category in categories %} сдублировать тег  <a class="p-2> и поставить до цикла
#    указать текст Все стаьи и в в href прописать {% url 'index' %}

# 4. Создать свой тег(функцию), для этого в пекедже blog templatetags именно с таким названием
#    внутри создать blog_tags.py.
# 5. В blog_tags.py сделать импорты не обходимые
#    В данном файле создать register = template.Library() для рполучения библиотеки
#   Созадть функцию с деклратором get_categories()
# 6. Во views.py в функциях index и  category_view удалить
#    categories = Category.objects.all() и в котексте  'categories': categories,
# 7. В index.html подгрузить файл {% load 'blog_tags' %} и до цикла {% for category in categories %}
#    прописать  {% get_categories as categories %}
# 8. В папке blog создать папку components в данной папке будут создаватся html файлы для разбивки основного кода html
# 9. В папке components создать _categories.html  в index.html вырезать
#    <div class="nav-scroller py-1 mb-2"> c категориями и вставить в _categories.html
#    ВМЕСТО  <div class="nav-scroller py-1 mb-2"> прописать {% include 'blog/components/_categories.html' %}

# 10. В папке components создать _card.html взять в index.html <div class="card h-100">
#      и вставить в данный файл а заместо данного див блока прописать {% include 'blog/components/_card.html' %}
# 11. В views.py реализовать функцию детали статьи article_view(request, pk)
# 12. В папке blog создать article_detail.html
# 13. В urls.py создать путь на страницу  article_detail.html
# 14. В _card.html <div class="card h-100"> обернуть в тег <a> и в href прописать {% url 'article' article.pk %}
# 15. В article_detail.html записываем базовый шаблон
#      в {% block main %} собрать из тегов страницу статьи




# -------------------------------- 5 урок 1го месяца --------------------------------------
#  Задачи:
#  1. Сделать умные ссылки на страницы
#  2. Создание статей, сделать отдельную страницу
#  3. Написть логику для создания статьи
#  4. Переделывание всех вьюшек на классы




# 1. Перейти в modelsa.py и сделать импорт from django.urls import reverse
#     В классе Category  создать фугкцию def get_absolute_url(self):
# 2. В _categories.html ссылку {% url 'category' category.pk %} заменить на {{ category.get_absolute_url }}
# 3. В modelsa.py в классе Category  создать фугкцию def get_absolute_url(self):
# 4. В _card в ссылке заменить {% url 'article' article.pk %} на {{ article.get_absolute_url }}

# 5. В views.py создать функцию add_article(request): для добавления статей на страницу
#     и поставить pass
# 7.  В пекедже blog(приложении) создать forms.py для содания формачек
# 8. В forms.py сделать импорт from django import forms, from .models import Article и
#    создать класс ArticleForm(forms.ModelForm) форма для создания статьи
#    В нём же создать class Meta
# 9. Во views.py сделать импорт from .forms import ArticleForm
#       и в функции add_article дописать условия
# 10. В папке blog создать add_article.html страница для добавления статей
#     В данный файл сделать шаблон от base.html и block main
# 11. В urls.py сделать путь на страницу add_article.html
# 12. В base.html в ссылке Добавить статью  в href  прописать {% url 'add_article' %}
# 13. В add_article.html  в {% block main %} написать страницу для формы
#     {% csrf_token %} от django служит генерацией токена для защиты
#     ниже прописать { form.as_p }} для получения формы и ниже сделать кнопку
#     но данный дизайн не походит просто показать

# 14. Перейти в forms.py в class ArticleForm дописать поле widgets для изминения формы

# 15. В add_article.html создать класс <div class="d-flex justify-content-center">
#   внутри него <div class="col-6 card p-4"> и в нитри данного блока <h3 class="text-center text-light">{{ title }}</h3>
#   после тег form и всё его содержимое переместить в <div class="col-6 card p-4">

# 16. Логика для создания статьи перейти во views.py в функции add_article
#   убрасть pass и дописать логику добавления статьи и попробовать добавить статью

# 17.  В views.py все функции переделать на классы сделать импорт классов
#      Создать класс  ArticleListView заменяющий функцию index
# 18. Перейти в urls.py что переделать путь для index функции

# 19.  В views.py функцию category_view переделть на класс ArticleListByCategory
# 20.  Перейти в urls.py что переделать путь для функции category_view на класс ArticleListByCategory

# 21.  В views.py функцию article_view переделть на класс ArticleDetailView
# 22.  Перейти в urls.py что переделать путь для функции article_view на класс ArticleDetailView

# 23.  В views.py функцию add_article переделть на класс NewArticle
# 24.  Перейти в urls.py что переделать путь для функции add_article на класс NewArticle






# -------------------------------- 6 урок 1го месяца --------------------------------------
#  Задачи:
#  1. Изминение статей прописать логику
#  2. Удаление статей создать логику и страницу
#  3. Вход в аккаунт логика
#  4. Выход из аккаунта
#  5. Поиск статьи

# 1. В views.py создать класс для изминения статей ArticleUpdate(UpdateView)
# 2. В urls.py прописать путь для класс  ArticleUpdate(UpdateView)
# 3. В article_detail.html в кнопке Изменить в href прописать {% url 'update' article.pk %}
# 4. В add_article.html в кнопке создать сделать в условие на текст

# 5. В views.py создать класс для удаления статьи ArticleDelete(DetailView)
# 6. В urls.py прописать путь для класса  ArticleDelete(DeleteView)
# 7. В article_detail.html в кнопке Удалить в href прописать {% url 'delete' article.pk %}
# 8. В папке blog(приложении) создать article_confirm_delete.html и в данный файл поставить шаблон
# 9. В article_confirm_delete.html в блоке {% block main %} создать тег form
#     для создания формачки, внутри формы сделать текст с тегом <p> <input> <a>

# 10. Для написания логики в аккант перейти в forms.py сделать импорт
#       from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#       from django.contrib.auth.models import User
# 11. В  forms.py создать класс LoginForm(AuthenticationForm)
# 12. В views.py сделать импорт формы LoginForm и создать функцию user_login(request)
# 13. В папке blog(приложении) создать login.html и в данный файл поставить шаблон
# 14. В urls.py прописать путь на функцию user_login()
# 15. В base.html в кнопочке Войти в  href прописать {% url 'login' %}
# 16. В login.html в {% block main %}  создать тег form внутри него {% csrf_token %} и {{ form.as_p }}
#       ниже кнопку Войти
#       Потом над тегом form создать <div class="d-flex justify-content-center p-4">
#       внутри div class="col-6"> <div class="card bg-dark border-primary">
#       <h3 class="text-center text-light">{{ title }}</h3>
#       <div class="card-body text-center"> внутрь которого переместить тег form
#       в котором внести изминения удалить {{ form.as_p }} и в ружную сделать поля

# 17. В views.py в функции user_login(request) в if request.method == 'POST':
#        убрать pass и дописать логику. так же импортировать 2 функции login и logout и messages
# 18. В base.html  кнопки Войти, Зарегистрироваться и Дропдаун обернуть в условие {% if not request.user.is_authenticated %}

# 19. Реализовать логику выход из аккаунта в views.py функцию user_logout(request)
# 20. В urls.py прописать путь на функцию user_logout()
# 21. В base.html на кнопку выход в href прописать {% url 'logout' %}

# 22. Сделать Поиск статьи, перейти во views.py сделать класс SearchResults(ArticleListView)
# 23. В urls.py прописать путь на класс  SearchResults(ArticleListView)
# 24. В base.html поле Поиск в тег form дописать method и action в который написать {% url 'search' %}
#       в тег input дописать name="q"



#  -------------------------------- 7 урок 1го месяца --------------------------------------
#  Задачи:
#  1. Логика регистрации пользователей
#  2. Сделать логику сообщений (Вывод уведомлений)
#  3. Сделать форму входа в аккаунт всплывающим
#  4. Подключить статику
#  5. Сделать футер

# 1. Перейти в form.py создать Класс формы
#    для регистрации пользователья RegistrationForm(UserCreationForm) и поля
# 2. Во views.py сделать импорт RegistrationForm и создать функ register(request):
#    в if request == 'POST': поставить пока что pass
# 3. В папке blog создать register.html в который вставить шаблон взяв всё из логина
# 4. В  register.html сдублировать 3 раза div  с классом form-floating для Имени Фамилии Эмейла и пароля
# 5. В urls.py сделать путь на функцию register(request):
# 6. В base.html в кнопке Зарегистрироваться в href прописать путь {% url 'register' %}
# 7. В login.html в кнопке Зарегистрироваться в href прописать путь {% url 'register' %}
# 8. Во views.py в функ register(request) дописать логику вместо pass

# 9.  В глав папке templates сделать папку components а в ней _messages.html
# 10. В _messages.html сделать условие {% if messages %} и в Bootstrap.ru
#     в разделе Компаненты Уведомления есть пример всплывающих уведомлений
# 11. В _messages.html в условии сделать блог messages в нем цикл d yenhb <div class="alert дописать условие">
#       и внутри данной дивки {{ message }}
# 12. В base.html до {% block main %} дописать {% block messages %} и {% include 'components/_messages.html %}
# 13. Во views.py в функ user_login() после login(request, user) выгрузить messages.success()
#       и в else messages.error()
# 14. Во views.py в функ user_logout() после logout(request) поставить messages.warning()
# 15. Во views.py в функ register(request) после user = form.save() прописать   messages.success()
#      в else сделать цикл c проверкой на конкретную ошибку

# 16. Перейти в settings.py подключить статику дописав:
                # STATIC_ROOT = BASE_DIR / 'static'
                #
                # MEDIA_URL = '/media/'
                # MEDIA_ROOT = BASE_DIR / 'media'
# 17. Перейти в главный urls.pu что бы подключить Статику
#       сделать импорт :
#       from project import settings
#       from django.conf.urls.static import static
#       И прописать условия
# 18. Так же нужно поставить условие с заглушкой если нет фото то по умолчанию должно быть
# 19. В _card.html тег img обернуть в условие {% if article.photo %}
# 20. В article_detail.html  тег img обернуть в условие {% if article.photo %}
# 21. Попробовать добавить статью с фото

# 22. В гугл вбить bootstrap footer на сайте MDB взять код и вставить в _footer.html
# 22. В папке components где base.html создать _footer.html и в него вставить код скопированный
# 23. В base.html в container добавить стиль min-height




#  -------------------------------- 8 урок 1го месяца данный урок дать на самостоялку --------------------------------------
#  Задачи:
#  1. Создать модель Comment которая знает статью Пользователя Текст и Дату
#  2. Сохранение комента  во views.py создать функцию
#  3. Сделать вывод и показ комента
#  4. Работа с админкой настройка
#  5. Создание модального Окна вместо страницы входа в аккаунт и регистрации


# 1. В models.py создать класс модели Коментариев lass Comment(models.Model)
#       и сделать импорт from django.contrib.auth.models import User
# 2. Сделать миграции что бы добавить в базу модель Comment c полями
# 3. В admin.py  зарегистрировать модель Comment
# 4. В forms.py сделать форму для Коментариев сделать импорт модели Comment
#       и создать class CommentForm(forms.ModelForm)
# 5. Во views.py сделать импорт Comment и CommentForm в class ArticleDetailView()
#   в функции def get_context_data() дописать условие
# 6. В article_detail.html сделать ущё один блок .card HTML для коментариев в col-9
#    и в <div class="card> создать тег  <form action="" method="post"> внутри него
#    {% csrf_token %} и  {{ comment_form.as_p }} и сделать кнопку Оставить коментарий
#    Так же сделать условие если пользовать не авторизован то сделать кнопку войти в аккаунт

# 7. Сохранение комента перейти во views.py создать функцию save_comment()
# 8. В urls.py прописать путь на функцию save_comment()
# 9. В article_detail.html в тег form в параметр action дописать {% url 'save_comment' article.pk %}

# 10. Сделать вывод коментов во views.py в ArticleDetailView(DetailView)
#       Дописать вывод коментов
# 11. В article_detail.html  в <div class="col-9"> внизу дописать цикл {% for comment in comments %}
#   в цикле создать  <div class="card> в нём уде тег <h4>  <p class="small"> и тег <p>

# 12. В  admin.py созадть классс class ArticleAdmin(admin.ModelAdmin) для статей
#     Класс для отображения коментариев class CommentAdmin(admin.ModelAdmin)

#   Модальное окно
# 13. Что бы сказать что на данном сайте всегда должны быть запущенны формачки
#      В приложении blog создать context_processors.py
# 14. В context_processors.py создать функцию add_my_forms()
# 15. В settings.py в TEMPLATES под ключём 'context_processors' подключить
#       нашу функцию 'blog.context_processors.add_my_forms'

# 16. НА сайте bootstrap 4.ru в разделе модальные окна найти
#   "Переключение между модальными окнами" и скопировать код и вставить в login.html
#   вырезать ссылку из вставленного кода тег <a>

# 17. В base.html найти кнопки Войти и Зарегистрироваться  удалить один тег <li>
#   со  всем содержимым и во втором теге <li> заменить тег <a> на тот что вырезали
#   заменить текст Первое модальное окно на слово Войти и ниже {% include 'blog/login.html' %}

# 18. В login.html в блоке <div class="modal fade"> в теге <h1> слово Модалка 1
#   заменить на слово Авторизация

# 19. Найти тег <form> со всем содержимым вырезать и вситавить
#   в <div class="modal-body"> вместо содержимого текста
#   в кнопке Открыть второе модальное окно заменить текст на Зарегестрироваться
#   везде где есть form дописать login_ что бы получилось login_form
#   В кнопку Зарегестрироваться подставить data-bs-target="#exampleModalToggle2" data-bs-toggle="modal" и
#   Удалить <div class="modal-footer"> Тем самым сделали формачку входа в аккаунт

# 20. В register.html найти тег <form> скопировать со всем содержимым
# 21.  В login.html во второй модалке вместо текста
#       вставить тег <form> Скройте это модальное окно и покажите первое с помощью кнопки ниже.
#   слово Модалка 2 заменить на Регистрация и везде где form заменить на register_form
#   В кнопку войти дописать параметры  data-bs-target="#exampleModalToggle2" data-bs-toggle="modal"
# 22. Вьюшки переделать в режим POST во views.py в функции ef user_login(request):
#   в redirect всё сделать на index
# 23. В views.py в функции ef register(request):
# #   в redirect всё сделать на index
# 24. Что бы формы работали нужно повесить action.
# 25. В login.html в первом <div class="modal> в <form> в action добавить {% url 'login' %}
# 25. В login.html в втором <div class="modal> в <form> в action добавить {% url 'register' %}




#  -------------------------------- 9 урок 1го месяца --------------------------------------
#  Задачи:
#  1. Сделать просмотры
#  2. Модель пользователя
#  3. Сделать страницу профиля
#  4. Сделать форму изминения Профиля и Аккаунта
#  5.


# 1. В views.py в классе ArticleDetailView в функции get_context_data дописать логику просмотров статьи

# 2. В models.py создать  class Profile(models.Model) свою модель пользователя
# 3. Сделать мирграции и зарегать модель в admin.py
# 4. В views.py изменить логику регистрации импортировать Profile
# 5. В функции def register(request): дописать логику
# 6. Перейти в Админку и добавить профиль админу

# 7. В views.py содать функцию def profile_view(request, pk)
# 8. В приложении blog в папке blog создать profile.html и вставить в него шаблон
# 9. В гугле вбить user page bootstrap на сайте 32 Bootstrap Profile взять шаблон
#   и вставить в profile.html
# 10. В urls.py прописать путь
# 11. В base.html на кнопку Моя страница в href прописать {% url 'profile' request.user.pk %}
# 12. В  Админке в разделе пользователи для admin дать ФИ и почту
# 13. В profile.html в <h6 class="f-w-600"> вывести {{ profile.user.first_name }} {{ profile.user.last_name }}
#      вместо теста rntng@gmail.com прописать
#      вместо  98979989898 прописать  {{ profile.phone_number }}
# 14. Попробовать добавить пользователя и проверить создалась ли для него страница профиля


# 15. В forms.py сделать импорт класса UserChangeForm
#   и создать класс class EditAccountForm(UserChangeForm) для формы Пользователя
# 16. В context_processors в функции add_my_forms(request): добавить 'edit_account': EditAccountForm()
# 17. В profile.html после <p>Web Designer</p> сделать условие {% if request.user == profile.user %}
#        В bootstrap.ru взять код кнопки и вставить в условие после кнопки
#       вставить код модального окна
#       вместо слова "Заголовок модального окна" вставить Изминение Аккаунта
#      В <div class="modal-body"> выгрузить форму








#  -------------------------------- 10 урок 1го месяца --------------------------------------
#  Задачи:
#  1. Сделать анимацию падающих снежинок
#  2. Статические файлы подключение
#  3. Доделать логику изменения данных аккаунта
#  4. Сделать изменение профиля
#  5.



# 1. В гугл вбить Снижинки на сайт взять готовый код
# 2. В base.html в теге body открыть тег script и внутрь вставить код снежинок  для пробы

# 3. В приложении blog создать папку static внутри неё папку blog
#   в данной папке создать папки css, img, js
# 4. В папке css создать style.css
# 5. В папке js создать snow.js и вставить в него код снежинок
# 6. В base.html после тега body открыть тег script и добавить src в который укажем путь {% static 'blog/js/snow.js' %}
# 7. В views.py сделать импорт из forms.py  EditAccountForm форму изменения аккаунта
# 8. В views.py сделать функ  edit_account_view(request) для изм. данных аккаунта
# 9. В urls.py сделать путь для функ  edit_account_view(request)
# 10. В profile.html кнопку "Сохранить изменения" переместить в тег form
#   в тег form в параметр action поставить {% url 'edit_account' %}
# 11. В context_processors.py  в EditAccountForm дописать instance=request.user if request.user.is_authenticated else None

# 11. В forms.py сделать класс для формы изменения Профиля EditProfileForm(forms.ModelForm):
# 12. В context_processors.py в функцию add_my_forms(request) добавить 'edit_profile': EditProfileForm()
# 13. В profile.html кнопку Изменить аккаунт и блок Модального окна <div class="modal> со всем содержимым
#  скопировать и вставить ниже тем самым сделали 2 модалку для изминения профиля

# 14. В profile.html во второй модалке кнопку Изменить аккакунт меняем на Изменить профиль
#  так же внести некие изменения  и сделать {{ edit_profile.as_p }}
# 15. Во views.py сделать импорт формы EditProfileForm
# 15. Во views.py создать функцию  edit_profile_view(request) для изменения Профиля
# 16. В urls.py сделать путь для функции edit_profile_view()
# 17. В profile.html во второй модалке в теге form в action прописать {% url 'edit_profile' %}
#   в тег img в src прописать {{ profile.get_photo }} что вытащить фото профиля
#   а в models.py поставить ссылку фото в функ  get_photo  xчто бы по умолчанию была фото маленькая


# 18. В base.html создать тег link и в href прописать {% static 'blog/css/style.css' %}
#   и стиль профиля вставить в файл stule.css




#  -------------------------------- 11 урок 1го месяца --------------------------------------
#  Задачи:
#  1. Сделать автора статьи
#  2. Убрать кнопки изменить и удалить если не явл автором статьи
#  3. Сделать вывод самой просматриваемой статьи и самую последнию в профиле
#  4. Сделать вывод всех статей пользователя в profile.html
#  5.

# 1. В models.py в классе  Article(models.Model) добавить поле автора
# 2. Сделать мигразию что бы сохранить поле автора
# 3. В Админке для каждой статьи поставить Автора admin
# 4. В views.py в классе NewArticle(CreateView): сделать функ def form_valid(self, form):
#    для авторства статьи
# 5. В article_detail.html заменить Автор: Аноним на Автор: {{ article.author }}
# 6. В article_detail.html  Кнопки Изменить, Удалить обернуть  в условие {% if article.author == request.user %}
# 7.  В article_detail.html  Автор: {{ article.author }} обернуть в тег <a>
# #       и в href прописать {% url 'profile' article.author.pk %}


# 8. Во views.py в функции profile_view внести изминения для просмотра и последней публикации
#  дописать articles = Article.objects.filter(author_id=pk)
#  так же most_viewed = articles.order_by('-views')[:1][0]
#  и recent_articles = articles.order_by('-created_at')[:1][0]
#  в context отправить  most_viewed и recent_articles и articles


# 9. В profile.html  вместо слова  "Sam Disuja" поставить тег <a>
#    и прописать {{ recent_articles }} и в href прописать {{ recent_articles.get_absolute_url }}
# 10. В profile.html  вместо слова  'Dinoter husainm' поставить тег <a>
#       внутрь тега прописать {{ most_viewed.title }} а в href  {{ most_viewed.get_absolute_url }}

# 11. В profile.html в самом незу сделать показ статей автора
#   создать блок d-flex внутри него col-8 внутри него цикл {% for article in articles %}
#   и в цикле создать блок <div class="card"> <h3> тег <img> -> {{ article.title }}
#   ниже создать  тег <a> в href прописать {{ article.get_absolute_url }}


#  Если останется время показать парсинг сайта Look.uz























