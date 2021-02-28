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

module universal_register(output [7:0] q,
                        input [7:0] d,
                          input i, c,l,r);
  //logic i0,i1,i2,i3,i4,i5,i6,i7;
  one_bit_block  b0(q[0], l, r, q[0], q[1], i,    d[0], c);
  one_bit_block  b1(q[1], l, r, q[1], q[2], q[0], d[1], c);
  one_bit_block  b2(q[2], l, r, q[2], q[3], q[1], d[2], c);
  one_bit_block  b3(q[3], l, r, q[3], q[4], q[2], d[3], c);
  one_bit_block  b4(q[4], l, r, q[4], q[5], q[3], d[4], c);
  one_bit_block  b5(q[5], l, r, q[5], q[6], q[4], d[5], c);
  one_bit_block  b6(q[6], l, r, q[6], q[7], q[5], d[6], c);
  one_bit_block  b7(q[7], l, r, q[7], i,    q[6], d[7], c);
endmodule

module toplvel(output [7:0] q,
                        input [7:0] d,
                          input i, c,l,r);
  universal_register register(q[7:0], d[7:0],i,c,l,r );
endmodule