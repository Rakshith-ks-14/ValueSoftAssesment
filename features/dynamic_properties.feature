Feature: Dynamic Properties Page

  Scenario: Verify dynamic button visibility and color change
    Given navigate to Elements > Dynamic Properties
    When fluently wait for the button with text Visible after "30" seconds to be displayed
    Then the button should be visible on the page

    When refresh the page
    Then the second button should change its color after some time "30"