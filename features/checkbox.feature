Feature: Checkbox Tree

  Scenario: Expand and select parent node
    Given the Elements > Checkbox page is open
    When the tree is expanded at all levels
    And the parent node "Documents" is ticked
    Then all nested elements under "Documents" have correct checked icons