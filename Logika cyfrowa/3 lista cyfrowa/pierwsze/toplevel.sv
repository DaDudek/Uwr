module halfadder(input a, b, output c, s);
  assign s = a ^ b;
  assign c = a && b;
endmodule

module fulladder(input a,b,c, output c0,s);
  logic c1, s1, c2;
  halfadder h1(a,b,c1,s1);
  halfadder h2(c, s1, c2,s);
  assign c0 = c1 || c2;
endmodule

module fourbitadder(input [3:0] a,
                    input [3:0] b,
                    output [3:0] s,
                    output [0:0]c);
  assign x0 = b[0] ^ 1'b0;
  assign x1 = b[1] ^ 1'b0;
  assign x2 = b[2] ^ 1'b0;
  assign x3 = b[3] ^ 1'b0;
  logic c0,c1,c2;
  logic s0,s1,s2,s3;
  fulladder f1(a[0],x0,1'b0, c0,s0);
  fulladder f2(a[1],x1,c0,c1,s1);
  fulladder f3(a[2],x2,c1,c2,s2);
  fulladder f4(a[3],x3,c2,c,s3);
  assign s[0]=s0;
  assign s[1]=s1;
  assign s[2]=s2;
  assign s[3]=s3;
endmodule

module oneBCDadder(input [3:0] a,
                input [3:0] b,
                output [3:0] o,
                output [0:0] c);
  logic [0:0] c0;
  logic [3:0] tmp;
  logic [3:0] to_fix;
  logic [0:0] c1;
  fourbitadder f1(a,b,tmp,c0);
  //jezeli przekraczamy 9 w bcd to wystarczy dodac 6 i dostajemy poprawny wynik modulo 10
  assign to_fix[3] = 0;
  assign to_fix[2] = c0 || ((tmp[2] || tmp[1])&& tmp[3]);
  assign to_fix[1] = c0 || ((tmp[2] || tmp[1])&& tmp[3]);
  assign to_fix[0] = 0;
  fourbitadder f2(tmp, to_fix, o ,c1);
  assign c=c1||c0;

endmodule




module BCDadder(input [7:0] a,
                input [7:0] b,
                output[7:0] o
                );
  logic [3:0]a1 = a[7:4];
  logic [3:0]a2 = a[3:0];
  logic [3:0]b1 = b[7:4];
  logic [3:0]b2 = b[3:0];
  logic [3:0] o2;
  logic [3:0] o1;
  logic [0:0] c0;
  logic [3:0] new_a1;
  logic [0:0] c1;
  logic [0:0] c2;
  oneBCDadder add1(a2,b2,o2,c0);
  oneBCDadder add2(a1, c0, new_a1, c1);
  oneBCDadder add3(new_a1, b1, o1, c2);
  assign o[7:4] = o1;
  assign o[3:0] = o2;
  
endmodule

module complimentto9(input [3:0] i, output [3:0] o);
  assign x = i[3];
  assign y = i[2];
  assign z = i[1];
  assign w = i[0];
  assign o[3] = !x && !y && !z;
  assign o[2] = y && !z || !y && z;
  assign o[1] = z;
  assign o[0] = !w;
endmodule


module BCDto9(input[7:0] a,
              output[7:0] o);
  logic [3:0]compto9b1;
  logic [3:0]compto9b2;
  complimentto9 comp1(a[7:4], o[7:4]);
  complimentto9 comp2(a[3:0], o[3:0]);
endmodule

module BCDsubtractor(input [7:0] a,
                     input [7:0] b,
                     output [7:0] o);
  
  logic [7:0] new_b;
  logic [7:0] tmp;
  logic [0:0] c0;
  logic [0:0] c;
  BCDto9 change1(b,new_b);
  BCDadder add1(new_b,a,tmp,c0);
  BCDadder add2(tmp,1,o,c);

endmodule

module toplevel(input [7:0] a,
                input [7:0] b,
                input [0:0] sub,
                output [7:0] o);
  logic [7:0] add;
  logic [7:0] subtract;
  BCDsubtractor subs(a,b,subtract);
  BCDadder adder(a,b,add);
  assign o[0]=sub && subtract[0] || (!sub && add[0]); 
  assign o[1]=sub && subtract[1] || (!sub && add[1]); 
  assign o[2]=sub && subtract[2] || (!sub && add[2]); 
  assign o[3]=sub && subtract[3] || (!sub && add[3]);
  assign o[4]=sub && subtract[4] || (!sub && add[4]); 
  assign o[5]=sub && subtract[5] || (!sub && add[5]); 
  assign o[6]=sub && subtract[6] || (!sub && add[6]); 
  assign o[7]=sub && subtract[7] || (!sub && add[7]); 
endmodule


