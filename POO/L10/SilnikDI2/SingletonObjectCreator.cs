using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDI2
{
    public class SingletonObjectCreator : ObjectCreator
    {

        public SingletonObjectCreator(Type type) : base(type)
        {
        }

        public SingletonObjectCreator() : base()
        {
        }

        public override object CreateObject()
        {
            if (instance == null)
            {
                instance = Activator.CreateInstance(type);
            }
            return instance;
        }


    }
}
