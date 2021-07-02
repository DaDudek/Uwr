using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDI2
{
    public class MoreThanOneLongestException : Exception
    {
        public MoreThanOneLongestException():  base() { }

        public MoreThanOneLongestException(string message)
            : base(message) { }

        public MoreThanOneLongestException(string message, Exception inner)
            : base(message, inner) { }
    }
}
