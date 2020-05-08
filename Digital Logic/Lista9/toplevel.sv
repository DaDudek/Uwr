// Kod wzorowany na wykładzie
module microwave(input clk,nrst,door,start,finish,
                output heat,light,bell);
  // kody stanów automatu
  const logic [2:0] CLOSED = 3'b 000, COOK = 3'b 001, 
  					PAUSE = 3'b 010, BELL = 3'b 011, OPEN = 3'b 100; 
  
  logic [2:0] q; // stan automatu
  always_comb begin //funkcja wyjścia
    light = 0;
    heat = 0;
    bell = 0;
    unique case(q)
      CLOSED: begin light = 0; heat = 0 ; bell = 0; end
      COOK: begin light = 1; heat = 1; bell = 0; end
      PAUSE: begin light = 1; heat = 0; bell = 0; end
      BELL: begin light = 0; heat = 0; bell = 1; end
      OPEN: begin light = 1; heat = 0; bell = 0; end
    endcase
  end
  
  // funkcja przejścia
  always_ff @(posedge clk or negedge nrst)
  	if (!nrst) q <= CLOSED;
  else unique case(q)
    CLOSED: begin
      if(door) q <= OPEN;
      else if (start & !door) q <= COOK;
    end
	COOK: begin
      if(door)  q <= PAUSE;
      else if(!door & finish) q <= BELL;
    end
    PAUSE: begin
      if(!door) q <= COOK;
    end
    BELL: begin
      if(door) q <= OPEN;
    end
    OPEN: begin
      if(!door) q <= CLOSED;
    end
  endcase
     
endmodule