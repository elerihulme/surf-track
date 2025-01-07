# Testing

## Validation

### HTML

- There were no errors or warnings found when passing the HTML code through the [W3C](https://validator.w3.org/) validator, except for in the sign-up page, which had a few erros due to an unordered list being within a span, which caused the validator to throw an error for tags beofre and after the list. This however was code from the django allauth library, so I am unable to change it.

- This checking was done manually by copying the HTML code from the 'Page Source' and pasting it into the validator, as authentication is required via the URL.

- [Home Page Logged Out User HTML validation report](documentation/validation/logged-out-home-html-validation.png)

- [Home Page Logged In User HTML validation report](documentation/validation/logged-in-home-html-validation.png)

- [My Sessions - No Sessions HTML validation report](documentation/validation/my-sessions-no-sessions-html-validation.png)

- [My Sessions - With Sessions HTML validation report](documentation/validation/my-sessions-with-sessions-html-validation.png)

- [Log Session HTML validation report](documentation/validation/log-session-html-validation.png)

- [Edit Session HTML validation report](documentation/validation/log-session-html-validation.png)

- [Sign Up HTML validation report](documentation/validation/sign-up-html-validation.png)
- [Sign Up Code Error HTML validation report](documentation/validation/sign-up-html-validation-error-code.png)

- [Log In HTML validation report](documentation/validation/log-in-html-validation.png)

- [Log Out HTML validation report](documentation/validation/log-session-html-validation.png)


### CSS

- No errors or warnings were found when passing through the [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator

- [CSS Validation](documentation/validation/css-validation.png)

### JavaScript

No custom JavaScript was used in this project, therefore JavaScript didn't require validation.

### Python

- No errors were found when the code was passed through [CI Python Linter](https://pep8ci.herokuapp.com/). 
- This checking was done manually by copying python code and pasting it into the validator.

- [Surf Sessions - Admin PEP8 validation](documentation/validation/surf-sessions-admin-pep8.png)

- [Surf Sessions - Apps PEP8 validation](documentation/validation/surf-sessions-apps-pep8.png)

- [Surf Sessions - Forms PEP8 validation](documentation/validation/surf-sessions-forms-pep8.png)

- [Surf Sessions - Models PEP8 validation](documentation/validation/surf-sessions-models-pep8.png)

- [Surf Sessions - URLs PEP8 validation](documentation/validation/surf-sessions-urls-pep8.png)

- [Surf Sessions - Views PEP8 validation](documentation/validation/surf-sessions-views-pep8.png)

- [Surf Track - asgi PEP8 validation](documentation/validation/surf-track-asgi-pep8.png)

- [Surf Track - Settings PEP8 validation](documentation/validation/surf-track-settings-pep8.png)

- [Surf Track - URLs PEP8 validation](documentation/validation/surf-track-urls-pep8.png)

- [Surf Track - wsgi PEP8 validation](documentation/validation/surf-track-wsgi-pep8.png)

## Lighthouse Report

- I encountered issues loading the page when running the loghthouse report myself, however someone else was able to run it for me.
- But I have since improved the accessibility

- [Lighthouse Report](documentation/testing/lighthouse-report.png)


## Manual Testing

| Page              | User Actions                                | Expected Results                                           | Y/N | Comments                          |
|-------------------|---------------------------------------------|------------------------------------------------------------|-----|-----------------------------------|
| Home Page         |                                             |                                                            |     |                                   |
| 1                 | View latest sessions                        | Sessions displayed in reverse chronological order          | Y   |                                   |
| 2                 | Click "View Details" button                 | Opens modal with full session details                      | Y   |                                   |
| 3                 | Click pagination next/previous              | Navigates through sessions                                 | Y   |                                   |
| 4                 | Click "Log Session" button                  | Redirects to Log Session form                              | Y   |                                   |
| 5                 | Click logo                                  | Redirects to home page                                     | Y   |                                   |
| **Modal**         | Click "View Details" button                 | Opens modal with session details                           | Y   |                                   |
|                   | Click "Close" button                        | Modal closes                                               | Y   |                                   |
|                   | Click outside modal                         | Modal closes                                               | Y   |                                   |
|                   | View session details                        | Full details of surf session displayed                     | Y   |                                   |
|-------------------|---------------------------------------------|------------------------------------------------------------|-----|-----------------------------------|
| My Sessions       |                                             |                                                            |     |                                   |
| 1                 | View personal sessions                      | Displays user's surf sessions                              | Y   |                                   |
| 2                 | Click "Edit" button                         | Redirects to Edit Session page                             | Y   |                                   |
| 3                 | Click "Delete" button                       | Opens delete confirmation modal                            | Y   |                                   |
| 4                 | Confirm delete                              | Session is deleted and success message is displayed        | Y   |                                   |
| 5                 | Cancel delete                               | Modal closes without deleting session                      | Y   |                                   |
| 6                 | Paginate through sessions                   | Displays next or previous set of sessions                  | Y   |                                   |
| **Modal**         | Click "Delete" button                       | Opens delete confirmation modal                            | Y   |                                   |
|                   | Click "Cancel"                              | Modal closes without deletion                              | Y   |                                   |
|                   | Confirm delete                              | Session is deleted and modal closes                        | Y   |                                   |
|-------------------|---------------------------------------------|------------------------------------------------------------|-----|-----------------------------------|
| Log In            |                                             |                                                            |     |                                   |
| 1                 | Click on Log In button                      | Redirects to Log In page                                   | Y   |                                   |
| 2                 | Click on the Sign Up link in the form       | Redirects to Sign Up page                                  | Y   |                                   |
| 3                 | Enter valid email                           | Field only accepts email address format                    | Y   |                                   |
| 4                 | Enter valid password                        | Field only accepts password format                         | Y   |                                   |
| 5                 | Click on Log In button                      | Redirects to home page with success message                | Y   |                                   |
| 6                 | Click logout button                         | Redirects to home page                                     | Y   |                                   |
| 7                 | Click browser back button                   | User remains logged out                                    | Y   |                                   |
| 8                 | Click Remember Me checkbox                  | Remembers user                                             | Y   |                                   |
|-------------------|---------------------------------------------|------------------------------------------------------------|-----|-----------------------------------|
| Log Out           |                                             |                                                            |     |                                   |
| 1                 | Click on "Logout" button                    | Redirects to logout confirmation page                      | Y   |                                   |
| 2                 | Confirm logout                              | User is logged out and redirected to home page             | Y   |                                   |
| 3                 | Click browser back button                   | User remains logged out                                    | Y   |                                   |
|-------------------|---------------------------------------------|------------------------------------------------------------|-----|-----------------------------------|
| Sign Up           |                                             |                                                            |     |                                   |
| 1                 | Click on Sign Up button                     | Redirects to Sign Up page                                  | Y   |                                   |
| 2                 | Click on the Login link in the form         | Redirects to Login page                                    | Y   |                                   |
| 3                 | Enter valid email 2 times                   | Field only accepts email address format                    | Y   |                                   |
| 4                 | Enter valid password 2 times                | Field only accepts password format                         | Y   |                                   |
| 5                 | Click on Sign Up button                     | Sends confirmation request email                           | Y   |                                   |
| 6                 | Confirm email                               | Redirects to Sign In page                                  | Y   |                                   |
| 7                 | Sign In after registration                  | Redirects to home page with success messag                 | Y   |                                   |
|-------------------|---------------------------------------------|------------------------------------------------------------|-----|-----------------------------------|
| Navigation        |                                             |                                                            |     |                                   |
| 1                 | Click on the logo                           | Redirects to home page                                     | Y   |                                   |
| 2                 | Click "My Sessions"                         | Redirects to My Sessions page                              | Y   |                                   |
| 3                 | Click "Log Session"                         | Redirects to Log Session page                              | Y   |                                   |
| 4                 | Click "Logout"                              | Redirects to logout page                                   | Y   |                                   |
| 5                 | Click "Sign Up"                             | Redirects to Sign Up page                                  | Y   |                                   |
| 6                 | Click "Login"                               | Redirects to Log In page                                   | Y   |                                   |
|-------------------|---------------------------------------------|------------------------------------------------------------|-----|-----------------------------------|


## User Story Testing

## Compatibility and Responsiveness

The website was tested on Chrome, Mozilla, Edge and Safari browsers with no problems found.

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. 
It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

- [Home Page Logged Out User Responsive](documentation/testing/home-logged-out-responsive.png)

- [Home Page Logged In User Responsive](documentation/testing/home-logged-in-responsive.png)

- [My Sessions - No Sessions Responsive](documentation/testing/my-sessions-no-sessions-responsive.png)

- [My Sessions - With Sessions Responsive](documentation/testing/my-sessions-with-sessions-responsive.png)

- [Log Session Responsive](documentation/testing/log-session-responsive.png)

- [Edit Session Responsive](documentation/testing/edit-session-responsive.png)

- [Sign Up Responsive](documentation/testing/sign-up-responsive.png)

- [Log In Responsive](documentation/testing/log-in-responsive.png)

- [Log Out Responsive](documentation/testing/log-out-responsive.png)

## Bugs