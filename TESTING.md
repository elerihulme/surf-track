# Testing

## Validation

### HTML

### CSS

### JavaScript

No custom JavaScript was used in this project, therefore JavaScript didn't require validation.

### Python

### Lighthouse



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

## Responsiveness

## Compatibility

## Bugs