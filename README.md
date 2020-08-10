# mini
 A mini app to log and display the time we need to make the cages,at different workstations.
 ![image](https://github.com/jpriyam/mini/blob/master/mini.gif)
Install Python (3.6 or 3.7) 
Install git bash on the laptop
Clone the repository using the following commands on gitbash:

git init  This creates a .git directory that contains the Git configuration files.
Clone the repository and copy the -HTTPS:
 https://gitlab.com/gitlab-org/gitlab.git
Run the command on gitbash - git clone https://gitlab.com/gitlab-org/gitlab.git
Next command will be -git pull origin master
You’ll have to add your gitlab password every time you clone through HTTPS.

      4) if there is a file called requirements.txt use the command 
pip install -r requirement.txt
      5) Open the folder in an editor and open Settings folder
      6) Settings folder ->  env.py
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : '<db_name>',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : ' <db_user>',
        'PASSWORD' : '<db_user_password> ',
    }
}

7) create a database in the with the same name in mysql
8) create a super user with the following commands 
python manage.py createsuperuser
Enter your name and password.
9) Then run 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
In that order 

(In case of an error in manage.py migrate try running 
Python manage.py migrate --run-syncdb to connect to the database)
