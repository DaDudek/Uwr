module betterBCD(input [3:0] i, output [3:0] o);
  assign x = i[3];
  assign y = i[2];
  assign z = i[1];
  assign w = i[0];
  assign o[0] = w;
  assign o[1] = (!x & !z &w) | (!x & z & !w) | (x & w);
  assign o[2] = (!y | !w) & (!y | !z) & (y | z | w);
  assign o[3] = x | (y & w) | (y & z);
endmodule
