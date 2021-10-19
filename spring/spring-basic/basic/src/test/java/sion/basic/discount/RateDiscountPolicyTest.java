package sion.basic.discount;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import sion.basic.AppCofing;
import sion.basic.member.Grade;
import sion.basic.member.Member;
import sion.basic.member.MemberService;
import sion.basic.member.MemberServiceImpl;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

class RateDiscountPolicyTest {

    MemberService memberService;
    DiscountPolicy discountPolicy;

    @BeforeEach
    public void beforeEach() {
        AppCofing appCofing = new AppCofing();
        memberService = appCofing.memberService();
        discountPolicy = appCofing.discountPolicy();
    }


    @Test
    @DisplayName("VIP는 10% 할인이 적용되어야 한다.")
    void vip() {
        // given
        Long memberId = 1L;
        Member member = new Member(memberId, "memberA", Grade.VIP);
        memberService.join(member);

        // when
        int discount = discountPolicy.discount(member, 10000);
        // then
        assertThat(discount).isEqualTo(1000);
    }

    @Test
    @DisplayName("VIP가 아니면 할인이 적용되지 않아야 한다.")
    void basic() {
        // given
        Long memberId = 2L;
        Member member = new Member(memberId, "memberB", Grade.BASIC);
        memberService.join(member);

        // when
        int discount = discountPolicy.discount(member, 10000);
        // then
        assertThat(discount).isEqualTo(0);
    }
}