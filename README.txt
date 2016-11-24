git clone https://github.com/anand-tiwari/patientinfo.git
cd patientinfo
virtualenv hosp
source hosp/bin/activate

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver
