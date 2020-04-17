using System;
using System.Collections;
using System.Collections.Generic;
					

public interface Interfejs{
	int element(int i);
}
				
public class ListaLeniwa : Interfejs, IEnumerable{
	public List<int> list = new List<int>();
	public int size;
	Random random = new Random();
	
	public int get_size(){
		return this.size;
	}
	 public int filter(){
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
	
	public string toString(){
		string napis = "";
		for(int i=0; i<size; i++){
			string tmp = list[i] + " ";
			napis = napis + tmp;
		}
		return napis;
	}
	
	public class ListEnum: IEnumerator{
		
		public List<int> list;
		public int position;
		
		
	public ListEnum(List<int> list){
		this.list= list;
		this.position = -1;
	}	
		
	 public bool MoveNext()
        {
            this.position++;
		 if (position < list.Count){
			 return true;
		 }
		 return false;
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
                return list[position];
            }
        }	
	}	
	
	 public IEnumerator GetEnumerator()
        {
            return new ListEnum(list);
        }
	
	 public int this[int index]
        {
            get
            {
                if (index < 0) throw new IndexOutOfRangeException();
                else return element(index + 1);
            }
            set
            {
                if (index < 0) {
					throw new IndexOutOfRangeException();
				}

                if (index >= get_size()){
					element(index + 1);
				}

                list[index] = value;
            }
        }
	
	public int Length
        {
            get
            {
                return get_size();
            }
        }
	
}

public class IntStream: Interfejs{
	public int value;
	
	public IntStream(){
		this.value = 0;
	}
	
	public int element(int i){
		for(int k=0; k < i ;k++){
			if (!this.eos()){
				this.value++;
			}
			else{
				this.reset();
				return 0;
			}
		}
		return this.value;
	}
	virtual public bool eos(){
		if (this.value <  2147483646 ) return false;
		return true;
	}
	virtual public void reset(){
		this.value = 0;
	}
}

public class Program
{
	public static void Main()
	{
		ListaLeniwa lista = new ListaLeniwa();
		Console.WriteLine(lista.get_size());
		Console.WriteLine(lista.element(1));
		Console.WriteLine(lista.element(2));
		Console.WriteLine(lista.element(3));
		Console.WriteLine(lista.element(5));
		Console.WriteLine(lista.element(20));
		Console.WriteLine(lista.get_size());
		Console.WriteLine(lista.element(18));
		Console.WriteLine(lista.get_size());
		Console.WriteLine(lista.Length);
		Console.WriteLine(lista.toString());
		Console.WriteLine();
		foreach(int el in lista)
             {
                 Console.WriteLine(el);
             }
		lista[0]=0;
		Console.WriteLine(lista.toString());

	}
}
