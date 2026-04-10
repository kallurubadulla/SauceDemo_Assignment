# Bug Report: Swag Labs Manual Testing
**Environment:** Windows 11 | Chrome Browser

| Bug ID | Summary | Severity | Steps to Reproduce | Expected vs Actual |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | Asset Mismatch: Product images show dogs. | Medium | 1. Login as `problem_user` | **E:** Correct product images. **A:** All images show a dog. |
| **BUG-02** | Functionality: "Add to Cart" button broken. | High | 1. Login as `problem_user` 2. Click Fleece Jacket | **E:** Item added to cart. **A:** Button is unresponsive. |
| **BUG-03** | UI Logic: Sorting filter fails to reorder. | Medium | 1. Login as `problem_user` 2. Change sort filter | **E:** List reorders. **A:** Order remains static. |
| **BUG-04** | Checkout: Last Name field clears itself. | High | 1. Login as `problem_user` 2. Enter checkout info | **E:** Field saves text. **A:** Field resets/fails to save. |
| **BUG-05** | Performance: Login delay (5 seconds). | Low | 1. Login as `performance_glitch_user` | **E:** Instant login. **A:** 5-second loading delay. |