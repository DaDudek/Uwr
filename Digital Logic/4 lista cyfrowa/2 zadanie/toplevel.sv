module funnelshifter(input [7:0]a,
             input [7:0]b,
             input [3:0]n,
             output [7:0] o);
  logic [15:0]connection;
  assign connection = {a,b};
  assign o = connection[n+7:n];
  
endmodule

module toplevel(input [7:0] i,
                input[3:0] n,
                input[0:0]ar,lr,rot,
                output [7:0] o);
  logic [3:0] new_n;
  logic [7:0] first, second;
  assign new_n = lr? (8-n) : n;
  assign first = rot? i : 
    (ar ? 
      (lr? i : {8 {i[7]}}) :
      (lr? i : {8 {1'b 0}}));
  assign second = rot? i:
    (lr? {8 {1'b 0}} : i) ;
  funnelshifter fs(first,second,new_n,o);
endmodule