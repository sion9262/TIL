# RESTful Service 기능 확장

## Validation
- Validation은 사용자가 보낸 데이터와 User 객체에 대해 타입이 맞는시 유효성 검사를 한다.

-`User` 객체에 대해 `@Size` `@Past` 같은 어노테이션을 통해 조건을 설정한다
    - `@Size` min, max 를 통해 String의 길이를 정함
    - `@Past`를 통해 과거의 date만 입력받을 수 있다고 정함.

- `Controller`에 해당 API에 @Valid 어노테이션을 추가한다.
- `ErrorHandler` 는 다음과 같이 정의한다.
```java 
    @Override
    protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException ex, HttpHeaders headers, HttpStatus status, WebRequest request) {
        ExceptionResponse exceptionResponse = new ExceptionResponse(new Date(), ex.getMessage(),
                ex.getBindingResult().toString());
        return new ResponseEntity<>(exceptionResponse, HttpStatus.BAD_REQUEST);
    }
```
- 최신 SpringBoot에서 @Valid를 사용하여면 다음과 같은 의존성을 주어야한다.
```java
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

## Internationalization

## XML format으로 반환

## Filtering

## Version 관리
