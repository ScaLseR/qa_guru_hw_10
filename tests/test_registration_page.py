"""автотест на заполнение и отправку формы
https://demoqa.com/automation-practice-form """
from qa_guru_hw_10.pages.registration_page import RegistrationPage


def test_filling_and_send_form():
    registration_page = RegistrationPage()
    registration_page.open_form_page()

    registration_page.fill_first_name('Бобр')
    registration_page.fill_last_name('Добр')
    registration_page.fill_user_email('bobrdobr@test.ru')
    registration_page.fill_gender()
    registration_page.fill_mobile_number('1234567890')
    registration_page.fill_date_of_birth('2022', 'May', '12')
    registration_page.fill_few_subjects(['English', 'Computer Science'])
    registration_page.fill_hobbies('Reading')
    registration_page.add_picture('bobr.jpg')
    registration_page.fill_current_address('Бобриное Болото')
    registration_page.fill_state_and_city('Haryana', 'Karnal')
    registration_page.press_submit()

    registration_page.assert_have_registrated_user('Бобр Добр',
                                                   'bobrdobr@test.ru',
                                                   'Male',
                                                   '1234567890',
                                                   '12 May,2022',
                                                   'English, Computer Science',
                                                   'Reading',
                                                   'bobr.jpg',
                                                   'Бобриное Болото',
                                                   'Haryana Karnal')
