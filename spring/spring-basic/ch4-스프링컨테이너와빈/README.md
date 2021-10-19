# 스프링 컨테이너와 스프링 빈

```java
// 스프링 컨테이너 생성
ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppCofing.class);
```
- `ApplicationContext`를 스프링 컨테이너라고 한다. (ApplicationContext는 인터페이스)
- 스프링 컨테이너는 `XML` or 어노테이션 기반의 자바 설정 클래스로 만들 수 있다.
- `AnnotationConfigApplicationContext`는 `ApplicationContext`의 구현체이다.

## 생성 과정

1. 스프링 컨테이너 생성
   1. 스프링 빈 저장소를 생성한다.
   2. 이때 구성 정보를 지정해줘야 한다.
2. 스프링 빈 등록
   1. 빈 이름은 메서드 이름을 사용한다.
   2. 빈 이름을 직접 부여할 수 있다. (@Bean(name="newBean"))
   3. 이때 모든 빈의 이름은 다르게 부여해야한다.
3. 스프링 빈 의존관계 설정 - 준비
4. 스프링 빈 의존관계 설정 - 완료
   1. 스프링 컨테이너는 설정 정보를 참고해서 의존관계를 주입한다.
   2. 단순히 자바 코드를 호출하는 것 같지만, 차이가 있다.

스프링은 빈을 생성하고, 의존관계를 주입하는 단계가 나누어져 있다.
그런데 이렇게 자바 코드로 작성하면 생성자를 호출하면서 의존관계 주입도 한번에 처리된다.
(사실은 나누어져 있음.)

## 컨테이너에 등록된 모든 빈 조회

- 모든 빈 출력하기
  - `ac.getBeanDefinitionNames()`
  - `ac.getBean()`
- 애플리케이션 빈 출력하기
  - 내가 등록한 빈만 출력
  - `getRole()` 로 구분한다.
    - `ROLE_APPLICATION` : 사용자 정의 빈

## 빈 조회

빈 조회 방식은 3가지

1. 빈 이름으로 조회 `ac.getBean("memberService", MemberService.class);`
2. 타입으로만 조회 `ac.getBean(MemberService.class);`
3. 구체타입으로 조회 `ac.getBean("memberService", MemberServiceImpl.class);`

마지막 구체타입으로 조회는 쓰이지 않음(MemberServiceImpl에 의존하기 때문)    

만약 없는 빈을 조회 했다면 `NoSuchBeanDefinitionException` 에러가 발생.

## 빈 타입 조회
- 만약 타입으로 조회시 같은 타입이 2개 이상있으면 중복 오류 발생 `NoUniqueBeanDefinitionException`
- 따라서 빈 이름을 지정하여 조회해아함.
- 특정 타입을 모두 조회하기
```java 
Map<String, MemberRepository> beansOfType = ac.getBeansOfType(MemberRepository.class);
for (String key : beansOfType.keySet()) {
   System.out.println("key = " + key + " value = " + beansOfType.get(key));
}
System.out.println("beansOftYPE = " + beansOfType);
```

## 빈 조회 - 상속 관계
- 부모 타입으로 조회하면, 자식 타입도 함께 조회됨.
- 모든 자바 객체의 최고 부모인 `Object`타입으로 조회하면, 모든 스프링 빈을 조회.
```java
Map<String, Object> beansOfType = ac.getBeansOfType(Object.class);
for (String key : beansOfType.keySet()) {
   System.out.println("key = " + key + " value = " + beansOfType.get(key));
}
```

## BeanFactory와 ApplicationContext

다음과 같은 순서로 상속된다.  
BeanFactory <- ApplicationContext <- AnnotationConfigApplicationContext  

- BeanFactory
  - 스프링 컨테이너의 최상위 인터페이스.
  - 스프링 빈을 관리하고 조회하는 역할을 담당.
  - `getBean()` 제공
- ApplicationContext
  - BeanFactory를 상속받아 제공한다.
  - 둘의 차이는?
  - 애플리케이션을 개발할 때는 빈을 관리, 조회하는 기능은 물론이고, 수 많은 부가기능이 필요
  - 제공 기능
    - 메세지소스를 이용한 국제화 기능 (한국에서 들어오면 한국어, 미국에서 들어오면 영어)
    - 환경 변수 (로클, 개발, 운영등을 구분해서 처리)
    - 애플리케이션 이벤트 (이벤트를 발행하고 구독하는 모델을 편리하게 지원)
    - 편리한 리소스 조회 (파일, 클래스패스, 외부 등에서 리소스를 편리하게 조회)

## 다양한 설정 형식 지원 - 자바코드, XML, Groovy 등...
- 자바코드 설정 사용
  - `new AnnotationConfigApplicationContext(AppConfig.class)`
- XML 설정 사용

```java
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="memberService" class="sion.basic.member.MemberServiceImpl">
        <constructor-arg name="memberRepository" ref="memberRepository"/>
    </bean>


    <bean id="orderService" class="sion.basic.order.OrderServiceImpl">
        <constructor-arg name="memberRepository" ref="memberRepository"/>
        <constructor-arg name="discountPolicy" ref="discountPolicy"/>
    </bean>
    <bean id="memberRepository" class="sion.basic.member.MemoryMemberRepository"/>
    <bean id="discountPolicy" class="sion.basic.discount.RateDiscountPolicy"/>
</beans>
```

## 스프링 빈 설정 메타 정보 - BeanDefinition
- 스프링은 어떻게 다양한 설정 형식을 지원할 까?
  - `BeanDefinition`이라는 추상화가 있어서다.
- 역할과 구현을 개념적으로 나움.
  - XML을 읽어서 BeanDefinition을 만들면 됨.
  - 자바 코드를 읽어서 만들면 됨.
  - 스프링 컨테이너는 자바 코드인지, XML인지 몰라도 된다.
- `BeanDefinition`을 빈 설정 메타정보라 한다.
  - `@Bean`, `<bean>`당 각각 하나씩 메타 정보가 생성된다.
- 스프링 컨테이너는 이 메타정보를 기반으로 스프링 빈을 생성한다.
- 보면 `reader`가 있어 그걸로 파일을 읽게된다.

## 정리

- `BeanDefinition`을 직접 생성해서 스프링 컨테이너에 등록할 수 있다.
- 스프링이 다양한 형태의 설정 정보를 `BeanDefinition`으로 추상화해서 사용하는 것이다.