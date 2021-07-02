﻿using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDL3
{
    public class CommonObjectCreator : ObjectCreator
    {

        public CommonObjectCreator(Type type) : base(type)
        {
        }

        public CommonObjectCreator() : base()
        {
        }

        public override object CreateObject()
        {
            return Activator.CreateInstance(type);
        }
    }
}
