Feature: Practice Form Submission

  Scenario: Successful form submission
    Given the user navigates to Forms > Practice Forms
    When the user fills all required fields with valid data
    And the user clicks the Submit button
    Then display a confirmation message "Thanks for submitting the form"

  Scenario: unsuccessful form submission
    Given the user navigates to Forms > Practice Forms
    When the user enters empty/invalid data "None" in the "first_name" field
    And the user clicks the Submit button
    Then it should not display a confirmation message "Thanks for submitting the form"

  Scenario: form field validation
    Given the user navigates to Forms > Practice Forms
    When the user enters empty/invalid data "abc123" in the "email" field
    And the user clicks the Submit button
    Then the filed should change its color
    And it should not display a confirmation message "Thanks for submitting the form"
