using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDL3
{
    public class TypeWithoutRegisterException : Exception
    {
        public TypeWithoutRegisterException() : base() { }

        public TypeWithoutRegisterException(string message)
            : base(message) { }

        public TypeWithoutRegisterException(string message, Exception inner)
            : base(message, inner) { }
    }
}
