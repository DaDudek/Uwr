// Write your modules here!
module circuit(input [15:0] i, output [15:0] o);
  logic [3:0] first  ;
  logic [3:0] second ;
  logic [3:0] third ;
  logic [3:0] fourth ;
  logic [3:0] new_first ;
  logic [3:0] new_second ;
  logic [3:0] new_third ;
  logic [3:0] new_fourth ;
  
  //L[0] > L[1] ? then swap
  always_comb
    if(i[15:12] > i[11:8]) first[3:0] = i[11:8];
  else first[3:0] = i[15:12];
  always_comb
    if(i[15:12] > i[11:8]) second[3:0] = i[15:12];
  else second[3:0] = i[11:8];
  
  // L[2] > L[3] ? then swap
  always_comb
    if(i[7:4] > i[3:0]) third[3:0] = i[3:0];
  else third[3:0] = i[7:4];
  always_comb
    if(i[7:4] > i[3:0]) fourth[3:0] = i[7:4];
  else fourth[3:0] = i[3:0];
  
  // L[1] > L[3] ? then swap
  always_comb
    if(second > fourth) new_second[3:0] = fourth[3:0];
  else new_second[3:0] = second[3:0];
  always_comb
    if(second > fourth) new_fourth[3:0] = second[3:0];
  else new_fourth[3:0] = fourth[3:0];
  
  // L[0] > L[2] ? then swap
  always_comb
    if(first > third) new_first[3:0] = third[3:0];
  else new_first[3:0] = first[3:0];
  always_comb
    if(first > third) new_third[3:0] = first[3:0];
  else new_third[3:0] = third[3:0];
  
  //L[1] > L[2] ? then swap
  always_comb
    if(new_second > new_third) o[7:4] = new_third[3:0];
  else o[7:4] = new_second[3:0] ;
  always_comb
    if(new_second > new_third) o[11:8] = new_second[3:0];
  else o[11:8] = new_third[3:0] ;
  
  assign o[15:12] = new_fourth[3:0];
  assign o[3:0] = new_first[3:0];
  
  
  	
      
endmodule