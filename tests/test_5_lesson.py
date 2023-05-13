from selene import browser
from selene import have, command
import os

def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanov")
    browser.element("#userEmail").type("ivanov@gmail.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id=userNumber]').type('1234567890')

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.all(".react-datepicker__month-select option").element_by(have.exact_text("August")).click()
    browser.element(".react-datepicker__year-select").click()
    browser.all(".react-datepicker__year-select option").element_by(have.exact_text("1990")).click()
    browser.all(".react-datepicker__day").element_by(have.exact_text("1")).click()

    browser.element("#subjectsInput").type("Computer Science").press_enter()
    browser.element("#subjectsInput").type("English").press_enter()

    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').set_value(os.path.join(os.path.abspath('test_picture.jpg')))