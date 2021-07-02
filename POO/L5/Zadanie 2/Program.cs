using System;
using System.Collections.Generic;
using System.IO;

namespace POO_5._2
{

    class CeasarStream : Stream
    {
        private Stream stream;
        private int key;
        private Dictionary<char, int> dict = new Dictionary<char, int>();
        private Dictionary<int, char> dictN = new Dictionary<int, char>();


        public CeasarStream(Stream stream,int key) {
            this.stream = stream;
            this.key = key;
            initDict();
            initDictN();
        }

        public override bool CanRead => stream.CanRead;

        public override bool CanSeek => stream.CanSeek;

        public override bool CanWrite => stream.CanWrite;

        public override long Length => stream.Length;

        public override long Position { get => stream.Position; set => stream.Position = value; }

        public override void Flush()
        {
            stream.Flush();
        }

        public override int Read(byte[] buffer, int offset, int count)
        {
            int score = stream.Read(buffer, offset, count);
            String words = System.Text.Encoding.UTF8.GetString(buffer, 0, buffer.Length).ToLower();
            String newWord = "";
            for (int i =0; i < words.Length; i++)
            {
                newWord += CeasarCipher(words[i], this.key);
            }
            byte[] newBuffer = System.Text.Encoding.UTF8.GetBytes(newWord, 0, newWord.Length);
            int limit;
            if (buffer.Length > newBuffer.Length)
            {
                limit = newBuffer.Length;
            }
            else {

                limit = buffer.Length;
            }
            for (int i = 0; i < limit; i++)
            {
                buffer[i] = newBuffer[i];
            }
            return score;

         
        }

        public override long Seek(long offset, SeekOrigin origin)
        {
            return stream.Seek(offset, origin);
        }

        public override void SetLength(long value)
        {
            stream.SetLength(value);
        }

        public override void Write(byte[] buffer, int offset, int count)
        {
            byte[] newBytes = buffer;
            String words = System.Text.Encoding.UTF8.GetString(newBytes,0,newBytes.Length).ToLower();
            String newWord = "";
            for (int i = 0; i < words.Length; i++)
            {
               newWord += CeasarCipher(words[i],this.key);
            }

            stream.Write(System.Text.Encoding.UTF8.GetBytes(newWord),offset, System.Text.Encoding.UTF8.GetBytes(newWord).Length);
            Flush();
        }


        int mod(int x, int m)
        {
            return (x % m + m) % m;
        }

        public char CeasarCipher(char character, int key) {
            if (!char.IsLetter(character))
            {

                return character;
            }
            else {
                int newKey = mod((this.dict[character] + key),35) ;
                return this.dictN[newKey];
            }

        }
      

        public void initDict() {

            this.dict.Add('a', 0);
            this.dict.Add('ą', 1);
            this.dict.Add('b', 2);
            this.dict.Add('c', 3);
            this.dict.Add('ć', 4);
            this.dict.Add('d', 5);
            this.dict.Add('e', 6);
            this.dict.Add('ę', 7);
            this.dict.Add('f', 8);
            this.dict.Add('g', 9);
            this.dict.Add('h', 10);
            this.dict.Add('i', 11);
            this.dict.Add('j', 12);
            this.dict.Add('k', 13);
            this.dict.Add('l', 14);
            this.dict.Add('ł', 15);
            this.dict.Add('m', 16);
            this.dict.Add('n', 17);
            this.dict.Add('ń', 18);
            this.dict.Add('o', 19);
            this.dict.Add('ó', 20);
            this.dict.Add('p', 21);
            this.dict.Add('q', 22);
            this.dict.Add('r', 23);
            this.dict.Add('s', 24);
            this.dict.Add('ś', 25);
            this.dict.Add('t', 26);
            this.dict.Add('u', 27);
            this.dict.Add('v', 28);
            this.dict.Add('w', 29);
            this.dict.Add('x', 30);
            this.dict.Add('y', 31);
            this.dict.Add('z', 32);
            this.dict.Add('ź', 33);
            this.dict.Add('ż', 34);

        }

        public void initDictN()
        {

            this.dictN.Add(0, 'a');
            this.dictN.Add(1, 'ą');
            this.dictN.Add(2, 'b');
            this.dictN.Add(3, 'c');
            this.dictN.Add(4, 'ć');
            this.dictN.Add(5, 'd');
            this.dictN.Add(6, 'e');
            this.dictN.Add(7, 'ę');
            this.dictN.Add(8, 'f');
            this.dictN.Add(9, 'g');
            this.dictN.Add(10, 'h');
            this.dictN.Add(11, 'i');
            this.dictN.Add(12, 'j');
            this.dictN.Add(13, 'k');
            this.dictN.Add(14, 'l');
            this.dictN.Add(15, 'ł');
            this.dictN.Add(16, 'm');
            this.dictN.Add(17, 'n');
            this.dictN.Add(18, 'ń');
            this.dictN.Add(19, 'o');
            this.dictN.Add(20, 'ó');
            this.dictN.Add(21, 'p');
            this.dictN.Add(22, 'q');
            this.dictN.Add(23, 'r');
            this.dictN.Add(24, 's');
            this.dictN.Add(25, 'ś');
            this.dictN.Add(26, 't');
            this.dictN.Add(27, 'u');
            this.dictN.Add(28, 'v');
            this.dictN.Add(29, 'w');
            this.dictN.Add(30, 'x');
            this.dictN.Add(31, 'y');
            this.dictN.Add(32, 'z');
            this.dictN.Add(33, 'ź');
            this.dictN.Add(34, 'ż');

        }

    }

    class Program
    {
        static void Main(string[] args)
        {
            String path = @"C:\Users\HP\Desktop\POO\POO - lista 5\Zadanie 2\POO 5.2\file.txt";
            FileStream fileToWrite = File.Create(path);
            CeasarStream ceasar = new CeasarStream(fileToWrite, 5);
            byte[] bytes = System.Text.Encoding.UTF8.GetBytes("dawid dudek");
            ceasar.Write(bytes, 0, bytes.Length);
            ceasar.Flush();
            fileToWrite.Close();


            FileStream fs = File.OpenRead(path);
            CeasarStream ceasar1 = new CeasarStream(fs, -5);
            byte[] buf = new byte[1024];
            int c;
            while ((c = ceasar1.Read(buf, 0, buf.Length)) > 0)
            {
                Console.WriteLine(System.Text.Encoding.UTF8.GetString(buf, 0, c));
            }
        }
    }
}
