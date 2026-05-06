Overview
This project contains automated test scenarios validating UI behavior and API data consistency for a demo web application. The tests focus on:

Dynamic UI interactions
Synchronization handling
Form validation
API vs UI data verification

The framework is designed to be scalable, readable, and maintainable, using best practices like Page Object Model (POM) and reusable utilities.

Test Scenarios Covered
Elements → Checkbox
Objective:
Validate hierarchical checkbox behavior and dynamic UI updates.

Test Coverage:
Dynamically expand all nodes in the checkbox tree.
Select a parent node.

Verify:
All child elements get selected automatically.
Icons representing selection state are correct.

Implementation Details:
Recursive or loop-based tree traversal.
Dynamic locator strategies for nested elements.

Assertions on:
Checkbox state (checked attribute or class)
Icon changes 

Elements → Dynamic Properties
Objective:
Validate delayed UI rendering and dynamic styling changes.

Test Coverage:
Test 1: Visibility After Delay
Wait for button: "Visible after 5 seconds"
Use fluent wait to:
Poll at intervals
Timeout gracefully

Test 2: Dynamic Color Change
Refresh page
Detect button color change after a delay
Validate:
Initial color vs updated color

Implementation Details:
FluentWait / ExplicitWait used instead of sleep
CSS property validation (color)
Page refresh handling

Forms → Practice Forms
Objective:
Validate form input constraints and submission behavior.

Field Validation Tests:
Test 1: Required Fields Validation
Leave mandatory fields empty
Submit form
Assert validation messages appear

Test 2: Invalid Input Format
Enter invalid email
Verify error indications (red border/message)

Form Submission Tests:
Test 1: Successful Submission
Fill all mandatory valid data
Submit form
Verify confirmation popup/modal

Implementation Details:
Input field interaction using clear/sendKeys
Validation message locators
Modal content assertions

Book Store Application → API Validation
Objective:
Ensure UI data matches backend API response.

Test Coverage:
Retrieve book list via API
Extract UI displayed data
Compare:
Book title
Author
Publisher

Implementation Details:
API call using HTTP client (Pyton requests)
JSON parsing
UI data extraction
Data comparison using assertions


How to Execute Tests
One of the key advantages of this framework is its fully automated test discovery and execution.

Simple Execution Command Run In cmd
- cd path/to/your/project
- python -m pip install -r requirements.txt or pip install -r requirements.txt
- pytest

That’s it — no additional parameters or setup required.

What Happens When You Run pytest
When you execute the above command, the framework performs the following steps automatically:

1. Pytest Initialization

pytest.ini is loaded first

It defines:
Test discovery paths (features/)
Reporting configurations (HTML + Allure)

This ensures:
Tests are picked automatically
No need to specify folders manually

2. Feature File Discovery (BDD Flow)
Pytest scans the features/ directory
Identifies all .feature files
Parses scenarios written in Gherkin syntax

3. Step Definitions Execution
Corresponding step implementations are located inside:
features/steps/
Each Gherkin step is mapped to Python methods
This creates a seamless flow from business-readable steps → executable code

4. Test Setup via conftest.py

Before execution begins:
Browser is initialized (e.g., Chrome)
Fixtures are injected (driver, config, test data)
Environment setup is handled centrally

Example responsibilities:
WebDriver setup/teardown
Config loading
Reusable session-level fixtures

Ensures:
No duplication
Clean and maintainable setup

5. Test Execution Flow
For each scenario:
Navigates to required page
Executes UI/API actions via Page Objects

Uses utilities for:
Wait handling
API calls

Assertions validate expected results
Fully modular and reusable structure

6. Automatic Report Generation
After execution completes, two types of reports are generated automatically:

HTML Report
Generated via pytest-html
Stored in:
/reports/html_repotrs

Contains:
Test summary (Pass/Fail)
Execution time
Logs (if enabled)

Allure Report
Allure results are generated during execution
Provides detailed, interactive reporting

Includes:
Step-level execution details
Screenshots (if integrated)
Attachments & logs
Failure trace analysis

View Allure Report
allure serve reports/allure_reports
This will:
Start a local server
Open report in browser automatically

End-to-End Execution Flow Summary
pytest command
     ↓
pytest.ini configuration loaded
     ↓
Feature files discovered (BDD)
     ↓
Step definitions mapped
     ↓
conftest.py initializes setup
     ↓
Tests executed via Page Objects + Utils
     ↓
Assertions performed
     ↓
HTML + Allure reports generated automatically

