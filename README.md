<ol>
  <li>open this folder on vscode</li>
  <li>select a .py file</li>
  <li>change selected interpreter on the bottom bar</li>
  <li>create a virtual enviroment using the latest python version</li>
  <li>a '.venv' folder should be added to the folder</li>
  <li>
    run the following commands:
    <ul>
      <br>
      <i>Dependencies</i>
      <li>pip install django</li>
      <li>pip install djangorestframework</li>
      <li>pip install django-cors-headers</li>
      <li>pip install pillow</li>
      <br />
      <i>Server set-up</i>
      <li>python manage.py makemigrations</li>
      <li>python manage.py migrate</li>
      <li>python manage.py createsuperuser</li>
      <br />
    </ul>
  </li>
  The following above are only run once, to start the server, run the command
  below:
  <li>python manage.py runserver</li>
</ol>
