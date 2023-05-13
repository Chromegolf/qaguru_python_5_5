from selene import browser
from selene import have, command
import os

def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanov")
    browser.element("#userEmail").type("ivanov@gmail.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id=userNumber]').type('8800100305')

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.all(".react-datepicker__month-select option").element_by(have.exact_text("August")).click()
    browser.element(".react-datepicker__year-select").click()
    browser.all(".react-datepicker__year-select option").element_by(have.exact_text("1990")).click()
    browser.all(".react-datepicker__day").element_by(have.exact_text("1")).click()

    browser.element("#subjectsInput").type("Computer Science").press_enter()
    browser.element("#subjectsInput").type("English").press_enter()

    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').set_value(os.path.join(os.path.abspath('test_picture.png')))

    browser.element('#currentAddress').type('Russia, Moscow')
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').should(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.exact_text('Karnal')).click()
    browser.element('#submit').click()

    browser.element(".modal-title").should(have.text("Thanks for submitting the form"))
    browser.all(".table").all("td").should(
        have.exact_texts(
            ("Student Name", "Ivan Ivanov"),
            ("Student Email", "ivanov@gmail.com"),
            ("Gender", "Male"),
            ("Mobile", "8800100305"),
            ("Date of Birth", "01 August,1990"),
            ("Subjects", "Computer Science, English"),
            ("Hobbies", "Reading"),
            ("Picture", "test_picture.png"),
            ("Address", "Russia, Moscow"),
            ("State and City", "Haryana Karnal")
        )
    )