using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDI2
{
    public class MoreThanOneDepedencyConsturctorException : Exception
    {
        public MoreThanOneDepedencyConsturctorException() { }

        public MoreThanOneDepedencyConsturctorException(string message)
            : base(message) { }

        public MoreThanOneDepedencyConsturctorException(string message, Exception inner)
            : base(message, inner) { }
    }
}
