module toplevev(input [3:0] i, output [3:0] o);
  assign x = i[3];
  assign y = i[2];
  assign z = i[1];
  assign w = i[0];
  assign o[3] = !x && !y && !z;
  assign o[2] = y && !z || !y && z;
  assign o[1] = z;
  assign o[0] = !w;
endmodule
