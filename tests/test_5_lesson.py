from data.users import User, Gender, Subject, Hobby
from package.registration_page import RegistrationPage
from datetime import date

def test_student_registration_form():
    #GIVEN
    student = User(
        first_name='Ivan',
        last_name='Ivanov',
        email='ivanov@gmail.com',
        phone='8800100300',
        gender=Gender.male.value,
        birthday=date(1990, 8, 1),
        subjects=[Subject.computer_science.value, Subject.english.value],
        hobbies=[Hobby.reading.value],
        upload_picture='test_picture.png',
        current_address='Russia, Moscow',
        state='Haryana',
        city='Karnal'
    )

    reg_page = RegistrationPage()
    reg_page.open()

    #WHEN
    reg_page.register(student)
    reg_page.submit()

    #THEN
    reg_page.should_registered_user(student)