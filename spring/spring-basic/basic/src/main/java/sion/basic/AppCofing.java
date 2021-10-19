package sion.basic;

import sion.basic.discount.DiscountPolicy;
import sion.basic.discount.RateDiscountPolicy;
import sion.basic.member.MemberService;
import sion.basic.member.MemberServiceImpl;
import sion.basic.member.MemoryMemberRepository;
import sion.basic.order.OrderService;
import sion.basic.order.OrderServiceImpl;

public class AppCofing {

    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    public OrderService orderService() {
        return new OrderServiceImpl(memberRepository(), discountPolicy());
    }

    private MemoryMemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    public DiscountPolicy discountPolicy() {
        return new RateDiscountPolicy();
    }

}
