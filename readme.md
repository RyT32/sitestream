<h1>Инструкция</h1>
<h3>Виртуальное окружение (ВО) - это папка где будут храниться библиотеки для определенного проекта</h3>
<h4>в терминале:</h4>
<hr>
 <p>1. python -m venv venv</p>

<p>2. venv/Scripts/activate - включение ВО</p>
<p> ЕСЛИ на 2 шаге вылезает ошибка  "выполнение сценариев отключено в этой системе"<br>
нужно открыть PowerShell от имени администратора и вставить команду -> Set-ExecutionPolicy RemoteSigned <br>
на вопрос ответить  A (Да для всех)
</p>

<p>Теперь скачиваем библиотеки</p>
<p>3. pip install django            -     фреймворк для созднания бэкенда и фронтенда(но обычно фронт на нем не делают)</p>
<p>4. pip install djangorestframework         - создание API     </p>  
<hr>
<br>
<h1>DJANGO</h1>
<p>5. django-admin startproject main .       - создание проекта с именем main (вы можете писать другое)</p>  
<p>6. py manage.py startapp home       - создание приложения с именем home (вы можете писать другое)</p> 
<p> web приложение - это отдельная логическая часть отвечающая за определенные функционал <br>
например : вход оплата главная_страница чат профиль 
<p>7.  py manage.py runserver - запуск сервера локально <br>
переходим по ссылке http://127.0.0.1:8000/ </p> 
<p>8. создать папку templates и media - для хранения html(страничек) и медиафайлов </p> 
<p>9. создать index.html в templates - страничка котораяа будет отображаться  </p> 
<p>10. в main/settings.py в списке INSTALLED_APPS зыписываю свое приложение "home"</p> 
<p>11. в main/settings.py в списке TEMPLATES  в ключе DIRS указать путь в папке templates :<br>
'DIRS': [BASE_DIR/"templates"]
<p>в конце добавляем путь к медиа файлам:<br>MEDIA_ROOT = os.path.join(BASE_DIR, 'media')<br>
MEDIA_URL = '/media/'</p>
</p>
<p>12. создаем функцию в home/views.py </p>
<p>13. указываю ссылку в main/urls.py и функцию которая будет срабатывать по этому запросу </p>
<p>14. python manage.py migrate  - делаем миграции (преобразуем python коде через систему ORM  в  sql-заросы) </p>
<hr>
<h2>Создание БД</h2>
<p>15. В models.py создаем свою модель </p>
<hr>
<h2> Структура проекта<р2>
<ul>


<li>article</li>
<li>card</li>
<li>catalog</li>
<li>home</li>
<li>main</li>


<li>accounts</li>
<li>api</li>

<li>templates</li>
<li>media</li>
</ul>




<hr>
<p>.API работа_с_сслыками фронт  </p>









<br>
<hr>
<p>github - платформа для хранения кода , работы в команде </p> 
<p>.gitignore - файл в готором указываем директории или папки которые не будут отправляться в репозиторий git</p> 