from package.registration_page import RegistrationPage

def test_student_registration_form():

    reg_page = RegistrationPage()

    reg_page.open()

    (
        reg_page

        .set_user_info('Ivan', 'Ivanov')
        .set_gender('Male')
        .set_contact_info('ivanov@gmail.com', '8800100300')
        .set_date('August', '1990', '1')
        .set_subjects('Computer Science', 'English')
        .set_hobbies()
        .set_picture('test_picture.png')
        .set_current_address('Russia, Moscow')
        .set_state_and_city('Haryana', 'Karnal')
    )
    reg_page.submit()

    '''
        reg_page.open()
        reg_page.set_user_info('Ivan', 'Ivanov')
        reg_page.set_gender('Male')
        reg_page.set_contact_info('ivanov@gmail.com', '8800100300')
        reg_page.set_date('August', '1990', '1')
        reg_page.set_subjects('Computer Science', 'English')
        reg_page.set_hobbies()
        reg_page.set_picture('test_picture.png')
        reg_page.set_current_address('Russia, Moscow')
        reg_page.set_state_and_city('Haryana', 'Karnal')
        reg_page.submit()
        '''

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
