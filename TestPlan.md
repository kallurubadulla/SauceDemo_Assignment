# Test Plan: Swag Labs E-Commerce Platform
**Project:** SDET Assignment - Storewise
**Author:** Kalluru Badulla

## 1. Scope
The scope of this testing project is to verify the end-to-end user journey of the Swag Labs website, focusing on:
* **Authentication:** Validating various user roles (Standard, Locked, Problem).
* **Inventory Management:** Verifying product display and sorting logic.
* **Checkout Flow:** From adding items to the cart to order completion.

## 2. Test Data (User Credentials)
* `standard_user`: Full access to the site.
* `locked_out_user`: Should be denied access with an error message.
* `problem_user`: Exhibits functional and visual bugs for testing.
* `performance_glitch_user`: Exhibits high latency/delay during login.

## 3. Test Cases
| TC ID | Summary | User Role | Priority |
| :--- | :--- | :--- | :--- |
| **TC01** | Verify successful login and landing on Inventory page. | standard_user | High |
| **TC02** | Verify that a locked user receives a clear error message. | locked_out_user | High |
| **TC03** | Verify that products can be added and removed from the cart. | standard_user | Medium |
| **TC04** | Verify that the product sort filter reorders the inventory. | standard_user | Medium |
| **TC05** | Verify successful end-to-end checkout with valid data. | standard_user | High |