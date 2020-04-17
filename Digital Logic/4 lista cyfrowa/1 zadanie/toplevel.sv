module onebitmover(
  input [3:0]i,
  input [0:0]l,r,
  output [3:0]o
);
  assign o[3] = (l & i[2]) || (r & 1'b0) || ((l ~| r) & i[3]);
  assign o[2] = (l & i[1]) || (r & i[3]) || ((l ~| r) & i[2]);
  assign o[1] = (l & i[0]) || (r & i[2]) || ((l ~| r) & i[1]);
  assign o[0] = (l & 1'b0) || (r & i[1]) || ((l ~| r) & i[0]);
  
endmodule