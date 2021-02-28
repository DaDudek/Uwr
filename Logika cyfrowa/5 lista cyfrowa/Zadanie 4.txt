// Write your modules here!
module twotofour(input [1:0]i, output[3:0] o);
  assign o[0] = !i[1] && !i[0];
  assign o[1] = !i[1] && i[0];
  assign o[2] = i[1] && !i[0];
  assign o[3] = i[1] && i[0];
endmodule

module threetoeight(input [2:0] i, output [7:0] o);
  logic [3:0] tmp;
  logic [3:0] tmp1;
  twotofour tf(i[1:0], tmp);
  twotofour tf1(i[1:0], tmp1);
  assign o[0]= !i[2] & tmp[0];
  assign o[1]= !i[2] & tmp[1];
  assign o[2]= !i[2] & tmp[2];
  assign o[3]= !i[2] & tmp[3];
  assign o[4]= i[2] & tmp1[0];
  assign o[5]= i[2] & tmp1[1];
  assign o[6]= i[2] & tmp1[2];
  assign o[7]= i[2] & tmp1[3];
endmodule
  
