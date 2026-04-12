# Swag Labs SDET Automation Framework

This repository contains a professional test automation framework for the SauceDemo e-commerce platform. It demonstrates a scalable approach to software testing using Python, Selenium, and Pytest.

## Key Features
* Global Fixtures: Centralized WebDriver management in conftest.py for clean setup and teardown.
* Automation Coverage: End-to-end testing of critical user flows including Login, Checkout, and Error Handling.
* Manual QA Insight: Comprehensive Bug Report detailing 5 distinct defects.
* Scalable Architecture: Organized with Python packages to support Page Object Model (POM) design patterns.

## Tech Stack
* Language: Python 3.x
* Framework: Pytest
* Tool: Selenium WebDriver
* Driver Management: WebDriver Manager

## Project Structure
SauceDemo_Assignment/
├── pages/                # Page Object Model classes
│   └── login_page.py
├── tests/                # Test scripts
│   └── test_sauce.py
├── conftest.py           # Global Pytest fixtures
├── BugReport.md          # Manual testing findings
├── TestPlan.md           # Testing strategy and test cases
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

## Setup and Execution

1. Clone the repository:
   git clone https://github.com/kallurubadulla/SauceDemo_Assignment.git
   cd SauceDemo_Assignment

2. Install dependencies:
   pip install -r requirements.txt

3. Run the tests:
   python -m pytest

## Bug Discovery Summary
As part of the manual exploratory testing, 5 distinct bugs were identified and detailed in BugReport.md:
1. Asset Mismatch: Incorrect product images for specific user roles.
2. Functional Blocker: Unresponsive Add to Cart buttons.
3. UI Logic: Failure of inventory sorting functionality.
4. Data Integrity: Checkout form fields failing to retain input.
5. Performance: Significant login latency for the performance_glitch_user.

---
Author: Kalluru Badulla
