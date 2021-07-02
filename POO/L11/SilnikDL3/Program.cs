using System;
using System.Collections.Generic;
using System.Reflection;
using Microsoft.VisualBasic.CompilerServices;

namespace SilnikDL3
{
    public class SimpleContainer
    {
        private Dictionary<Type, ObjectCreator> registerMap;

        public SimpleContainer()
        {
            registerMap = new Dictionary<Type, ObjectCreator>();
        }

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

        private T basicResolve<T>(List<Type> list) where T : class
        {
            Type type = typeof(T);
            List<Type> tmp = new List<Type>();
            foreach (var item in list)
            {
                tmp.Add(item);
            }
            tmp.Add(type);
            if (type.IsInterface || type.IsAbstract)
            {
                if (registerMap.ContainsKey(type))
                {
                    ObjectCreator creator = registerMap[type];
                    var obj = (T)creator.CreateObject();
                    this.ResolveProperties<T>(tmp, obj);
                    return obj;
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
                    var obj =  (T)creator.CreateObject();
                    this.ResolveProperties<T>(tmp, obj);
                    return obj;
                }
                else
                {
                    var obj = (T)Activator.CreateInstance(type);
                    this.ResolveProperties<T>(tmp, obj);
                    return obj;
                }

            }
        }

        public void BuildUp<T>(T Instance) where T: class
        {
            this.ResolveProperties<T>(new List<Type>(), Instance);
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
                List<Type> tmp = new List<Type>();
                foreach (var item in list)
                {
                    tmp.Add(item);
                }
                tmp.Add(type);
                return basicResolve<T>(tmp);
            }
            ParameterInfo[] paramInfo = info.GetParameters();
            Object[] arguments = new object[info.GetParameters().Length];
            int argCounter = 0;

            if (paramInfo.Length == 0)
            {
                List<Type> tmp = new List<Type>();
                foreach (var item in list)
                {
                    tmp.Add(item);
                }
                tmp.Add(type);
                return basicResolve<T>(tmp);
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
            list.Add(type);
            var createdObject = (T)info.Invoke(arguments);
            this.ResolveProperties<T>(list,createdObject);
            return createdObject;
        }

        private void ResolveProperties<T>(List<Type> list, T objectToResolve) where T : class 
        {
            PropertyInfo[] info = typeof(T).GetProperties();
            foreach (var property in info)
            {
                var attributes = property.CustomAttributes;
                
                foreach (var customAttribute in attributes)
                {
                    if ((customAttribute.AttributeType == typeof(DepedencyPropertyAttribute)) && property.CanWrite) 
                    {
                        List<Type> tmp = new List<Type>();
                        foreach (var item in list)
                        {
                            tmp.Add(item);
                        }
                        Type propertyType = property.PropertyType;
                        tmp.Add(typeof(T));
                        MethodInfo method = typeof(SimpleContainer).GetMethod("recursiveResolve", BindingFlags.NonPublic | BindingFlags.Instance);
                        MethodInfo generic = method.MakeGenericMethod(propertyType);
                        // stworzony obiekt pola
                        var objectProperty =Convert.ChangeType(generic.Invoke(this, new object[] { tmp }),propertyType);

                        MethodInfo[] methInfos = property.GetAccessors();
                        foreach (var methodInfo in methInfos) 
                        {
                            if (methodInfo.ReturnType == typeof(void)) 
                            {
                                //this.pole = obiekt
                                methodInfo.Invoke(objectToResolve, new object[] { objectProperty});
                            }
                        }
                    }

                             
                }

            }
        }



        private ConstructorInfo findLongestConstructor(Type type)
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


  
    public class DI3Foo
    {
        public DI3Foo() { }
    }

    public class DI3Foo2
    {
        [SilnikDL3.DepedencyProperty]
        public DI3Foo field1 { get; set; }
        public DI3Foo2() { }
    }

    class Program
    {
        static void Main(string[] args)
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            DI3Foo2 fs = simpleContainer.Resolve<DI3Foo2>();
            Console.WriteLine(fs.field1);
        }
    }
}
