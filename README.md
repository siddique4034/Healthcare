Healthcare

A Django-based healthcare web application that connects patients with doctors. The platform allows doctors to share blog posts on various health topics, while patients can browse through these posts and book appointments with doctors.

Features

For Patients

View a list of all doctors with profile pictures and names.

Book an appointment by selecting a specialization, date, and time.

View all blog posts published by doctors.

Filter blog posts by categories such as Mental Health, Heart Disease, Covid-19, and Immunization.


For Doctors

Create and publish blog posts with a title, image, category, summary, and content.

Manage appointments booked by patients.

Integration with Google Calendar to manage appointment schedules.


Installation

1. Clone the repository:

git clone https://github.com/siddique4034/Healthcare.git
cd Healthcare


2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'


3. Install dependencies:

pip install -r requirements.txt


4. Apply migrations:

python manage.py migrate


5. Create a superuser (for admin access):

python manage.py createsuperuser


6. Run the development server:

python manage.py runserver



API Integration

Google Calendar API is used for scheduling appointments. Ensure you have the necessary API keys configured in the project settings.


Tech Stack

Backend: Django, Django REST Framework

Frontend: HTML, CSS, JavaScript

Database: PostgreSQL / SQLite

APIs: Google Calendar API


Contributing

Contributions are welcome! To contribute:

1. Fork the repository.


2. Create a new branch (feature-branch).


3. Commit your changes.


4. Push to your fork and create a pull request.



License

This project is open-source and available under the MIT License.

Contact

For any queries, feel free to reach out:

GitHub: siddique4034
