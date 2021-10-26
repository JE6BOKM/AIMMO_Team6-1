# Posts
Supports creating, editing, deleting, viewing posts.

## Create a post

**Request**:

`POST` `/api/v1/posts/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
title      | string | Yes      | The title of a post.
content    | string | No       | The content of a post.


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

Name       | Type   | Required | Description
-----------|--------|----------|------------
limit      | string | No       | Limit of entities.
offset     | string | No       | Start point of entity.

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
        },
        {
            "id": 6,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "sample title 3 edited",
            "content": "interesting3  wow",
            "created_at": "2021-10-26T13:50:51+0000"
        }
    ]
}
```


## Update a post

**Request**:

`PUT/PATCH` `/api/v1/posts/:id`

Parameters:

Name       | Type   | Description
-----------|--------|---
title      | string | The title of a post.
content    | string | The content of a post.



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
