"""Класс для страницы регистрации https://demoqa.com/automation-practice-form"""
from selene import have, command
from os import path
from selene.support.shared import browser
from qa_guru_hw_10.data.user import User


class RegistrationPage:

    def open_form_page(self) -> None:
        browser.open('/automation-practice-form')

    def _fill_first_name(self, value: str) -> None:
        browser.element('#firstName').type(value)

    def _fill_last_name(self, value: str) -> None:
        browser.element('#lastName').type(value)

    def _fill_user_email(self, value: str) -> None:
        browser.element('#userEmail').type(value)

    def _fill_gender(self) -> None:
        browser.element('[for="gender-radio-1"]').click()

    def _fill_mobile_number(self, value: str) -> None:
        browser.element('#userNumber').type(value)

    def _fill_date_of_birth(self, year: str, month: str, day: str) -> None:
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def _fill_few_subjects(self, subject_first: str, subject_second: str) -> None:
        browser.element('#subjectsInput').type(subject_first).press_enter().type(subject_second).press_enter()

    def _fill_hobbies(self, value) -> None:
        browser.all('.custom-control').element_by(have.exact_text(value)).click()

    def _add_picture(self, value: str) -> None:
        browser.element("#uploadPicture").send_keys(path.abspath(value))

    def _fill_current_address(self, value: str) -> None:
        browser.element('#currentAddress').type(value)

    def _fill_state_and_city(self, state: str, city: str) -> None:
        browser.element('[id="state"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('[id="city"]').click()
        browser.all('[id^="react-select"][id*=option]').element_by(have.exact_text(city)).click()

    def _press_submit(self) -> None:
        browser.element('#submit').perform(command.js.click)

    def assert_have_registered_user(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.mobile_number,
                f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
                f'{user.subject_first}, {user.subject_second}',
                user.hobbies,
                user.picture,
                user.current_address,
                f'{user.state} {user.city}'
            )
        )

    def register(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_user_email(user.email)
        self._fill_gender()
        self._fill_mobile_number(user.mobile_number)
        self._fill_date_of_birth(user.year_of_birth, user.month_of_birth, user.day_of_birth)
        self._fill_few_subjects(user.subject_first, user.subject_second)
        self._fill_hobbies(user.hobbies)
        self._add_picture(user.picture)
        self._fill_current_address(user.current_address)
        self._fill_state_and_city(user.state, user.city)
        self._press_submit()
