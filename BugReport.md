# Bug Report: Swag Labs Manual Testing
**Environment:** Windows 11 | Chrome Browser

| Bug ID | Summary | Severity | Steps to Reproduce | Expected vs Actual |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | Asset Mismatch: Product images show dogs. | Medium | 1. Login as `problem_user` | **E:** Correct product images. **A:** All images show a dog. |
| **BUG-02** | Functionality: "Add to Cart" button broken. | High | 1. Login as `problem_user` 2. Click Fleece Jacket | **E:** Item added to cart. **A:** Button is unresponsive. |
| **BUG-03** | UI Logic: Sorting filter fails to reorder. | Medium | 1. Login as `problem_user` 2. Change sort filter | **E:** List reorders. **A:** Order remains static. |
| **BUG-04** | Checkout: Last Name field clears itself. | High | 1. Login as `problem_user` 2. Enter checkout info | **E:** Field saves text. **A:** Field resets/overwrites First Name. |
| **BUG-05** | Performance: Login delay (5 seconds). | Low | 1. Login as `performance_glitch_user` | **E:** Instant login. **A:** 5-second loading delay. |
| **BUG-06** | Logic: Checkout proceeds with empty cart. | High | 1. Go to Cart with 0 items. 2. Click Checkout. | **E:** Prevent checkout. **A:** Proceeds to info page. |
| **BUG-07** | Input: Postal Code accepts alphabetical text. | High | 1. Enter 'ABCDE' in Postal Code field. | **E:** Show error. **A:** Accepts invalid format. |
| **BUG-08** | Login Error: Missing Password Requirement. | Low | 1. Leave both fields empty. 2. Click Login. | **E:** Mention both fields. **A:** Only mentions Username. |
| **BUG-09** | Validation: Reports only first missing field. | Medium | 1. Leave all checkout fields blank. | **E:** List all missing fields. **A:** Only lists the first one. |
| **BUG-10** | UI: Checkout Overview missing item quantity. | Low | 1. Navigate to Checkout Step 2. | **E:** Show 'Qty' per item. **A:** Quantity column is missing. |
| **BUG-11** | Blocker: Cannot finish checkout process. | Critical | 1. `problem_user`: Complete checkout info. | **E:** Reach Overview. **A:** Form data corruption blocks progress. |
| **BUG-12** | Detail Page: Wrong product image persists. | High | 1. `problem_user`: Open product detail. | **E:** Correct image. **A:** Shows the dog image. |
| **BUG-13** | JS Error: Add to cart triggers crash. | Critical | 1. `error_user`: Click Add to cart. | **E:** Item added. **A:** Console throws JS error. |
| **BUG-14** | Cart Logic: "Remove" button fails to act. | High | 1. `error_user`: Click Remove on cart item. | **E:** Item removed. **A:** Item stays in cart. |
| **BUG-15** | Filter Error: Sort triggers UI crash. | High | 1. `error_user`: Change sort dropdown. | **E:** Sort works. **A:** Triggers internal error. |
| **BUG-16** | Layout: Cart Icon Misplacement. | Medium | 1. Login as `visual_user`. | **E:** Cart in header. **A:** Icon shifted out of position. |
| **BUG-17** | UI: Sort Dropdown Overlap. | Medium | 1. `visual_user`: Check sort dropdown. | **E:** Neatly aligned. **A:** Overlaps product grid. |
| **BUG-18** | Visual: Product Detail Image offset. | Low | 1. `visual_user`: Open product detail. | **E:** Image centered. **A:** Shifted too far left. |
| **BUG-19** | Styling: Wrong Checkout button color. | Low | 1. `visual_user`: View cart page. | **E:** Standard green. **A:** Inconsistent styling/color. |
| **BUG-20** | Navigation: Add to cart redirects user. | High | 1. `problem_user`: Click Add for Onesie. | **E:** Stay on page. **A:** Unexpected navigation. |
