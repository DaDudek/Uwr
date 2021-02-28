// na podstawie układu z wykładu
module fourbitmux(output o,
                  input s1,s0,
                  input a0,a1,a2,a3
                  );
  assign first = s0? a1 : a0;
  assign second = s0? a3 : a2;
  assign o = s1? second : first;
endmodule

// kod z wykładu 
module dff(output q, nq, 
           input  clk, d);
  logic r,s,nr,ns;
  nand gq(q, nr, nq), gnq(nq,ns,q), gr(nr, clk,r),
  gs(ns,nr, clk, s),gr1(r, nr,  s),gs1(s, ns, d);
endmodule

module one_bit_block(output Q, input l,r,q,sr,sl,d,c);
  logic tmp;
  fourbitmux MUX(tmp,l,r,q,sl,sr,d);
  dff ds(Q, ,c,tmp);
endmodule

// na podstawie programistycznego
module universal_register(output [3:0] q,
                          input [3:0] d,
                          input i, c,l,r);
  one_bit_block  b0(q[0], l, r, q[0], q[1], i,    d[0], c);
  one_bit_block  b1(q[1], l, r, q[1], q[2], q[0], d[1], c);
  one_bit_block  b2(q[2], l, r, q[2], q[3], q[1], d[2], c);
  one_bit_block  b3(q[3], l, r, q[3], i,    q[2], d[3], c);

endmodule

module toplvel(output [3:0] q,
               input [3:0] d,
                          input i, c,l,r);
  universal_register register(q[3:0], d[3:0],i,c,l,r );
endmodule