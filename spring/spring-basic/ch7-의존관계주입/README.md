# 의존관계 자동주입.

## 다양한 의존관계 주입 방법

의존관계 주입은 다음과 같은 방법이 있다.

### 생성자 주입
- 생성자를 통해 주입 받는 방법이다.
- 특징
  - 생성자 호출시점에 딱 1번 호출됨.
  - 불변, 필수 의존관계에 사용
- 만약 생성자가 1개라면 `@Autowired` 생략가능  
- 룸복을 사용하면 생성자 메서드를 사용하지 않아도 `@RequiredArgsConstructor`를 사용하면 final이 붙은 필드를 모아서 생성자를 자동으로 만들어줌.
### 수정자 주입(setter)
- `setter`를 통해 필드의 값을 변경.
- 특징
  - 선택, 변경 가능성이 있는 의존관계에 사용
- 만약 `@Autowired`의 기본 동작은 주입할 대상이 없으면 오류 발생.
- 수정자 주입시 Bean이 없어도 동작하게 하려면 `@Autowired(required = false)사용

### 필드 주입 (테스트할 때만 사용하는 것을 권장)
- `@Autowired MemberRepository memberRepository` 방식
- 외부 변경이 불가능해서 테스트하기 힘들다는 치명적인 단점. (순수 자바 코드일 때.)
- DI프레임워크가 없으면 아무것도 할 수 없음.
- 스프링 설정을 목적으로 하는 `@Configuration` 같은 곳에서만 특별한 용도로 사용

### 일반 메서드 주입
- `public void init(MemberRepository memberRepository){ ... } `일반 메서드를 통해 주입받는다 
- 특징
  - 한번에 여러 필드를 주입 받을 수 있음.
  - `setter` 주입과 비슷하지만, 여러 개를 한번에 받을 수 있다는 장점이있다.


참고 의존관계는 스프링 컨테이너가 관리하는 스프링 빈이여만 등록가능하다.  
아무 곳이나 `@Autowired` 쓴다고 주입받는 것이 아니다.

## 옵션 처리

만약 스프링 빈이 없어도 동작하게 하려면?
- `@Autowired(required = false)` 을 한다.
- 일반적인 방식은 아예 매서드가 호출이 되지 않음.
- `@Nullable`, `Optional<>` 통해 비어있는 값을 받을 수 있다.
```java 
//호출 안됨
@Autowired(required = false)
public void setNoBean1(Member member) {
System.out.println("setNoBean1 = " + member);
}
//null 호출
@Autowired
public void setNoBean2(@Nullable Member member) {
System.out.println("setNoBean2 = " + member);
}
//Optional.empty 호출
@Autowired(required = false)
public void setNoBean3(Optional<Member> member) {
System.out.println("setNoBean3 = " + member);
}
```

## 의존관계 주입 선택 정리
- 생성자 주입을 권장한다.

불변  
1. 대부분의 의존관계는 한번 일어나면 종료시 까지 의존관계를 변경할 일이 없다. 변하면 안된다.
2. 수정자 주입을 사용하려면 `public` 메서드인데, 누군가 실수로 변경할 수 있으므로 좋은 설계 방법이 아님.

누락
1. 순수 자바코드로 테스트하는 경우 `필드 주입`일 경우 의존관계 주입이 불가능하다.
2. 생성자 주입을 사용하면 주입데이터가 누락 됬을때 컴파일 오류 발생.
3. 생성자 주입을 사용하면 필드에 `final`키워드를 사용하는데 만약 값이 설정되지 않으면 오류를 컴파일 시점에서 막아준다. (런타임 중 오류가 났다 생각하면....)

## 조회 빈이 2개 이상이면?

1. 기본적으로 `@Autowired`는 타입으로 빈을 조회한다.  
2. 하지만, `DiscountPolicy`의 하위 타입인 `FixDscountPolicy`, `RateDiscountPolicy` 둘다 빈으로 등록한다면?  
3. `NoUniqueBeanDefinitionException` 오류가 발생한다.
4. 하위 타입으로 지정할 수  있지만, DIP위배하고 유연성이 떨어지므로 다음과 같은 방법으로 해결한다.

## @Autowired 필드명, @Qualifier, @Primay

1. `@Autowired` 필드명 매칭
- `@Autowired`는 타입으로 매칭을 시도하고 안될 경우 필드 이름, 파라미터 이름으로 매칭함.

```java 
// 기존
@Autowired
private DiscountPolicy discountPolicy
// 수정
@Autowired
private DiscountPolicy rateDiscountPolicy
```

2. `@Qualifier` 사용
- `@Qualifier` 추가 구분자를 붙여 매칭한다. (빈 이름을 변경하는 것이 아님)
- 빈 등록시 `@Qualifier`를 뿥혀준다.

```java 
@Component
@Qualifier("mainDiscountPolicy")
public class RateDiscountPolicy implements DiscountPolicy {}

@Component
@Qualifier("fixDiscountPolicy")
public class FixDiscountPolicy implements DiscountPolicy {}
```

주입 시에도 다음과 같이 붙혀준다.

```java 
public OrderServiceImpl(MemberRepository memberRepository,
@Qualifier("mainDiscountPolicy") DiscountPolicy
discountPolicy){...}
```

- 만약 `mainDiscountPolicy`를 못찾는 다면 `mainDiscountPolicy`라는 스프링 빈을 추가로 찾는다.
- 그래도 없으면 `NoSuchBeanDefinitionException`에러

3. `@Primary` 사용
- `@Primary`는 우선순위를 정하는 방법이다. 
- `@Autowired` 시 여러 빈이 매칭되면 `@Primary`가 우선권을 가짐.

```java 
@Component
@Primary
public class RateDiscountPolicy implements DiscountPolicy {}
```

우선순위
- `@Primary`는 기본값 처럼 동작, `@Qualifier`는 상세하게 동작. 즉 자동보다는 수동이 우선 순위가 높다. 
- `@Qualifier`가 우선순위가 더 높음

ex)
- `@Primary`는 메인 DB로 설정
- `Qualifier`는 서브 DB로 설정

4. 에노테이션 직접 만들기
- `@Qualifier("mainDiscountPolicy")` 이렇게 문자를 적으면 컴파일시 타입 체크가 안된다.
- 어노테이션을 만들어 문제를 해결 할 수 있음.

```java 
// MainDiscountPolicy

@Target({ElementType.FIELD, ElementType.METHOD, ElementType.PARAMETER,
ElementType.TYPE, ElementType.ANNOTATION_TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented@Qualifier("mainDiscountPolicy")
public @interface MainDiscountPolicy {...}

// RateDiscountPolicy

@Component
@MainDiscountPolicy
public class RateDiscountPolicy implements DiscountPolicy {}

// OrderServiceImpl

@Autowired
public OrderServiceImpl(MemberRepository memberRepository, @MainDiscountPolicy DiscountPolicy discountPolicy) {
  this.memberRepository = memberRepository;
  this.discountPolicy = discountPolicy;
}
```

- 어노테이션은 상속이라는 개념이 없음. 전부 스프링이 지원해 주는 기능이다.
- 무분별한 재정의는 유지보수에 혼란만 가중할 수 있다.

## 조회한 빈이 모두 필요할 때 , List, Map
- 할인과 관련된 서비스를 제공하는데, 클라이언트가 할인의 종류를 선택할 수 있다고 가정한다면?
- DiscountService Class 생성 후 `DiscountPolicy`로 등록된 모든 빈을 가져온다.
- `discount()` 함수 실행 시 `discountCode`라는 빈 이름을 받아 그에 맞는 빈을 `get()`으로 가져온 후 로직을 처리한다.
```java 

// DiscountService
private final Map<String, DiscountPolicy> policyMap;
private final List<DiscountPolicy> policies;

public DiscountService(Map<String, DiscountPolicy> policyMap, List<DiscountPolicy> policies) {
    this.policyMap = policyMap;
    this.policies = policies;
}

public int discount(Member member, int price, String discountCode) {
    return policyMap.get(discountCode).discount(member, price);
}
```

## 자동, 수동의 올바른 실무 운영 기준
- 자동을 선호하는 추세 (자동 빈 등록을 사용해도 OCP, DIP를 지킬 수 있다.)
- 자동을 사용할 경우
  - 업무 로직 빈 : 웹 컨트롤러, 핵심 비지니스 로직이 있는 서비스, 데이터 계층의 로직처리 등.. 보통 비지니스 요구사항을 개발할 떄 추가되거나 변경된다.
- 수동을 사용할 경우
  - 기술 지원 빈 : AOP를 처리할 때 주로 사용. 데이터베이서 연결, 공통 로그 처리 처럼 업무 로직을 지원하기 위한 하부 기술이나 공통 기술들에 사용
  - 비지니스 로직 중에서 다형성을 적극 활용할 때. 다른 개발자가 보기 좋으려면 수동 빈등록을 하거나 특정 패키지에 같이 묶어 사용
  