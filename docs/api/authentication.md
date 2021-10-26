# Authentication
For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Bearer", with whitespace separating the two strings. For example:

```
Authorization: Bearer 9944b09199c62b...e4b
```

Unauthenticated responses that are denied permission will result in an HTTP `401 Unauthorized` response with an appropriate `WWW-Authenticate` header. For example:

```
WWW-Authenticate: Bearer
```

The curl command line tool may be useful for testing token authenticated APIs. For example:

```bash
curl -X GET http://127.0.0.1:8000/api/v1/example/ -H 'Authorization: Bearer 9944b09199c62b...e4b'
```

## Retrieving Tokens
Authorization tokens are issued and returned when a user registers. A registered user can also retrieve their token with the following request:

**Request**:

`POST` `/api/v1/accounts/login/`

Parameters:

Name | Type | Description
---|---|---
email | string | The user's email
password | string | The user's password

**Response**:
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NDM4OTk0LCJpYXQiOjE2MzUyNjYxOTQsImp0aSI6IjFlNmQyZjg0NDk2MjQ2OTdiNzIyYWVjYzgxYjA3MTNhIiwidXNlcl9pZCI6Mzl9.ilPYnR5yjeJVOoP9vEJqDvhzrJfhBSdnUiifBiaXPcs",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNTg3MDk5NCwiaWF0IjoxNjM1MjY2MTk0LCJqdGkiOiIwZDdiMWM2NDUwODk0YTUyOTViYjJiODQyMGNjMTNlYyIsInVzZXJfaWQiOjM5fQ.E5gVqoEW18uh91vyILFE52DJ4MwEf4Guy_pA-QOI4o0",
    "user": {
        "pk": 39,
        "username": "guest9",
        "email": "guest9@guest.com",
        "first_name": "",
        "last_name": ""
    }
}
```
