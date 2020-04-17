module graytobinary(input [31:0] i, output [31:0] o);
  // korzystam z tego ze najstarszy bit taki sam w obu reprezentacjach a kolejne oblicza się przez xorowanie
  // definicja z wikipedii 
  integer k;
  logic [0:0]tmp;
  always_comb 
    begin
      o[31] = i[31];
      tmp = i[31];
      for (k=30; k>-1; k=k-1)
        begin
        	o[k] = tmp ^ i[k];
          tmp = o[k];
    	end
    end
endmodule
