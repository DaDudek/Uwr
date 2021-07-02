using System;
using System.Collections.Generic;
using Microsoft.VisualBasic.CompilerServices;

namespace SilnikDI
{
    public class TypeWithoutRegisterException : Exception {
        public TypeWithoutRegisterException() { }

        public TypeWithoutRegisterException(string message)
            : base(message) { }

        public TypeWithoutRegisterException(string message, Exception inner)
            : base(message, inner) { }
    }

    public abstract class ObjectCreator {
        public Type type;
        public object instance;

        public ObjectCreator(Type type) {
            this.type = type;
        }

        public abstract object CreateObject();

        public Type getMyType() {
            return this.type;
        }
    }

    public class SingletonObjectCreator : ObjectCreator
    {

        public SingletonObjectCreator(Type type) : base(type) 
        {     
        }

        public override object CreateObject()
        {
            if (instance == null) {
                instance = Activator.CreateInstance(type);
            }
            return instance;
        }


    }


    public class CommonObjectCreator : ObjectCreator
    {

        public CommonObjectCreator(Type type) : base(type)
        {
        }

        public override object CreateObject()
        {
            return Activator.CreateInstance(type);
        }
    }

    public class SimpleContainer {
        private Dictionary<Type, ObjectCreator> registerMap;

        public SimpleContainer() {
            registerMap = new Dictionary<Type, ObjectCreator>();
        }

        public void RegisterType<T>(bool isSingleton) where T : class
        {
            if (registerMap.ContainsKey(typeof(T)))
            {
                if (isSingleton)
                {
                    registerMap[typeof(T)] = new SingletonObjectCreator(typeof(T));
                }
                else
                {
                    registerMap[typeof(T)] = new CommonObjectCreator(typeof(T));
                }
            }
            else {
                if (isSingleton)
                {
                    registerMap.Add(typeof(T), new SingletonObjectCreator(typeof(T)));
                }
                else
                {
                    registerMap.Add(typeof(T), new CommonObjectCreator(typeof(T)));
                }
            }
            
        }
        public void RegisterType<From, To>(bool isSingleton) where To : From
        {
            if (registerMap.ContainsKey(typeof(From)))
            {
                if (isSingleton)
                {
                    registerMap[typeof(From)] = new SingletonObjectCreator(typeof(To));
                }
                else
                {
                    registerMap[typeof(From)] = new CommonObjectCreator(typeof(To));
                }
            }
            else 
            {
                if (isSingleton)
                {
                    registerMap.Add(typeof(From), new SingletonObjectCreator(typeof(To)));
                }
                else
                {
                    registerMap.Add(typeof(From), new CommonObjectCreator(typeof(To)));
                }
            }
            
        }
        public T Resolve<T>() where T:class {
            Type type = typeof(T);
            if (type.IsInterface || type.IsAbstract)
            {
                if (registerMap.ContainsKey(type))
                {
                    ObjectCreator creator = registerMap[type];
                    return (T)creator.CreateObject();
                }
                else
                {
                    throw new TypeWithoutRegisterException("missed register class");
                }
            }
            else {
                if (registerMap.ContainsKey(type))
                {
                    ObjectCreator creator = registerMap[type];
                    return (T)creator.CreateObject();
                }
                else {
                    this.RegisterType<T>(false);
                    return this.Resolve<T>();
                }

            }
        }
    }



    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
