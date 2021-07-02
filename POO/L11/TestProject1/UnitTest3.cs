using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SilnikDL3;

namespace TestProject1
{
    [TestClass]
    public class UnitTest3
    {
        [TestMethod]
        public void shouldInjectionPublicFieldWithAttribute()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            DI3Foo2 fs = simpleContainer.Resolve<DI3Foo2>();
            Assert.IsTrue(fs.field1 != null);

        }

        [TestMethod]
        public void shouldInjectionMoreThanOneFieldWithAttribute()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            DI3Foo3 fs = simpleContainer.Resolve<DI3Foo3>();
            Assert.IsTrue(fs.field2 != null);
            Assert.IsTrue(fs.field2.field1 != null);
            Assert.IsTrue(fs.field3 != null);
        }


        [TestMethod]
        public void shouldInjectionToObjectWithDeepRecursion()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            DI3D fs = simpleContainer.Resolve<DI3D>();
            Assert.IsTrue(fs.fieldA != null);
            Assert.IsTrue(fs.fieldB != null);
            Assert.IsTrue(fs.fieldC != null);
            Assert.IsTrue(fs.fieldC.fieldA2 != null);
            Assert.IsTrue(fs.fieldA2 == null);

        }


        [TestMethod]
        public void shouldBuildUpObjectWithOneField() 
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            DI3Foo2 fs = new DI3Foo2();
            simpleContainer.BuildUp<DI3Foo2>(fs);
            Assert.IsTrue(fs.field1 != null);
        }

        [TestMethod]
        public void shouldBuildUpObjectWithMoreThanOneField()
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            DI3Foo3 fs = new DI3Foo3();
            simpleContainer.BuildUp<DI3Foo3>(fs);
            Assert.IsTrue(fs.field2 != null);
            Assert.IsTrue(fs.field2.field1 != null);
            Assert.IsTrue(fs.field3 != null);
        }

        [TestMethod]
        public void shouldReturnTheSameContainer() 
        {
            SimpleContainer simpleContainer = new SimpleContainer();
            ServiceLocator.SetContainerProvider(() => simpleContainer);
            SimpleContainer containerFromLocator = ServiceLocator.Current.GetInstance<SimpleContainer>();
            SimpleContainer containerFromLocator2 = ServiceLocator.Current.GetInstance<SimpleContainer>();
            Assert.IsTrue(containerFromLocator.Equals(simpleContainer));
            Assert.IsTrue(containerFromLocator.Equals(containerFromLocator2));



        }

        [TestMethod]
        public void shouldReturnDifferentContainers()
        {
            ServiceLocator.SetContainerProvider(() => new SimpleContainer());
            SimpleContainer containerFromLocator = ServiceLocator.Current.GetInstance<SimpleContainer>();
            SimpleContainer containerFromLocator2 = ServiceLocator.Current.GetInstance<SimpleContainer>();
            Assert.IsTrue(!containerFromLocator.Equals(containerFromLocator2));

        }

        [TestMethod]
        public void shouldResolveProperlyByLocator() 
        {
            ServiceLocator.SetContainerProvider(() => new SimpleContainer());
            DI3Foo3 fs = ServiceLocator.Current.GetInstance<DI3Foo3>();
            Assert.IsTrue(fs.field2 != null);
            Assert.IsTrue(fs.field2.field1 != null);
            Assert.IsTrue(fs.field3 != null);

        }
    }

    public class DI3Foo
    {
        public DI3Foo(){ }
    }

    public class DI3Foo2
    {
        [SilnikDL3.DepedencyProperty]
        public DI3Foo field1 { get; set; }
        public DI3Foo2() { }
    }

    public class DI3Foo3
    {
        [DepedencyProperty]
        public DI3Foo2 field2 { get; set; }

        [DepedencyProperty]
        public DI3Foo field3 { get; set; }
        public DI3Foo3() { }
    }

    public class DI3A {
        public DI3A() { }
    }

    public class DI3B {
        public DI3A fieldA { get; set; }

        public DI3B(DI3A f) {
            this.fieldA = f;
        }
    }

    public class DI3C {
        public DI3A fieldA { get; set; }
        public DI3B fieldB { get; set; }

        [DepedencyProperty]
        public DI3A fieldA2 { get; set; }

        public DI3C(DI3A f, DI3B f2)
        {
            this.fieldA = f;
            this.fieldB = f2;
        }
    }
    public class DI3D
    {
        public DI3A fieldA { get; set; }
        public DI3B fieldB { get; set; }

        public DI3A fieldA2 { get; set; }

        [DepedencyProperty]
        public DI3C fieldC { get; set; }


        [DepedencyConstructor]
        public DI3D(DI3A f, DI3B f2)
        {
            this.fieldA = f;
            this.fieldB = f2;
        }

        public DI3D(DI3A f, DI3B f2, DI3A f3)
        {
            this.fieldA = f;
            this.fieldB = f2;
            this.fieldA2 = f3;
        }
    }

}
