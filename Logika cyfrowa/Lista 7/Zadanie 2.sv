module tff(output q, nq, 
           input t, clk, nrst);
  logic ns, nr, ns1, nr1, j, k;
  nand n1(ns, clk, j), n2(nr, clk, k),
  n3(q, ns, nq), n4(nq, nr,  q, nrst), n5(ns1,!clk, t, nq), 
  n6(nr1, !clk, t, q), n7(j, ns1, k), n8(k, nr1, j, nrst);
  endmodule
module syncnt(output  [2:0] q,
              input en, clk, nrst, down);
  logic [2:0]tmp;
  tff t1(q[0],tmp[0],en , clk, nrst);
  tff t2(q[1],tmp[1],((down?  tmp[0]: q[0]) & en),clk,nrst );
  tff t3(q[2],tmp[2],((down? tmp[0] & tmp[1] : q[0] & q[1]) & en), clk, nrst);
endmodule