"""автотест на заполнение и отправку формы
https://demoqa.com/automation-practice-form """
from qa_guru_hw_10.pages.registration_page import RegistrationPage
from qa_guru_hw_10.data.user import User


def test_filling_and_send_form():
    registration_page = RegistrationPage()
    registration_page.open_form_page()

    bobr = User(first_name='Бобр',
                last_name='Добр',
                email='bobrdobr@test.ru',
                gender='Male',
                mobile_number='1234567890',
                day_of_birth='12',
                month_of_birth='May',
                year_of_birth='2022',
                subject_first='English',
                subject_second='Computer Science',
                hobbies='Reading',
                picture='bobr.jpg',
                current_address='Бобриное Болото',
                state='Haryana',
                city='Karnal')

    registration_page.open_form_page()
    registration_page.register(bobr)
    registration_page.assert_have_registered_user(bobr)

