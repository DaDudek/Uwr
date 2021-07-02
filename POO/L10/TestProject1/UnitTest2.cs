using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SilnikDI2;

namespace TestProject1
{
    [TestClass]
    public class UnitTest2
    {
        [TestMethod]
        public void shouldReturnRegisterInstance()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            IFoo foo1 = new FooImpl();
            simpleContainer.RegisterInstance<TestProject1.IFoo>(foo1);

            IFoo foo2 = simpleContainer.Resolve<IFoo>();

            Assert.IsTrue(foo1 == foo2);
        }

        [TestMethod]
        public void shouldReturnObjectWithOneField()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            A a = simpleContainer.Resolve<A>();
            Assert.IsTrue(a.GetType() == typeof(A));
            Assert.IsTrue(a.b != null);

        }

        [TestMethod]
        public void shouldCreateWithStringInstance()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            simpleContainer.RegisterInstance("Ala ma kota");
            X x = simpleContainer.Resolve<X>();

            Assert.IsTrue(x.y != null);
            Assert.IsTrue(x.Str != null);
            Assert.IsTrue(x.Str == "Ala ma kota");

        }

        [TestMethod]
        [ExpectedException(typeof(System.Reflection.TargetInvocationException))]
        public void shouldFindCycleAndThrowException()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            ACycle fs = simpleContainer.Resolve<ACycle>();

        }


        [TestMethod]
        [ExpectedException(typeof(MoreThanOneLongestException))]
        public void shouldFindThatIsMoreThanOneLongestConstructorAndThrowException()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            twoLongConstr fs = simpleContainer.Resolve<twoLongConstr>();
        }


        [TestMethod]
        [ExpectedException(typeof(MoreThanOneDepedencyConsturctorException))]
        public void shouldFindThatIsMoreThanOneDepedencyConstructorAndThrowException()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            var fs = simpleContainer.Resolve<twoDepedencyConstr>();
        }

        [TestMethod]
        public void shouldChooseDepdencyConstrurctorOverTheLongest()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            var fs = simpleContainer.Resolve<DepedencyConstrExample>();
            simpleContainer.RegisterInstance("Ala ma kota");
            Assert.IsTrue(fs.x != null);
            Assert.IsTrue(fs.a == null);
            Assert.IsTrue(fs.b == null);

        }

        [TestMethod]
        public void shouldChooseTheLongestConstructor()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            simpleContainer.RegisterInstance("Ala ma kota");
            var fs = simpleContainer.Resolve<TheLongestConstrExample>();
            Assert.IsTrue(fs.x == null);
            Assert.IsTrue(fs.a != null);
            Assert.IsTrue(fs.b != null);

        }

        [TestMethod]
        public void shouldCreateMoreComplicateObject()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            var fs = simpleContainer.Resolve<I>();
            Assert.IsTrue(fs.k != null);
            Assert.IsTrue(fs.k.j != null);

        }


        [TestMethod]
        [ExpectedException(typeof(System.Reflection.TargetInvocationException))]
        public void shouldThrowExceptionBecauseCantResolveOneOfParam()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            var fs = simpleContainer.Resolve<X>();
        }
    }

    public class B { }

    public class A
    {
        public B b;

        public A(B b)
        {
            this.b = b;
        }
    }


    public class X {

        public Y y;
        public string Str;
        public X(Y d, string s)
        {
            this.y = d;
            this.Str = s;
        }
    }
    public class Y { }


    public class ACycle{
        public BCycle b;

        public ACycle(BCycle b1)
        {
            this.b = b1;

        }
    }

    public class BCycle{
        public ACycle a;

        public BCycle(ACycle a1)
        {
            this.a = a1;

        }
    }


    public class twoLongConstr
    {
        public twoLongConstr(int x, int y) { }

        public twoLongConstr(string x, string y) { }

    }

    public class twoDepedencyConstr
    {
        [DepedencyConstructor]
        public twoDepedencyConstr(int x) { }

        [DepedencyConstructor]
        public twoDepedencyConstr(string x, string y) { }

    }

    public class DepedencyConstrExample
    {
        public Foo x;
        public string a;
        public string b;

        [DepedencyConstructor]
        public DepedencyConstrExample(Foo foo) {
            this.x = foo;
        }

        public DepedencyConstrExample(string x, string y) 
        {
            this.a = x;
            this.b = y;
        }

    }

    public class TheLongestConstrExample
    {
        public Foo x;
        public string a;
        public string b;

        public TheLongestConstrExample(Foo foo)
        {
            this.x = foo;
        }

        public TheLongestConstrExample(string x, string y)
        {
            this.a = x;
            this.b = y;
        }

    }

    public class K {
        public J j;

        public K(J par) {
            this.j = par;
        }
    }

    public class J { }

    public class I {
        public K k;

        public I(K par) {
            this.k = par;
        }
    
    }
}

