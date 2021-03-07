# Sign In / Sign Out

- Using Django Authentication module for logging in and logging out users.

  | Modules                          | Use Case           | Params                                           |
  | -------------------------------- | ------------------ | ------------------------------------------------ |
  | authenticate(username, password) | Verify Credentials | username & password                              |
  | login(request, user)             | Sign In            | request & user obj (generated from authenticate) |
  | logout(request)                  | Sign out           | request obj                                      |

## [Sign In Form](https://getbootstrap.com/docs/4.0/examples/sign-in/)

- View Page source
- Copy relevant items to your page
- Change fields to requirement
- Add POST method and action to redirect form submission required to the desired view

### Todo

- Sign Up
