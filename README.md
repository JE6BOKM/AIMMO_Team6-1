<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">CRUD project with DRF</h3>

  <p align="center">
    A very simple boarding app with DRF.
    <br />
    <br />
    <br />
  </p>
</p>

<!-- ABOUT THE PROJECT -->
# About The Project

유저 정보를 갖고 게시판을 다루는 프로젝트 입니다.

## Version
- **Python**: 3.9
- **DB**: PostgreSQL 13
- **Django**: 3.2.8

## Built With

* [Django Rest Framework](https://www.django-rest-framework.org/)
* [cookiecutter django rest ](https://github.com/agconti/cookiecutter-django-rest)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)


## Authentication
Using JWT
```
Authorization: Bearer 9944b09199c62b...e4b
```


<!-- USAGE EXAMPLES -->
### Usage
Start the dev server for local development:

```
$ docker-compose up
```

## API Document
```
http://localhost:8001/
```


# Endpoints

## Post API
### Retreive
```
$ curl http://localhost:8000/api/v1/posts/
```
<details>
<summary>response</summary>

```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 6,
            "author": {
                "username": "guest2",
                "email": "guest2@guest.com"
            },
            "title": "sample title 3 edited",
            "content": "interesting3  wow",
            "created_at": "2021-10-26T13:50:51+0000"
        },
        {
            "id": 2,
            "author": {
                "username": "guest1",
                "email": "guest1@guest.com"
            },
            "title": "sample title 2",
            "content": "interesting2",
            "created_at": "2021-10-26T13:29:13+0000"
        }
    ]
}
```

</details>


### List
```
$ curl http://localhost:8000/api/v1/posts/2/
```
<details>
<summary>response</summary>

```
{
    "id": 2,
    "author": {
        "username": "guest1",
        "email": "guest1@guest.com"
    },
    "title": "sample title 2",
    "content": "interesting2",
    "created_at": "2021-10-26T13:29:13+0000"
}
```

</details>

### Delete
```
$ curl -X DELETE http://localhost:8000/api/v1/posts/2/ -H "Authorization: Bearer eajsdfj...asfdasd"
```

### Update
```
$ curl -X PATCH http://localhost:8000/api/v1/posts/2/ -d '{"content": "edit"}' -H "Authorization: Bearer eajsdfj...asfdasd"
```
<details>
<summary>response</summary>

```
{
    "title": "sample title 2",
    "content": "edit"
}
```

<d/etails>

### Create
```
$ curl -X POST http://localhost:8000/api/v1/posts/ -d '{"title":"title", "content": "content"}' -H "Authorization: Bearer eajsdfj...asfdasd"
```
<details>
<summary>response</summary>

```

{
    "title": "title",
    "content": "content"
}

```

<d/etails>

<!-- ROADMAP -->
## Roadmap

- CI/CD
- deploy.
- Unit tests and coverage.
- Front page to see how it workds.



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
