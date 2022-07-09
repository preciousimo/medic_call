# MedicCall
While buiding another name inspiration came which is MedicCare.🙂🙃
Medic_call helps register complete patient information. It captures and stores the medical history, treatment required, details of their previous visits, upcoming appointments if any, reports, insurance details and more

# Cloning the repository
--> Clone the repository using the command below :

    git clone https://github.com/preciousimo/medic_call
--> Move into the directory where we have the project files :

    cd medic_call

# Create a virtual environment
--> Install virtualenv first:

    pip install virtualenv
--> Create virtual environment:

    virtualenv envname
--> Activate the virtual environment :

    envname\scripts\activate

# Install the requirements :
    pip install -r requirements.txt

# Migrate Database
    python manage.py migrate

# Create Super User
    python manage.py createsuperuser

# To run the App, use :
    python manage.py runserver
Then, the development server will be started at http://127.0.0.1:8000/
    
⚠ Please note that this setup is for windows

## Documentation
You can check up django documentation page for any further information.
[Django Docs](https://docs.djangoproject.com/en/4.0/)
