# 컴포넌트스캔

## 컴포넌트 스캔과 의존관계 자동 주입 시작하기

- 스프링 빈을 등록할 때 `@Bean` 이나 `<bean>`을 통해 직접 등록할 빈을 나열했다.
- 하지만 빈이 많아진다면? 관리하기의 어려움이 있다.
- 따라서 스프링 빈을 자동을 등록하는 컴포넌트 스캔이 등장했다.

```java

@Configuration
@ComponentScan
public class AutoAppConfig {}
```

- 컴포넌트 스캔을 사용하려면 `@ComponentScan` 어노테이션을 붙혀주면 된다.
- 컴포넌트 스캔은 `@Component` 어노테이션이 붙어있는 클래스를 스캔하여 스프링 빈으로 등록한다.
- 이전에는 직접 빈도 등록하고 의존관계도 주입하였지만, 이젠 설정 정보가 없기에 의존관계 주입도 이 클래스(컴포넌트 어노테이션이 붙은) 안에서 해결해야한다.
- `@Autowired`는 의존관계를 자동으로 주입해준다.

@Compoent
- 기존과 `AnnotationConfigApplicationContext` 사용은 동일 대신 `AutoAppConfig` 클래스를 넘겨준다.
- @ComponentScan 은 @Component 가 붙은 모든 클래스를 스프링 빈으로 등록한다.
- 이때 스프링 빈의 기본 이름은 클래스명을 사용하되 맨 앞글자만 소문자를 사용한다.
  - 빈 이름 기본 전략: MemberServiceImpl 클래스 memberServiceImpl
  - 빈 이름 직접 지정: 만약 스프링 빈의 이름을 직접 지정하고 싶으면
  @Component("memberService2") 이런식으로 이름을 부여하면 된다.

@Autowired
- 생성자에 @Autowired 를 지정하면, 스프링 컨테이너가 자동으로 해당 스프링 빈을 찾아서 주입한다.
- 이때 기본 조회 전략은 타입이 같은 빈을 찾아서 주입한다.
- getBean(MemberRepository.class) 와 동일하다고 이해하면 된다.


## 탐색 위치와 기본 스캔 대상
- 모든 자바 클래스를 컴포넌트 스캔하면 시간이 오래걸리기에 탐색 위치를 지정해줘야함.

```java 
@ComponentScan(
    basePackages = "sion.basic"
)
```
- `basePackages`: 탐색핧 패키지의 시작 위치를 지정. 이 패키지를 포함해서 하위 패키지를 모두 스캔한다.
  - `basePackages` = {"sion.basic", "sion.basic.service"} 와 같이 여러 시작 위치 지정 가능하다.
- `basePackagesClasses`: 지정한 클래스의 패키지를 탐색 시작 위치로 지정.
- 아무것도 지정하지 않는다면 `@ComponentScan`이 붙은 설정 정보 클래스의 패키지가 시작 위치가 된다.

권장하는 방법
- 프로젝트 최상단에 두어 시작한다.
- 스프링부트에는 `@SpringBootApplication` 안에 `@ComponetScan`이 들어 있다.


스캔 대상
- `@Componet`: 컴포넌트 스캔에서 사용
- `@Controller` : 스프링 MVC 컨트로럴에서 사용
- `@Service`: 스프링 비지니스 로직에서 사용
- `@Repository`스프링 데이터 접근 계층에서 사용
- `@Configuration`:  스프링 설정 정보에서 사용

참고 
사실 애노테이션에는 상속관계라는 것이 없다. 그래서 이렇게 애노테이션이 특정 애노테이션을 들고
있는 것을 인식할 수 있는 것은 자바 언어가 지원하는 기능은 아니고, 스프링이 지원하는 기능이다  

컴포넌트 스캔의 용도 뿐만 아니라 다음 애노테이션이 있으면 스프링은 부가 기능을 수행한다.  
- `@Controller`: 스프링 MVC 컨트롤러로 인식
- `@Repository`: 스프링 데이터 접근 계층으로 인식하고, 데이터 계층의 예외를 스프링 예외로 변환해준다.
- `@Configuration`: 앞서 보았듯이 스프링 설정 정보로 인식하고, 스프링 빈이 싱글톤을 유지하도록 추가
처리를 한다.
- `@Service`: 특별한 처리를 하지 않는다. 대신 개발자들이 핵심 비즈니스 로직이 여기에
있겠구나 라고 비즈니스 계층을 인식하는데 도움이 된다.

## 컴포넌트 필터

- 컴포넌트 스캔은 2가지의 필더가 있음 
  - `includeFilters` : 컴포넌트 스캔 대상을 추가로 지정한다.
  - `excludeFilters` : 컴포넌트 스캔에서 제외할 대상을 지정한다.

어노테이션 정의
```java 

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MyIncludeComponent {
}
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MyExcludeComponent {
}
```

컴포넌트 스캔 정의
```java 
@ComponentScan(
     includeFilters = @Filter(type = FilterType.ANNOTATION, classes = MyIncludeComponent.class),
     excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = MyExcludeComponent.class
    )
```

FilterType은 5가지 옵션이 있다.
- ANNOTATION: 기본값, 애노테이션을 인식해서 동작한다.
  - ex) org.example.SomeAnnotation
- ASSIGNABLE_TYPE: 지정한 타입과 자식 타입을 인식해서 동작한다.
  - ex) org.example.SomeClass
- ASPECTJ: AspectJ 패턴 사용
  - ex) org.example..*Service+
- REGEX: 정규 표현식
  - ex) org\.example\.Default.*
- CUSTOM: TypeFilter 이라는 인터페이스를 구현해서 처리
  - ex) org.example.MyTypeFilter

## 중복 등록과 충돌

컴포넌트 스캔에서 같은 빈 이름이 등록될 때  
1. 자동 빈 등록 vs 자동 빈 등록
2. 수동 빈 등록 vs 자동 빈 등록

자동 빈 등록 vs 자동 빈 등록
- 컴포넌트 스캔에 의해 자동으로 스프링 빈이 등록되는데, 그 이름이 같은 경우 스프링은 오류를 발생시킨다.
  - ConflictingBeanDefinitionException 예외 발생

수동 빈 등록 vs 자동 빈 등록
- 수동 빈이 우선권을 가짐 (자동빈을 오버라이딩 해버린다.)
- 스프링부트부터는 오류가 발생 (설정을 변경하면 오버라이딩 할 수 있다.)