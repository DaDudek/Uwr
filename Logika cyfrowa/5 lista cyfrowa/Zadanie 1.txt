// Half adder
module halfadder(
  input a, 
  input b,
  output o,
  output c
);

  assign o = a ^ b;
  assign c = a & b;

endmodule

// Full adder
module fulladder(
  input a,
  input b,
  input d,
  output o,
  output c
);

  logic t, c1, c2;

  halfadder ha1(a, b, t, c1);
  halfadder ha2(t, d, o, c2);

  assign c = c1 | c2;

endmodule

// Multibit serial adder
module tenbitadder(input [9:0] a,
                   input [9:0] b,
                   input [0:0] c0,
                   output[9:0] o,
                   output[0:0] c);
  logic [9:0] cn;
  fulladder f0(a[0],b[0],c0, o[0], cn[0]);
  fulladder f1(a[1],b[1],cn[0], o[1], cn[1]);
  fulladder f2(a[2],b[2],cn[1], o[2], cn[2]);
  fulladder f3(a[3],b[3],cn[2], o[3], cn[3]);
  fulladder f4(a[4],b[4],cn[3], o[4], cn[4]);
  fulladder f5(a[5],b[5],cn[4], o[5], cn[5]);
  fulladder f6(a[6],b[6],cn[5], o[6], cn[6]);
  fulladder f7(a[7],b[7],cn[6], o[7], cn[7]);
  fulladder f8(a[8],b[8],cn[7], o[8], cn[8]);
  fulladder f9(a[9],b[9],cn[8], o[9], c);

endmodule
module andtenthings(input [9:0] i,
                    input [0:0] e,
                    output [9:0] o);
  assign o[0] = i[0] & e;
  assign o[1] = i[1] & e;
  assign o[2] = i[2] & e;
  assign o[3] = i[3] & e;
  assign o[4] = i[4] & e;
  assign o[5] = i[5] & e;
  assign o[6] = i[6] & e;
  assign o[7] = i[7] & e;
  assign o[8] = i[8] & e;
  assign o[9] = i[9] & e;
endmodule

module toplevel(input[7:0] a, 
                input [4:0] e,
                output [9:0] o);
  logic [9:0] number_to_add = {2'b 0, a};
  logic [0:0] cn,cn2,cn3;
  logic [9:0] tmp1;
  logic [9:0]score0,score1,score2, score3,score4;
  andtenthings and1(number_to_add, e[4],score0);
  tenbitadder add1(number_to_add,score0, 1'b 0, score1, cn);
  assign condition = e[3] | e[4];
  andtenthings and2(score1, condition, score2);
  tenbitadder add2(number_to_add, score2, 1'b 0, score3, cn2);
  assign condition1 = e[2] | e[3] | e[4];
  andtenthings and3(score3, condition1, score4);
  tenbitadder add3(number_to_add, score4, 1'b 0, o, cn3);


endmodule
  