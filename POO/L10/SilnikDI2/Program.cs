using System;
using System.Collections.Generic;
using System.Reflection;
using Microsoft.VisualBasic.CompilerServices;

namespace SilnikDI2
{

    public class SimpleContainer
    {
        private Dictionary<Type, ObjectCreator> registerMap;

        public SimpleContainer()
        {
            registerMap = new Dictionary<Type, ObjectCreator>();
        }

        //new code start
        public void RegisterInstance<T>(T Instance) where T : class
        {
            if (registerMap.ContainsKey(typeof(T)))
            {
                registerMap[typeof(T)] = new InstanceObjectCreator(Instance);
            }
            else
            {
                registerMap.Add(typeof(T), new InstanceObjectCreator(Instance));
            }

        }
        // new code end

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
            else
            {
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
        public T Resolve<T>() where T : class
        {
            return this.recursiveResolve<T>(new List<Type>());
        }

        private T basicResolve<T>() where T : class 
        {
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
            else
            {
                if (registerMap.ContainsKey(type))
                {
                    ObjectCreator creator = registerMap[type];
                    return (T)creator.CreateObject();
                }
                else
                {
                    return (T)Activator.CreateInstance(type); ;
                }

            }
        }



        private T recursiveResolve<T>(List<Type> list) where T : class
        {
            Type type = typeof(T);
            if (list.Contains(type))
            {
                throw new CycleInResolveTreeException();
            }

            ConstructorInfo info = findLongestConstructor(typeof(T));
            if (info == null) 
            {
                return basicResolve<T>();
            }
            ParameterInfo[] paramInfo = info.GetParameters();
            Object[] arguments = new object[info.GetParameters().Length];
            int argCounter = 0;

            if (paramInfo.Length == 0) 
            {
                return basicResolve<T>();
            }

            if (registerMap.ContainsKey(type)) 
            {
                if (registerMap[type].GetType() == typeof(InstanceObjectCreator)) 
                {
                    return (T)registerMap[type].CreateObject();
                }
            }

            for (int i = 0; i < paramInfo.Length; i++)
            {
                List<Type> tmp = new List<Type>();
                foreach (var item in list)
                {
                    tmp.Add(item);
                }
                Type paramType = paramInfo[i].ParameterType;
                tmp.Add(type);
                MethodInfo method = typeof(SimpleContainer).GetMethod("recursiveResolve", BindingFlags.NonPublic | BindingFlags.Instance);
                MethodInfo generic = method.MakeGenericMethod(paramType);
                arguments[argCounter] = generic.Invoke(this, new object[] { tmp });
                argCounter++;
            }
            return (T)info.Invoke(arguments);

        }

       

        private ConstructorInfo findLongestConstructor(Type type) {
            int longestParametersNumber = 0;
            int howManyLongestConstructors = 0;
            int howManyDepedencyConstrucors = 0;
            ConstructorInfo longestInfo = null;
            ConstructorInfo dependencyInfo = null;
            ConstructorInfo[] ci;
            ci = type.GetConstructors();
            for (int i = 0; i < ci.Length; i++)
            {
                ParameterInfo[] pi = ci[i].GetParameters();
                if (pi.Length > longestParametersNumber)
                {
                    longestParametersNumber = pi.Length;
                    longestInfo = ci[i];
                    howManyLongestConstructors = 1;
                }
                else if (pi.Length == longestParametersNumber)
                {
                    howManyLongestConstructors++;
                }

                foreach (CustomAttributeData a in ci[i].CustomAttributes)
                {
                    if (a.AttributeType == typeof(DepedencyConstructorAttribute))
                    {
                        howManyDepedencyConstrucors++;
                        dependencyInfo = ci[i];
                    }

                }
            }
            if (howManyDepedencyConstrucors > 1)
            {
                throw new MoreThanOneDepedencyConsturctorException();
            }
            if (howManyDepedencyConstrucors == 1)
            {
                return dependencyInfo;
            }
            if (howManyLongestConstructors > 1)
            {
                throw new MoreThanOneLongestException();
            }
            if (howManyLongestConstructors == 1)
            {
                return longestInfo;
            }

            return null;
        }



    }

    public class Test
    {
        public ConstructorInfo findLongestConstructor(Type type)
        {
            int longestParametersNumber = 0;
            int howManyLongestConstructors = 0;
            int howManyDepedencyConstrucors = 0;
            ConstructorInfo longestInfo = null;
            ConstructorInfo dependencyInfo = null;
            ConstructorInfo[] ci;
            ci = type.GetConstructors();
            for (int i = 0; i < ci.Length; i++)
            {
                ParameterInfo[] pi = ci[i].GetParameters();
                if (pi.Length > longestParametersNumber)
                {
                    longestParametersNumber = pi.Length;
                    longestInfo = ci[i];
                    howManyLongestConstructors = 1;
                }
                else if (pi.Length == longestParametersNumber)
                {
                    howManyLongestConstructors++;
                }

                foreach (CustomAttributeData a in ci[i].CustomAttributes)
                {
                    if (a.AttributeType.ToString() == "SilnikDI2.DepedencyConstructorAttribute")
                    {
                        howManyDepedencyConstrucors++;
                        dependencyInfo = ci[i];
                    }

                }
            }
            if (howManyDepedencyConstrucors > 1)
            {
                throw new MoreThanOneDepedencyConsturctorException();
            }
            if (howManyDepedencyConstrucors == 1)
            {
                return dependencyInfo;
            }
            if (howManyLongestConstructors > 1)
            {
                throw new MoreThanOneLongestException();
            }
            if (howManyLongestConstructors == 1)
            {
                return longestInfo;
            }

            throw new Exception();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World");
        }
    }
}
