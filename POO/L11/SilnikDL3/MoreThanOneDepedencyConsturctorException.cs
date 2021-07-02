using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDL3
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
