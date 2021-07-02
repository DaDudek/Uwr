﻿using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDI2
{
    public class CycleInResolveTreeException : Exception
    {
        public CycleInResolveTreeException() : base() { }

        public CycleInResolveTreeException(string message)
            : base(message) { }

        public CycleInResolveTreeException(string message, Exception inner)
            : base(message, inner) { }
    }
   
}
