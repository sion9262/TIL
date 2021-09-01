### Web Service
    1. World Wide Web(WWW) 를 이용한 디바이스와 디바이스간의 통신 서비스.
    2. 네트워스 상 특정 포트에 대한 요청에 대한 처리

    네트워크 상에서 서로 다른 종류의 컴퓨터들 간에 상호작용하기 위한 소프트웨어 시스템이다.

    3 Keys
    1. 머신 - 머신 (어플리케이션 - 어플리케이션) 간의 상호작용을 위한 설계
    2. 플랫폼의 종속되지 않음.
    3. 네트워크 상의 커퓨니 케이션
    
    ex) html, css, javascript 등 

### Web Application
    원격 서버에 저장되고 브라우저 인터페이스를 통해 인터넷을 통해 전달되는 응용프로그램
    ex) 웹메일, 온라인 쇼핑몰, 온라인뱅킹 등 

### 웹 서버와 어플리케이션의 관계

    웹 서버는 어플리케이션에게 Request받으면 웹 서버는 Response 해준다.

    Server Definition
    1. Request/Response Format
    2. Request Structure
    3. Response Structure
    4. Endpoint(URL...)

    2가지의 데이터 포맷으로 전달된다.
    1. XML
    2. JSON (많이 사용됨.)

### SOAP
    SOAP(Simple Object Access Protocol)은 XML기반 통신이다.

    포맷 
    SOAP-ENV : Envelope
        SOAP-ENV : Header
        SOAP-ENV : Body
    
    단점 : 복잡한 구조로 인해 오버헤드가 심하며 개발하기가 어려운 단점이있다.

### RESTful
    REST(REpresentational State Transfer)
    - Resource의 Representation에 의한 상태 전달
    - HTTP Method를 통해 Resource를 처리하기 위한 아키텍쳐
    - SOAP 단점을 보안

    RESTful
    - REST API를 제공하는 웹 서비스
    - 자원의 상태를 표현하기 위한 서비스

    REST - HTTP - HTTP Methods (GET, PUT, POST, DELETE)
                - HTTP Status Codes (200, 201, 404, 500 ...)

    Resource
    - URI (Uniform Resource Identifier), 인터넷 자원을 나타내는 유일한 주소
    - XML, HTML, JSON 
    