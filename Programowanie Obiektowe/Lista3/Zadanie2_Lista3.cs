using System;

public class Dictionary<K,V>
{	
	private K [] key_table;
	private V [] val_table;
	private int size;
	private int count_elements;	
	
	public void set_key_table_by_val(int position, K val){
		this.key_table[position] = val;
	}
	public void set_key_table(K[] table){
		this.key_table = table;
	}
	
	public K get_key_table(int position){
		return this.key_table[position];
	}
	
	public void set_val_table(V[] table){
		this.val_table = table;
	}
	
	public void set_val_table_by_val(int position, V val){
		this.val_table[position] = val;
	}
	
	public V get_val_table(int position){
		return this.val_table[position];
	}
	
	public void set_size(int x){
		this.size = x;
	}
	
	public int get_size(){
		return this.size;
	}
	
	public void set_count_elements(int x){
		this.count_elements = x;
	}
		
	public int get_count_elements(){
		return this.count_elements;
	}
		
	public Dictionary(){
		this.set_size(100000);
		this.set_count_elements(0);
		this.key_table = new K[size];
		this.val_table = new V[size];
	}
	public void is_big_enough(){
		if(this.get_count_elements() + 1 == this.get_size()){
			K [] tmp_key_table = new K[size*2];
			V [] tmp_val_table = new V[size*2];
			for(int i=0; i<size; i++){
				tmp_key_table[i] = this.get_key_table(i);
				tmp_val_table[i] = this.get_val_table(i);
			}
			this.set_key_table(tmp_key_table);
			this.set_val_table(tmp_val_table);
			this.set_size(this.get_size() *2);

		}
	}
	
	public void Add(K key, V val)
	{
		this.is_big_enough();
		bool flag = true;
		for(int i=0; i<this.count_elements; i++)
		{
			if(this.get_key_table(i).Equals(key)) 
			{
				this.set_val_table_by_val(i, val);
				flag = false;
				break;
			}
		}
		if(flag)
		{
			this.set_key_table_by_val(this.get_count_elements() + 1, key);
			this.set_val_table_by_val(this.get_count_elements() + 1, val);
			this.set_count_elements(this.get_count_elements()+1);
		}
	}
	public V find_by_key(K key){
		for(int i = 0; i<this.get_count_elements(); i++)
		{
			if(this.get_key_table(i).Equals(key)) return this.get_val_table(i);
		}
		return default(V);
	}
	public void delete_by_key(K key)
	{
		for(int i=0; i<this.get_count_elements(); i++){
			bool flag = false;
			if(this.get_key_table(i).Equals(key)){
				flag = true;
				for(int j=i; j<this.get_count_elements(); j++){
					this.set_key_table_by_val(j,this.get_key_table(j+1));
					this.set_val_table_by_val(j,this.get_val_table(j+1));
				}
			}
			if(flag){
				this.set_count_elements(this.get_count_elements() -1);
				break;
			}
		}
	}
}


public class Program
{
	public static void Main()
	{
		Dictionary <int, int> dict = new Dictionary<int,int>();
		dict.Add(0,5);
		dict.Add(1,4);
		dict.Add(2,3);
		dict.Add(3,214);
		dict.Add(6,40);
		dict.Add(11,24);
		int tmp= dict.get_size();
		Console.WriteLine("aktualny rozmiar");
		Console.WriteLine(tmp);
		
		Console.WriteLine("ilosc elementow");
		Console.WriteLine(dict.get_count_elements());
		
		dict.delete_by_key(421);
		dict.delete_by_key(0);
		Console.WriteLine("ilosc elementow po usunieciu");
		Console.WriteLine(dict.get_count_elements());
		
		Console.WriteLine("test szukania po kluczu - bledny klucz zwraca 0");
		Console.WriteLine(dict.find_by_key(523));
		Console.WriteLine(dict.find_by_key(1));
		
		
		Console.WriteLine("ile elementow?");
		Console.WriteLine(dict.get_count_elements());
		dict.Add(1,8);
		Console.WriteLine("ile elementow po dodaniu na istniejacy klucz");
		Console.WriteLine(dict.get_count_elements());

		Console.WriteLine("sprawdzenie czy element o kluczu 1 dobrze sie zaktualizował");
		Console.WriteLine(dict.find_by_key(1));

	}
}