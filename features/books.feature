Feature: Book Store Data Validation

  Scenario: Validate book list against API
    Given the user navigates to the Book Store page
    When the list of books is displayed on the page
    And the user retrieves the list of books from the API
    Then the number of books displayed should equal the number of books in the API
    And the book titles, authors and publishers on the page should match the API response