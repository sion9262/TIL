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