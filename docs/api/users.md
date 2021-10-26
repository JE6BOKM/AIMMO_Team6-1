# Users
Supports registering, viewing, and updating user accounts.

## Register a new user account

**Request**:

`POST` `/api/v1/accounts/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
username   | string | Yes      | The username for the new user.
email      | string | Yes      | The user's email address.
password1  | string | Yes      | The user's given password.
password2  | string | Yes      | The user's given confirm password.

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NDM4MjUwLCJpYXQiOjE2MzUyNjU0NTAsImp0aSI6ImVlOTZiNTY4M2U3OTQ1ODRhZDQ1M2RlOGJmZWE2MDBiIiwidXNlcl9pZCI6Mzl9.yyjxWOM_sp5GxspQbL3uf3F88r2uH2yx6QwwDwW5YBQ",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNTg3MDI1MCwiaWF0IjoxNjM1MjY1NDUwLCJqdGkiOiIxNDU1MGJjNGNlYmU0ODU1YWVhOGU0NTUyMDExYzhhNyIsInVzZXJfaWQiOjM5fQ.psmub1EAfiyTZ9_RmKjX4C14duqji8CCQIPHxmifuEE",
    "user": {
        "pk": 39,
        "username": "guest9",
        "email": "guest9@guest.com",
        "first_name": "",
        "last_name": ""
    }
}
```

The `auth_token` returned with this response should be stored by the client for
authenticating future requests to the API. See [Authentication](authentication.md).


## Get a user's profile information

**Request**:

`GET` `/users/:id`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks",
  "email": "richard@piedpiper.com",
}
```


## Update your profile information

**Request**:

`PUT/PATCH` `/users/:id`

Parameters:

Name       | Type   | Description
-----------|--------|---
first_name | string | The first_name of the user object.
last_name  | string | The last_name of the user object.
email      | string | The user's email address.



*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "6d5f9bae-a31b-4b7b-82c4-3853eda2b011",
  "username": "richard",
  "first_name": "Richard",
  "last_name": "Hendriks",
  "email": "richard@piedpiper.com",
}
```
