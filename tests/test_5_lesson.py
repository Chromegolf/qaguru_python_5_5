from selene import browser
from selene import have

from package.resource import path


class RegistrationPage:

    def __init__(self):
        pass

    def open(self):
        browser.open('/automation-practice-form')

    def set_user_info(self, first_name, last_name):
        browser.element("#firstName").type(first_name)
        browser.element("#lastName").type(last_name)

    def set_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        ##browser.element('[for="gender-radio-1"]').click()

    def set_contact_info(self, email, phone):
        browser.element("#userEmail").type("ivanov@gmail.com")
        browser.element('[id=userNumber]').type('8800100300')

    def set_date(self, month, year, date):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.all(".react-datepicker__day").element_by(have.exact_text(date)).click()

    def set_subjects(self, first_subjects, second_subjects):
        browser.element("#subjectsInput").type(first_subjects).press_enter()
        browser.element("#subjectsInput").type(second_subjects).press_enter()

    def set_hobbies(self):
        browser.element('[for="hobbies-checkbox-2"]').click()

    def set_picture(self):
        browser.element('#uploadPicture').set_value(path('foto.jpg'))

    def set_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def set_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.element('#react-select-3-option-2').should(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-0').should(have.exact_text(city)).click()

    def should_registered_user(self, full_name, email, gender, phone, full_date, subjects_list, hobbies,
                               picture, current_address, place):
        browser.element(".modal-title").should(have.text("Thanks for submitting the form"))
        browser.all(".table").all("td").should(
            have.exact_texts(
                ("Student Name", full_name),
                ("Student Email", email),
                ("Gender", gender),
                ("Mobile", phone),
                ("Date of Birth", full_date),
                ("Subjects", subjects_list),
                ("Hobbies", hobbies),
                ("Picture", picture),
                ("Address", current_address),
                ("State and City", place)
            )
        )


def test_student_registration_form():
    reg_page = RegistrationPage()
    reg_page.open()
    reg_page.set_user_info('Ivan', 'Ivanov')
    reg_page.set_gender('Male')
    reg_page.set_contact_info('ivanov@gmail.com', '8800100300')
    reg_page.set_date('August', '1990', '1')
    reg_page.set_subjects('Computer Science', 'English')
    reg_page.set_hobbies()
    reg_page.set_picture()
    reg_page.set_current_address('Russia, Moscow')
    reg_page.set_state_and_city('Haryana', 'Karnal')

    browser.element('#submit').click()

    reg_page.should_registered_user(
        "Ivan Ivanov",
        "ivanov@gmail.com",
        "Male",
        "8800100300",
        "01 August,1990",
        "Computer Science, English",
        "Reading",
        "test_picture.png",
        "Russia, Moscow",
        "Haryana Karnal"
    )
