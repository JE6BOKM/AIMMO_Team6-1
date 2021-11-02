# Comments

Supports creating, editing, deleting, viewing comments.

## Create a comments

**Request**:

`POST` `/api/v1/comments/`

Parameters:

| Name    | Type   | Required | Description                   |
| ------- | ------ | -------- | ----------------------------- |
| comment | string | Yes      | The content of comment        |
| post    | int    | Yes      | The post with comments.       |
| parent  | int    | No       | The parent comment of comment |

_Note:_

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
    "post": 1,
    "comment": "New comments"
}
```

## List of comments.

**Request**:

`GET` `/api/v1/comments/`

Parameters:

| Name    | Type   | Required | Description                              |
| ------- | ------ | -------- | ---------------------------------------- |
| limit   | string | No       | Limit of entities.                       |
| offset  | string | No       | Start point of entity.                   |
| post_id | int    | No       | Filter to see comments on specific posts |

_Note:_

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 12,
    "next": "http://localhost:8000/api/v1/comments/?limit=3&offset=3&post_id=1",
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": {
                "id": 1,
                "username": "test",
                "email": "test@test.com"
            },
            "post": 1,
            "created_at": "2021-11-02T01:01:36+0000",
            "updated_at": "2021-11-02T01:01:36+0000",
            "parent": null,
            "comment": "New Comments",
            "reply": []
        },
        {
            "id": 2,
            "user": {
                "id": 1,
                "username": "test",
                "email": "test@test.com"
            },
            "post": 2,
            "created_at": "2021-11-02T01:09:01+0000",
            "updated_at": "2021-11-02T01:09:01+0000",
            "parent": null,
            "comment": "NewComments",
            "reply": [
                {
                    "id": 3,
                    "user": {
                        "id": 1,
                        "username": "test",
                        "email": "test@test.com"
                    },
                    "post": 2,
                    "created_at": "2021-11-02T01:15:07+0000",
                    "updated_at": "2021-11-02T01:15:07+0000",
                    "parent": 2,
                    "comment": "NewReply",
                    "reply": []
                },
                {
                    "id": 4,
                    "user": {
                        "id": 1,
                        "username": "test",
                        "email": "test@test.com"
                    },
                    "post": 2,
                    "created_at": "2021-11-02T01:15:31+0000",
                    "updated_at": "2021-11-02T01:15:31+0000",
                    "parent": 2,
                    "comment": "NewReply2",
                    "reply": []
                }
            ]
        },
        {
            "id": 5,
            "user": {
                "id": 1,
                "username": "test",
                "email": "test@test.com"
            },
            "post": 2,
            "created_at": "2021-11-02T01:29:49+0000",
            "updated_at": "2021-11-02T01:32:23+0000",
            "parent": null,
            "comment": "NewComment3",
            "reply": []
        }
    ]
}
```

## Update a post

**Request**:

`PUT/PATCH` `/api/v1/comments/:id`

Parameters:

| Name    | Type   | Required | Description                   |
| ------- | ------ | -------- | ----------------------------- |
| comment | string | Yes      | The content of comment        |
| post    | int    | Yes      | The post with comments.       |
| parent  | int    | No       | The parent comment of comment |

_Note:_

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "id":5,
    "user":{
        "id":1,
        "username":"test",
        "email":"test@test.com"
    },
    "post":2,
    "created_at":"2021-11-02T01:29:49+0000",
    "updated_at":"2021-11-02T02:52:22+0000",
    "parent":null,
    "comment":"NewComment3",
    "reply":[]
}
```

## Delete a post

**Request**:

`DELETE` `/api/v1/comments/:id`

_Note:_

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
204 No Content

```
