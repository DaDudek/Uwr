using System;
using System.Collections.Generic;
using System.Text;

namespace SilnikDL3
{
    public delegate SimpleContainer ContainerProviderDelegate();
    public class ServiceLocator
    {
        private static ContainerProviderDelegate _provider;
        private static ServiceLocator _current;
        public static void SetContainerProvider(ContainerProviderDelegate ContainerProvider) 
        {
            _provider = ContainerProvider;
        }

        public static ServiceLocator Current
        {
            get {
                if (_current == null) 
                {
                    _current = new ServiceLocator();
                }
                return _current;
            }
        }

        public T GetInstance<T> () where T : class
        {
            var obj = _provider();
            if (typeof(T).Equals(obj.GetType()))
            {
                return (T)(object)obj;
            }
            return _provider().Resolve<T>();
        }
    }
}
