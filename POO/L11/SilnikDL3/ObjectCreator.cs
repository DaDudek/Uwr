using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDL3
{
    public abstract class ObjectCreator
    {
        public Type type;
        public object instance;

        public ObjectCreator(Type type)
        {
            this.type = type;
        }

        public ObjectCreator()
        {
        }

        public abstract object CreateObject();

        public Type getMyType()
        {
            return this.type;
        }
    }
}
