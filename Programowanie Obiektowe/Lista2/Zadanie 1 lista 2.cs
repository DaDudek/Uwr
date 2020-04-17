using System;
					
public class IntStream{
	public int value;
	
	public IntStream(){
		this.value = 0;
	}
	
	virtual public int next(){
		if (!this.eos()){
			this.value++;
			return this.value;
		}
		else{
			this.reset();
			return 0;
		}
	}
	virtual public bool eos(){
		if (this.value <  2147483646 ) return false;
		return true;
	}
	virtual public void reset(){
		this.value = 0;
	}
}

public class PrimeStream: IntStream{
	public PrimeStream(){
		this.value = 1;
	}
	override public int next(){
		this.value++;
		if(this.eos()){
			this.reset();
		return this.value;
		}
		while(!this.is_prime(this.value)){
			this.value++;
		}
		return this.value;
	}
	override public void reset(){
		this.value = 2;
	}
	public bool is_prime(int x){
		int square_root = (int)Math.Sqrt(base.value) +1;
		if (base.value == 1) return false;
		if (base.value == 2 || base.value == 3) return true;
			for (int i = 2 ; i< square_root; i++ ){
				if((x%i)== 0){
					return false;
				}
			}
		return true;
	}
}
public class RandomStream: IntStream{
	Random rands = new Random();
	public RandomStream(){
		this.value = 0;
	}
	override public int next(){
		if(!this.eos()){
		this.value = rands.Next(97, 122);
		}
		return this.value;
	}
	override public bool eos(){
		return false;
	}
}

public class RandomWordStream{
	PrimeStream ps = new PrimeStream();
	RandomStream ris = new RandomStream();
	public String next(){
		String word= "";
		int len = ps.next();
		for(int i=0; i<len; i++){
			char letter = (char) ris.next();
			word = word + letter;
		}
		return word;
	}
}

public class Program
{
	public static void Main()
	{
		RandomWordStream ps = new RandomWordStream();
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());
		Console.WriteLine(ps.next());

		
	}
}
