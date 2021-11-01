# Posts
Supports creating, editing, deleting, viewing posts.

## Search posts

**Request**:

`GET` `/api/v1/posts/?search=ap`


Parameters:

| Name   | Type   | Required | Description          |
| ------ | ------ | -------- | -------------------- |
| search | string | Yes      | The title of a post. |


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
category 없을 때.
```json
Content-Type application/json
404 Not found

```

```json
Content-Type application/json
200 Ok

{
    "count": 5,
    "next": "http://localhost:8000/api/v1/posts/?limit=3&offset=3",
    "previous": null,
    "results": [
        {
            "id": 8,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "ㅁㅁㅁㅁㅁ",
            "content": "ㅁㄴㅇㄹ",
            "created_at": "2021-10-26T15:42:25+0000"
        },
        {
            "id": 7,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "sㅁㄴㅇㄹ",
            "content": "interesㅁㄴㅇㄹting3",
            "created_at": "2021-10-26T15:41:46+0000"
        }
    ]
}
```


## Filter posts

**Request**:

`GET` `/api/v1/posts/?category=fruits`

Parameters:

| Name     | Type   | Required | Description          |
| -------- | ------ | -------- | -------------------- |
| category | string | Yes      | The title of a post. |


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
category 없을 때.
```json
Content-Type application/json
404 Not found

```

```json
Content-Type application/json
200 Ok

{
    "count": 5,
    "next": "http://localhost:8000/api/v1/posts/?limit=3&offset=3",
    "previous": null,
    "results": [
        {
            "id": 8,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "ㅁㅁㅁㅁㅁ",
            "content": "ㅁㄴㅇㄹ",
            "created_at": "2021-10-26T15:42:25+0000"
        },
        {
            "id": 7,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "sㅁㄴㅇㄹ",
            "content": "interesㅁㄴㅇㄹting3",
            "created_at": "2021-10-26T15:41:46+0000"
        }
    ]
}
```


## Create a post

**Request**:

`POST` `/api/v1/posts/`

Parameters:

| Name    | Type   | Required | Description            |
| ------- | ------ | -------- | ---------------------- |
| title   | string | Yes      | The title of a post.   |
| content | string | No       | The content of a post. |


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
    "title": "Today I learned",
    "content": "Django Rest Framework"
}
```

## List of posts.

**Request**:

`GET` `/api/v1/posts/`

Parameters:

| Name   | Type   | Required | Description            |
| ------ | ------ | -------- | ---------------------- |
| limit  | string | No       | Limit of entities.     |
| offset | string | No       | Start point of entity. |

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 5,
    "next": "http://localhost:8000/api/v1/posts/?limit=3&offset=3",
    "previous": null,
    "results": [
        {
            "id": 8,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "ㅁㅁㅁㅁㅁ",
            "content": "ㅁㄴㅇㄹ",
            "read_cnt": 3,
            "created_at": "2021-10-26T15:42:25+0000"
        },
        {
            "id": 7,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "sㅁㄴㅇㄹ",
            "content": "interesㅁㄴㅇㄹting3",
            "read_cnt": 3,
            "created_at": "2021-10-26T15:41:46+0000"
        },
        {
            "id": 6,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "sample title 3 edited",
            "content": "interesting3  wow",
            "read_cnt": 3,
            "created_at": "2021-10-26T13:50:51+0000"
        }
    ]
}
```


## Update a post

**Request**:

`PUT/PATCH` `/api/v1/posts/:id`

Parameters:

| Name    | Type   | Description            |
| ------- | ------ | ---------------------- |
| title   | string | The title of a post.   |
| content | string | The content of a post. |



*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "title": "sample title 3 edited",
    "content": "interesting  wow"
}
```


## Delete a post

**Request**:

`DELETE` `/api/v1/posts/:id`


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
204 No Content

```


# Comments

## List comments

**Request**:

`GET` `/api/v1/posts/:id/comments/`


Parameters:

| Name | Type   | Required | Description          |
| ---- | ------ | -------- | -------------------- |
| id   | string | Yes      | The title of a post. |


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
```json
Content-Type application/json
200 Ok

{
    "count": 5,
    "next": "http://localhost:8000/api/v1/posts/1/comments",
    "previous": null,
    "results": [
        {
            "post_id": 12,
            "user": 3,
            "comments": [
                {
                    "parent_comment_id": 2,
                    "comment_id": 1,
                    "user": 1,
                    "content": "안녕하세요"
                },
                {
                    "parent_comment_id": 2,
                    "comment_id": 1,
                    "user": 1,
                    "content": "안녕하세요"
                }
            ]
        },
        {
            "post_id": 23,
            "user": 4,
            "comments": [
                {
                    "parent_comment_id": 2,
                    "comment_id": 1,
                    "user": 1,
                    "content": "asdf"
                },
                {
                    "parent_comment_id": 2,
                    "comment_id": 1,
                    "user": 1,
                    "content": "안녕s하세32f요"
                }
            ]
        }
    ]
}
```

```json
Content-Type application/json
200 Ok

{
    "count": 5,
    "next": "http://localhost:8000/api/v1/posts/1/comments",
    "previous": null,
    "results": [
        {
            "post_id": 2,
            "user": 1,
            "content": "하하",
            "comments": [
                {
                    "comment_id": 2,
                    "user": 1,
                    "content": "하하",
                }
            ]
        }
    ]
}
```


## Create 1depth comment

**Request**:

`GET` `/api/v1/posts/:id/comments/`


Parameters:

| Name | Type   | Required | Description          |
| ---- | ------ | -------- | -------------------- |
| id   | string | Yes      | The title of a post. |


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
```
{
    "post_id": 12,
    "user": 3,
    "content": "wow"
}
```

## Create 2depth comment

**Request**:

`GET` `/api/v1/posts/:id/comments/:id/`


Parameters:

| Name | Type   | Required | Description          |
| ---- | ------ | -------- | -------------------- |
| id   | string | Yes      | The title of a post. |


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
```
{
    "comment_id": 12,
    "user": 3,
    "content": "wow"
}
```

## Delete 1depth comment

**Request**:

`DELETE` `/api/v1/posts/:id/comments/:id/`


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
```json
Content-Type application/json
204 No Content

```


## Delete 2depth comment

**Request**:

`DELETE` `/api/v1/posts/:id/comments/:id/:id/`


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:
```json
Content-Type application/json
204 No Content

```



## Update 1depth comment

**Request**:

`PUT/PATCH` `/api/v1/posts/:id/comments/:id/`

Parameters:

| Name    | Type   | Description            |
| ------- | ------ | ---------------------- |
| content | string | The content of a post. |


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "post_id": 12,
    "user": 3,
    "content": "wow"
}
```

## Update 2depth comment

**Request**:

`PUT/PATCH` `/api/v1/posts/:id/comments/:id/:id/`

Parameters:

| Name    | Type   | Description            |
| ------- | ------ | ---------------------- |
| content | string | The content of a post. |


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "comment_id": 12,
    "user": 3,
    "content": "wow"
}
```
