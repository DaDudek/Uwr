﻿using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDI2
{
    public class InstanceObjectCreator : ObjectCreator
    {
        public InstanceObjectCreator(object Instance) : base()
        {
            this.instance = Instance;
        }

        public override object CreateObject()
        {
            return this.instance;
        }
    }
}
