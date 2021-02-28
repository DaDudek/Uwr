module tff(output q, nq, 
           input t, clk, nrst);
  logic ns, nr, ns1, nr1, j, k;
  nand n1(ns, clk, j), n2(nr, clk, k),
  n3(q, ns, nq), n4(nq, nr,  q, nrst), n5(ns1,!clk, t, nq), 
  n6(nr1, !clk, t, q), n7(j, ns1, k), n8(k, nr1, j, nrst);
  endmodule
module syncnt_load(output [2:0] q, input [2:0] d,
                   input en, clk, load);
  genvar n;
  logic [2:0] tmp;
  logic [2:0] t;
  assign t = {q[1] & t[1], q[0] & t[0], en};
  for (n = 0; n < 3; n = n + 1)
    tff tf(q[n],tmp[n], (load ?  d[n] : q[n] ^ t[n])^q[n],clk, en);
endmodule