using System;
using System.Collections;
			
public class PrimeCollection : IEnumerable {
	
	public class ListEnum: IEnumerator{
		
		public int[] numbers;
		public int position;
		
		public bool is_prime(int x){
		int square_root = (int)Math.Sqrt(x) +1;
		if (x == 1) return false;
		if (x == 2 || x == 3) return true;
			for (int i = 2 ; i< square_root; i++ ){
				if((x%i)== 0){
					return false;
				}
			}
		return true;
	}
		
	public ListEnum(){
		this.numbers = new int[200000];
		this.position = -1;
	}	
		
	 public bool MoveNext()
        {
            int el;
            this.position++;

            if (this.position == 0) el = 1;
            else el = this.numbers[position - 1];
            
            for(int i = el + 1; i < 200000; i++)
            {
                if (is_prime(i))
                {
                    this.numbers[position] = i;
					break;
                }
            }

            if (this.numbers[position] <= 0) return false;
            else return true;
        }
	
	public void Reset()
        {
            this.position = -1;
        }
	
	object IEnumerator.Current
        {
            get
            {
                return Current;
            }
        }	
		
	public int Current
        {
            get
            {
                return this.numbers[position];
            }
        }	
		
}
		
	 public IEnumerator GetEnumerator()
        {
            return new ListEnum();
        }
	
}

public class Program
    {
        public static void Main(string[] args)
        {
            PrimeCollection pc = new PrimeCollection();
             foreach(int p in pc)
             {
                 Console.WriteLine(p);
             }
        }
    }
	
	