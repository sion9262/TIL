package sion.basic.order;

import sion.basic.discount.DiscountPolicy;
import sion.basic.discount.FixDiscountPolicy;
import sion.basic.member.Member;
import sion.basic.member.MemberRepository;
import sion.basic.member.MemoryMemberRepository;

public class OrderServiceImpl implements OrderService{
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    private final DiscountPolicy discountPolicy = new FixDiscountPolicy();

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}
