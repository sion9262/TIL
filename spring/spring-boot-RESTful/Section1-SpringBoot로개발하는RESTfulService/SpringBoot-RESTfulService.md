### SpringBoot란?

    SpringBoot란? 단독 실행 가능한 어플리케이션이다.
    Spring을 이용하면 많은 설정 작업이 필요하지만,
    SpringBoot을 이용하면 간단한 설정으로 바로 실행할 수 있다.

    SpringBoot에는 이미 Tomcat, Jetty 등 내장되어 있다.
    Spring 실행에 필요한 많은 API는 starter에 이미 설정되어있다.
    
[프로젝트 생성](https://start.spring.io/) 

    SpringBoot를 싱행하기 위해서는 @SpringBootApplication 어노테이션을 붙혀야함.

### 프로젝트 생성

    Project : Maven vs Gradle
    Language : Java vs Kotlin vs Groovy
    Version : 원하시는 버전
    Project Metadata 
        Group : 개발하고자하는 회사의 이름 그룹의 이름 등..
        Artiface : 생성하고자 하는 어플리케이션의 이름 

    Dependencies : 사용하고자 하는 라이브러리 

### 프로젝트 정의
    게시판 CRUD에 대한 RESTful Service

    User -> Posts (1:N)


|Description|REST API|HTTP Method|
|:---:|:---:|:---:|
|Retrieve all Users|/users|GET|
|Create a User|/users|POST|
|Retrieve one User|/users/{id}|GET|
|Delete a User|/users/{id}|DELETE|
|Retrieve all posts for a User|/users/{id}/posts|GET|
|Create a posts for a User|/users/{id}/posts|POST|
|Retrieve details of a User|/users/{id}/posts/{post_id}|GET|

### Spring Boot 동작 원리
    설정 파일 application.yml or application.properties

    ex ) properties
    logging.level.org.springframework = debug
    
    ex) yml
    logging:
        level:
            org.springframework : debug

    yml 포맷이 직관적이게 설정파일을 작성할 수 있다.

### DispatcherServlet
    1. 클라이언트의 모든 요청을 한곳으로 받아서 처리
    2. 요청에 맞는 Handler로 요청을 전달
    3. Handler의 실행 결과를 Http Response 형태로 만들어서 반환
    
    기존 
    Request -> DispatcherServlet -> Handler Mapping -> Controller -> ViewResolver -> View

    Spring4부터 @RestController 지원
    @RestController = @Controller + @ResponseBody
    View를 갖지 않는 REST Data(JSON/XML)를 변환 
    
    RESTful Web Services Container
    Request -> DispatcherServlet -> Handler Mapping -> REST Controller -> Response

### Path Variable
    URL에 변수를 넣는 방식
    ex) http://localhost:8080/books/ - 전체 책 조회 
    ex) http://localhost:8080/books/1 or http://localhost:8080/books/123 - 특정 책 조회

    @GetMapping(path="/books/{id}")
    public Book GetBook(@PathVariable String id) ... 