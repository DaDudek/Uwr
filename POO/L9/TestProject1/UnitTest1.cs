using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SilnikDI;

namespace TestProject1
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void shouldReturnFooObject()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            simpleContainer.RegisterType<Foo>(false);
            Foo fs = simpleContainer.Resolve<Foo>();
            Assert.IsTrue(fs.GetType() == typeof(Foo));

        }

        [TestMethod]
        public void shouldReturnFooObjectWithoutRegister()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            Foo fs = simpleContainer.Resolve<Foo>();
            Assert.IsTrue(fs.GetType() == typeof(Foo));

        }

        [TestMethod]
        [ExpectedException(typeof(TypeWithoutRegisterException))]
        public void shouldthrowExceptionAfterResolveInterfaceWithoutRegister()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            IFoo fs = simpleContainer.Resolve<IFoo>();
        }

        [TestMethod]
        [ExpectedException(typeof(TypeWithoutRegisterException))]
        public void shouldthrowExceptionAfterResolveAbstractClassWithoutRegister()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            AbstractFoo fs = simpleContainer.Resolve<AbstractFoo>();
        }

        [TestMethod]
        public void shouldReturnFooImplObjecThatImplemenstIFooAfterRegister()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            simpleContainer.RegisterType<IFoo, FooImpl>(false);
            IFoo f = simpleContainer.Resolve<IFoo>();
            Assert.IsInstanceOfType(f, typeof(FooImpl));
        }

        [TestMethod]
        public void shouldReturnFooAbstractExtendObjecThatExtendAbstractFooAfterRegister()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            simpleContainer.RegisterType<AbstractFoo, FooAbstractExtend>(false);
            AbstractFoo f = simpleContainer.Resolve<AbstractFoo>();
            Assert.IsInstanceOfType(f, typeof(FooAbstractExtend));
        }

        [TestMethod]
        public void shouldOverrideAfterSecondRegister()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            simpleContainer.RegisterType<IFoo, FooImpl>(false);
            simpleContainer.RegisterType<IFoo, FooImpl2>(false);
            IFoo f = simpleContainer.Resolve<IFoo>();
            Assert.IsInstanceOfType(f, typeof(FooImpl2));
        }

        [TestMethod]
        public void shouldReturnSingleton()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            simpleContainer.RegisterType<IFoo, FooImpl>(true);
            IFoo f1 = simpleContainer.Resolve<IFoo>();
            IFoo f2 = simpleContainer.Resolve<IFoo>();
            Assert.IsTrue(f1 == f2);
        }

        [TestMethod]
        public void shouldNotReturnSingleton()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            simpleContainer.RegisterType<IFoo, FooImpl>(false);
            IFoo f1 = simpleContainer.Resolve<IFoo>();
            IFoo f2 = simpleContainer.Resolve<IFoo>();
            Assert.IsTrue(f1 != f2);
        }
    }

    public class Foo { 
    
    }

    public interface IFoo { }

    public abstract class AbstractFoo { }

    public class FooImpl : IFoo { }

    public class FooImpl2 : IFoo { }

    public class FooAbstractExtend : AbstractFoo { }
}
