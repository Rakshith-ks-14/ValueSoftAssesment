DemoQA BDD Test Suite
This project contains BDD-style automated tests (using pytest-bdd + Selenium) for validating different modules of the DemoQA application.
The tests cover UI behavior, dynamic properties, form validation, and API data correctness.

Features Tested
1. Elements > Checkbox
Dynamically expand the tree at all levels.

Tick a parent node and assert that all nested elements show the correct icons.

2. Elements > Dynamic Properties
Fluently wait for the button with text “Visible after 5 seconds” to be displayed.

Refresh the page and verify that the second button changes color after some time.

3. Forms > Practice Forms
Field Validation Tests

Required field validation.

Invalid email format validation.

Form Submission Tests

Successful form submission with valid data.

Prevent duplicate submission.

4. Book Store Application
Retrieve the list of books displayed on the UI.

Call the /BookStore/v1/Books API.

Validate that the UI data (title, author, etc.) matches the API response.

Tech Stack
Python 3.9+

pytest – test runner

pytest-bdd – BDD framework

Selenium WebDriver – browser automation

requests – API validation

pytest-html – HTML reporting

allure-pytest – Allure reporting
