package sion.basic;

import sion.basic.member.Grade;
import sion.basic.member.Member;
import sion.basic.member.MemberService;
import sion.basic.member.MemberServiceImpl;
import sion.basic.order.Order;
import sion.basic.order.OrderService;
import sion.basic.order.OrderServiceImpl;

public class OrderApp {
    public static void main(String[] args) {
        MemberService memberService = new MemberServiceImpl();
        OrderService orderService = new OrderServiceImpl();

        Long memberId = 1L;
        Member member = new Member(memberId, "sion", Grade.VIP);
        memberService.join(member);

        Order order = orderService.createOrder(memberId, "itemA", 10000);

        System.out.println("order =" + order);
    }
}
