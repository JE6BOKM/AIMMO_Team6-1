<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">[Assignment 1] 에이모</h3>

  <p align="center">
    
    <br />
    <br />
    <br />
  </p>
</p>

<!-- ABOUT THE PROJECT -->

## About The Project

유저 정보를 갖고 게시판을 다루는 프로젝트 입니다.  
다음의 내용이 REST API로 구현되어 있습니다.  
유저 생성과 로그인  
게시글 생성, 수정, 삭제 및 게시글 카테고리 구분, 게시글 검색  
댓글과 대댓글 생성, 수정, 삭제  
Unit Test

<br>

## 배포 주소

아래 URL을 사용하여 REST API 요청을 할 수 있습니다.

<br>

## 참여 맴버

### 신재민

- Test code 작성
  - User 생성, 로그아웃
  - 게시글 CRUD
  - 댓글 CRUD
- Mongodb와 Django 연동

### 김민규

- 게시글 카테고리 필드 추가 및 필터링
- 게시글 검색
- 게시글 읽힘 수 (동일 유저 no counting)

### 강성묵

- 댓글, 대댓글 CRUD 구현
- 댓글 Pagination
- aws에 프로젝트 배포

<br>

## Requirements

- 원티드 지원 과제 내용 포함
- 게시글 카테고리
- 게시글 검색
- 대댓글(1 depth)
  - 대댓글 pagination
- 게시글 읽힘 수
  - 같은 User가 게시글을 읽는 경우 count 수 증가하면 안 됨
- Rest API 설계
- Unit Test
- 1000만건 이상의 데이터를 넣고 성능테스트 진행 결과 필요

## Version

- **Python**: 3.9
- **DB**: Mongodb 5.0
- **Django**: 3.2.8

## Built With

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [cookiecutter django rest ](https://github.com/agconti/cookiecutter-django-rest)

## 구현 방법과 이유에 대한 간략한 설명

### 사용자

- 사용자 생성 시 계정과 email 그리고 password 와 password 확인으로 생성 가능합니다.
- 사용자 생성과 로그인 시 jwt 토큰을 발행하며, 2일간 사용 가능합니다.

### 게시물

- 게시물을 보는 것은 누구나 볼 수 있습니다.
- 게시물을 생성, 삭제, 수정을 하려면 로그인을 해야 하며, 삭제, 수정은 게시물을 작성한 사용자만 할 수 있습니다.

### 댓글

- 댓글을 보는것은 누구나 볼 수 있습니다.
- 댓글을 생성, 삭제, 수정을 하려면 로그인을 해야 하며, 삭제, 수정은 댓글을 생성한 사용자가 할 수 있습니다.
- comment 항목 중 parent가 없다면 메인 댓글 parent(int) 값을 갖고 있다면 해당 comment_id의 대댓글입니다.
- 댓글과 대댓글을 읽어올 시 기본 10개의 limit 옵션이 적용되며 offset,limit parameter로 변경 가능합니다.

## Postman api document

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

### Runserver with Docker

```
$ docker-compose up
```

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

### ENDPOINT

| Method | EndpointURL                        | Request Body                      | Remark                        |
| :----: | ---------------------------------- | --------------------------------- | ----------------------------- |
|  POST  | /user/accounts/                    | name, email, password1, password2 | 회원가입                      |
|  POST  | /user/accounts/login               | email, password                   | 로그인                        |
|  POST  | /posts/                            | title, content, category          | 게시물 작성                   |
|  GET   | /posts/                            |                                   | 게시물 조회                   |
|  GET   | /posts/{post_id}                   |                                   | 게시물 조회                   |
| DELETE | /posts/{post_id}                   |                                   | 게시물 삭제                   |
|  PUT   | /posts/{post_id}                   | title, content, category          | 게시물 수정                   |
|  GET   | /posts/list?offset=&limit=         |                                   | 게시물 목록 조회              |
|  GET   | /posts/list?search=                |                                   | 게시물 검색 (검색어로 검색)   |
|  GET   | /posts/list?category={category_id} |                                   | 게시물 검색 (카테고리로 검색) |
|  POST  | /comments/                         | post, comment                     | 댓글 작성                     |
|  GET   | /comments/                         |                                   | 전체 댓글 목록 조회           |
|  GET   | /comments/?post_id={post_id}       |                                   | post_id 댓글 목록 조회        |
|  PUT   | /comment/{comment_id}              | comment                           | 댓글/대댓글 수정              |
| DELETE | /comment/{comment_id}              |                                   | 댓글/대댓글 삭제              |
|  POST  | /comments/                         | post, comment, parent             | 대댓글 작성                   |

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.
