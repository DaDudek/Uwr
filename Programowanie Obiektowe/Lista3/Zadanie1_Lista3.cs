using System;

public class MyList<T>{
	
	public class Element{
		public T val;
		public Element next;
		public Element prev;
		
		public Element(T val){
			this.val = val;
			this.next = null;
			this.prev = null;
		}
	}
	
	public Element first;
	public Element last;
	
	public MyList(){
		first = null;
		last = null;
	}
	
	public bool isEmpty(){
		if(this.first==null) return true;
		else{
			return false;
		}
	}
	
	public void addFirst(T val)
	{
		if (this.first == null)
		{ //0 elementow
			Element el = new Element(val);
			el.next = null;
			el.prev = null;
			this.first = el;
			this.last = el;
		}
		
		else
		{
			Element el = new Element(val);
			this.first.prev = el;
			el.next = this.first;
			el.prev = null;
			this.first = el;
			
		}
	}
	
	public T removeFirst(){
		if(this.first == null) return default(T);
		else
		{
			if(this.first.next==null) 
			{
				this.last=null;
				Element tmps = this.first;
				this.first = null;
				return tmps.val;

			}	
			Element tmp = this.first;
			this.first.next.prev = null;
			this.first = this.first.next;
			return tmp.val;
		}
	}
	
	public void addLast(T val)
	{
		if (this.first == null)
		{ //0 elementow
			Element el = new Element(val);
			el.next = null;
			el.prev = null;
			this.first = el;
			this.last = el;
		}
		else
		{
				Element el = new Element(val);
				this.last.next = el;
				el.next = null;
				el.prev = this.last;
				this.last = el;
		}
	}
	
	public T removeLast(){
	if(this.first == null) return default(T);
		else
		{
			if(this.first.next==null) 
			{
				this.first=null;
				Element tmps = this.last;
				this.last = null;
				return tmps.val;

			}	
			Element tmp = this.last;
			this.last.prev.next = null;
			this.last = this.last.prev;
			return tmp.val;
		}
	}
}


public class Program{
	public static void Main(){
		MyList<int> l1 = new MyList<int>();
		l1.addFirst(5);
		Console.WriteLine(l1.first.val);
		Console.WriteLine(l1.last.val);
		Console.WriteLine();
		l1.addFirst(7);
		Console.WriteLine(l1.first.val);
		Console.WriteLine(l1.last.val);
		Console.WriteLine();
		l1.addFirst(2);
		Console.WriteLine(l1.first.val);
		Console.WriteLine(l1.last.val);
		Console.WriteLine();
		
		
		Console.WriteLine("nowa lista");
		Console.WriteLine();
		MyList<int> l2 = new MyList<int>();
		l2.addLast(5);
		Console.WriteLine(l2.first.val);
		Console.WriteLine(l2.last.val);
		Console.WriteLine();
		l2.addLast(7);
		Console.WriteLine(l2.first.val);
		Console.WriteLine(l2.last.val);
		Console.WriteLine();
		l2.addLast(1);
		Console.WriteLine(l2.first.val);
		Console.WriteLine(l2.last.val);
		Console.WriteLine();
		l2.addFirst(8);
		Console.WriteLine(l2.first.val);
		Console.WriteLine(l2.last.val);
		Console.WriteLine();
		
		Console.WriteLine("Test usuwania");
		Console.WriteLine();
		Console.WriteLine(l2.removeFirst());
		Console.WriteLine("pierwszy");
		Console.WriteLine(l2.first.val);
		Console.WriteLine("ostatni");
		Console.WriteLine(l2.last.val);
		Console.WriteLine();
		Console.WriteLine(l2.removeLast());
		Console.WriteLine("pierwszy");
		Console.WriteLine(l2.first.val);
		Console.WriteLine("ostatni");
		Console.WriteLine(l2.last.val);
		Console.WriteLine();
		Console.WriteLine(l2.removeLast());
		Console.WriteLine("pierwszy");
		Console.WriteLine(l2.first.val);
		Console.WriteLine("ostatni");
		Console.WriteLine(l2.last.val);
		Console.WriteLine();
		Console.WriteLine("usuwanie elementu gdy jest tylko 1");
		Console.WriteLine(l2.removeFirst());
		//Console.WriteLine(l2.first.val); wywoła błąd bo nie ma zadnych wartosci w liscie 
		//Console.WriteLine(l2.last.val);
		//Console.WriteLine();
		
		
	}
}
