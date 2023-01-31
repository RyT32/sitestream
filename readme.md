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
<p>7.  py manage.py runserver - запуск сервера локально </p> 
<p>8. создать папку templates - для хранения html(страничек)  </p> 
<p>9. создать index.html в templates - страничка котораяа будет отображаться  </p> 
<p>10. в main/settins.py в списке INSTALLED_APPS зыписываю свое приложение "home"</p> 
<p>11. в main/settins.py в списке TEMPLATES  в ключе DIRS указать путь в папке templates :<br>
'DIRS': [BASE_DIR/"templates"]
</p>
<p>12. создаем функцию в home/views.py </p>
<p>13. указываю ссылку в main/urls.py и функцию которая будет срабатывать по этому запросу </p>
<p>. </p>
<p>. </p>
<p>. </p>









<br>
<hr>
<p>github - платформа для хранения кода , работы в команде </p> 
<p>.gitignore - файл в готором указываем директории или папки которые не будут отправляться в репозиторий git</p> 