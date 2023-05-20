from selene import browser, have
from tests.conftest import RESOURCE_PATH
from data.users import User

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
## in high level

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

    def set_date(self, year, month, date):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click()
        browser.all(".react-datepicker__month-select option").element_by(have.exact_text(month)).click()
        browser.element(".react-datepicker__year-select").click()
        browser.all(".react-datepicker__year-select option").element_by(have.exact_text(year)).click()
        browser.all(".react-datepicker__day").element_by(have.exact_text(date)).click()
        return self

    def set_subjects(self, subjects):
        ##browser.element("#subjectsInput").type(first_subjects).press_enter()
        ##browser.element("#subjectsInput").type(second_subjects).press_enter()
        for subject in subjects:
            browser.element('#subjectsInput').type(subject).press_tab()
        return self

    def set_hobbies(self, hobbies):
        ##browser.element('[for="hobbies-checkbox-2"]').click()
        ##browser.all('#hobbiesWrapper .custom-checkbox').element_by(have.exact_text(value)).click()
        for hobbie in hobbies:
            browser.all('#hobbiesWrapper .custom-checkbox').element_by(have.exact_text(hobbie)).click()
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

    def should_registered_user(self, user: User):
        subjects = ', '.join(map(str, user.subjects))
        hobbies = ','.join(map(str, user.hobbies))
        browser.element(".modal-title").should(have.text("Thanks for submitting the form"))
        browser.all(".table").all("td").should(
            have.exact_texts(
                ("Student Name", f"{user.last_name} {user.first_name}"),
                ("Student Email", user.email),
                ("Gender", user.gender),
                ("Mobile", user.phone),
                ("Date of Birth", user.birthday.strftime("%d %B,%Y")),
                ("Subjects", subjects),
                ("Hobbies", hobbies),
                ("Picture", user.upload_picture),
                ("Address", user.current_address),
                ("State and City", f"{user.state} {user.city}")
            )
        )

    def register(self, user: User):
        self.set_user_info(user.last_name, user.first_name)
        self.set_contact_info(user.email, user.phone)
        self.set_gender(user.gender)
        self.set_date(user.birthday.strftime("%Y"),
                      user.birthday.strftime("%B"),
                      user.birthday.strftime("%-d"))
        self.set_subjects(user.subjects)
        self.set_hobbies(user.hobbies)
        self.set_picture(user.upload_picture)
        self.set_current_address(user.current_address)
        self.set_state_and_city(user.state, user.city)



