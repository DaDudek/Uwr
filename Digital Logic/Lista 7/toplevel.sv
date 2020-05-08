module tff(output q, nq, 
           input t, clk, nrst);
  logic ns, nr, ns1, nr1, j, k;
  nand n1(ns, clk, j), n2(nr, clk, k),
  n3(q, ns, nq), n4(nq, nr,  q, nrst), n5(ns1,!clk, t, nq), 
  n6(nr1, !clk, t, q), n7(j, ns1, k), n8(k, nr1, j, nrst);
  endmodule
module syncnt(output  [3:0] q,
              input  clk, nrst,step, down);
  logic [3:0]tmp;
  tff t1(q[0],tmp[0],1'b1 , clk, nrst);
  tff t2(q[1],tmp[1],((down?  tmp[0]: q[0])),clk,nrst );
  tff t3(q[2],tmp[2],((down? tmp[0] & tmp[1] : q[0] & q[1])), clk, nrst);
  tff t4(q[3],tmp[3],((down? tmp[0] & tmp[1] & tmp[2] : q[0] & q[1] & q[2])), clk, nrst);
endmodule