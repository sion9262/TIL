package sion.basic.member;


import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import sion.basic.AppCofing;

public class MemberSerivceTest {
    MemberService memberService;

    @BeforeEach
    public void beforeEach() {
        AppCofing appCofing = new AppCofing();
        memberService = appCofing.memberService();
    }


    @Test
    void join(){
        // given
        Member member = new Member(1L, "sion", Grade.VIP);

        // when
        memberService.join(member);
        Member findMember = memberService.findMember(1L);

        // then
        Assertions.assertThat(member).isEqualTo(findMember);
    }
}
