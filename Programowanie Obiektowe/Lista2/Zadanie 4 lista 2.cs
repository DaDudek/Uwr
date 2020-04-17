using System;
using System.Collections.Generic;
					
public class ListaLeniwa{
	public List<int> list = new List<int>();
	public int size;
	Random random = new Random();
	
	public int get_size(){
		return size;
	}
	virtual public int filter(){
		return random.Next();
	}
	 public int element(int i){
		if(i<size) return list[i-1];
		while(size < i){
			list.Add(this.filter());
			size++;
		}
		return list[i-1];
	}
}

public class Pierwsze: ListaLeniwa{
	
	override public int filter(){
		if (this.get_size()==0){
			return 2;
		}
		int tmp = this.list[this.get_size()-1] +1;
		while(!this.is_prime(tmp))
		{
				tmp++;
		}
		return tmp;
	}

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
	
}
public class Program
{
	public static void Main()
	{
		Pierwsze lista = new Pierwsze();
		Console.WriteLine(lista.get_size());
		Console.WriteLine(lista.element(1));
		Console.WriteLine(lista.element(2));
		Console.WriteLine(lista.element(3));
		Console.WriteLine(lista.element(5));
		Console.WriteLine(lista.element(20));
		Console.WriteLine(lista.get_size());
		Console.WriteLine(lista.element(18));
		Console.WriteLine(lista.get_size());
	
	}
}
