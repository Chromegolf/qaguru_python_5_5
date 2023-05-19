import os
from selene import browser, have, command
from conftest import RESOURCE_PATH

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')


    def set_user_info(self, first_name, last_name):
        browser.element("#firstName").type(first_name)
        browser.element("#lastName").type(last_name)
        return self

    def set_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        ##browser.element('[for="gender-radio-1"]').click()
        return self

    def set_contact_info(self, email, phone):
        browser.element("#userEmail").type(email)
        browser.element('[id=userNumber]').type(phone)
        return self

    def set_date(self, month, year, date):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.all(".react-datepicker__day").element_by(have.exact_text(date)).click()
        return self

    def set_subjects(self, first_subjects, second_subjects):
        browser.element("#subjectsInput").type(first_subjects).press_enter()
        browser.element("#subjectsInput").type(second_subjects).press_enter()
        return self

    def set_hobbies(self):
        browser.element('[for="hobbies-checkbox-2"]').click()
        return self

    def set_picture(self, value):
        browser.element('#uploadPicture').set_value(f'{RESOURCE_PATH}/{value}')
        return self

    def set_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def set_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.element('#react-select-3-option-2').should(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-0').should(have.exact_text(city)).click()
        return self

    def submit(self):
        browser.element('#submit').click()

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
