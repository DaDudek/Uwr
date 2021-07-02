using System;
using System.Collections;
using System.Collections.Generic;


namespace POO_5._4
{

    class ComparisonToIComparerAdapter<T> : IComparer{

        private Comparison<T> comparison;

        public ComparisonToIComparerAdapter(Comparison<T> comparison) {
            this.comparison = comparison;
        }

        public int Compare(object x, object y)
        {
            return comparison((T)x, (T)y);
        }
    }
   
    class Program
    {
        private static int comparisonExample(int x, int y) {
            return x.CompareTo(y);
        }

        static void Main(string[] args)
        {
            ArrayList a = new ArrayList() { 1, 5, 3, 3, 2, 4, 3 };

            Comparison<int> comparison = comparisonExample;

            a.Sort(new ComparisonToIComparerAdapter<int>(comparison));

            for (int i = 0; i < a.Count ; i++)
            {
                Console.WriteLine(a[i]);
            }

        }
    }
}
