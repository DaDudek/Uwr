module toplevel(input clk,
                input [15:0] d,
                input [1:0] sel,
                output logic [15:0] cnt,
                output logic [15:0] cmp,
                output logic [15:0] top,
                output out);

  always_ff  @(posedge clk) // rejestry
    if(sel == 2'b 01) cmp <= d;
    else if(sel == 2'b 10) top <= d;
  
  always_ff @(posedge clk) // licznik 
    if(sel == 2'b 11) cnt <= d;
    else if(cnt < top) cnt <= cnt +16'b 1;
    else cnt <= 16'b 0;
  
  assign out = cnt < cmp; // wyjscie
endmodule
