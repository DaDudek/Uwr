using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp1
{

    public interface ISubscriber<T> {
        void Handle(T notification);
    }

    class CategoryChooseNotification {
        private string _category;

        public CategoryChooseNotification(string category) {
            this._category = category;
        }

        public string getCategory() {
            return this._category;
        }
    
    }

    class UserChooseNotification {
        private Person _person;

        public UserChooseNotification(Person person) {
            this._person = person;
        }

        public Person getPerson() {
            return this._person;
        }
    }

    class AddUserNotification {

        private Person _person;
        private string _option;

        public AddUserNotification(Person person, string option)
        {
            this._person = person;
            this._option = option;
        }

        public Person getPerson() {
            return _person;
        }

        public string getOption() {
            return _option;
        }

    }

    class ModifyUserNotification {
        private Person _person;

        public ModifyUserNotification(Person person)
        {
            this._person = person;
        }

        public Person getPerson() {
            return _person;
        }
    }

    class TreeListEditor :
        ISubscriber<AddUserNotification>,
        ISubscriber<ModifyUserNotification>
    {

        private System.Windows.Forms.TreeView treeView;

        public TreeListEditor(System.Windows.Forms.TreeView View){       
                this.treeView = View;
            }

        public void Handle(AddUserNotification notification)
        {

            if (notification.getOption() == "Wykładowcy")
            {
                treeView.Nodes[0].Nodes.Clear();
                List<Person> Tutors = DataBase.getTutors();

                foreach (Person tutor in Tutors)
                {
                    this.treeView.Nodes[0].Nodes.Add(tutor.ToString());
                }
            }
            else if (notification.getOption() == "Studenci")
            {
                treeView.Nodes[1].Nodes.Clear();
                List<Person> Students = DataBase.getStudents();

                foreach (Person student in Students)
                {
                    this.treeView.Nodes[1].Nodes.Add(student.ToString());
                }
            }
            
        }

        public void Handle(ModifyUserNotification notification)
        {
            treeView.Nodes[0].Nodes.Clear();
            List<Person> Tutors = DataBase.getTutors();

            foreach (Person tutor in Tutors)
            {
                this.treeView.Nodes[0].Nodes.Add(tutor.ToString());
            }
            treeView.Nodes[1].Nodes.Clear();

            List<Person> Students = DataBase.getStudents();

            foreach (Person student in Students)
            {
                this.treeView.Nodes[1].Nodes.Add(student.ToString());
            }
        }
    }

    class DataTableEditor :
       ISubscriber<AddUserNotification>,
       ISubscriber<ModifyUserNotification>,
       ISubscriber<CategoryChooseNotification>,
       ISubscriber<UserChooseNotification>
    {
        private System.Windows.Forms.DataGridView dataGrid;

        public DataTableEditor(System.Windows.Forms.DataGridView grid) {
            this.dataGrid = grid;
        }

        public void Handle(AddUserNotification notification)
        {
            if (notification.getOption() == "Wykładowcy")
            {
                this.dataGrid.Rows.Clear();
                List<Person> Tutors = DataBase.getTutors();

                foreach (Person tutor in Tutors)
                {
                    this.dataGrid.Rows.Add(tutor.getFirstName(), tutor.getLastName(), tutor.getAddres());
                }

            }
            else if (notification.getOption() == "Studenci")
            {
                this.dataGrid.Rows.Clear();

                List<Person> Students = DataBase.getStudents();

                foreach (Person student in Students)
                {
                    this.dataGrid.Rows.Add(student.getFirstName(), student.getLastName(), student.getAddres());
                }
            }
        }

        public void Handle(ModifyUserNotification notification)
        {
            this.dataGrid.Rows.Clear();
            this.dataGrid.Rows.Add(notification.getPerson().getFirstName(),
                notification.getPerson().getLastName(), notification.getPerson().getAddres());

        }

        public void Handle(CategoryChooseNotification notification)
        {
            if (notification.getCategory() == "Wykładowcy") {
                List<Person> Tutors = DataBase.getTutors();
                this.dataGrid.Rows.Clear();
                foreach (Person tutor in Tutors)
                {
                    this.dataGrid.Rows.Add(tutor.getFirstName(), tutor.getLastName(), tutor.getAddres());
                }
            }

            else if (notification.getCategory() == "Studenci")
            {
                List<Person> Students = DataBase.getStudents();
                this.dataGrid.Rows.Clear();
                foreach (Person student in Students)
                {
                    this.dataGrid.Rows.Add(student.getFirstName(), student.getLastName(), student.getAddres());
                }
            }


        }

        public void Handle(UserChooseNotification notification)
        {
            List<Person> Tutors = DataBase.getTutors();
            this.dataGrid.Rows.Clear();
            Person person = notification.getPerson();
            this.dataGrid.Rows.Add(person.getFirstName(), person.getLastName(), person.getAddres());
        }
    }

    public class EventAggregator {
        private Dictionary<Type, List<object>> _subscribers = new Dictionary<Type, List<object>>();


        public void RegisterSubscriber<T>(ISubscriber<T> subscriber) 
        {
            if (!_subscribers.ContainsKey(typeof(T))) 
            { 
                _subscribers.Add(typeof(T),new List<object>());
            }

            _subscribers[typeof(T)].Add(subscriber);

        }

        public void UnregisterSubscriber<T>(ISubscriber<T> subscriber)
        {
            if (!_subscribers.ContainsKey(typeof(T)))
            {
                _subscribers[typeof(T)].Remove(subscriber);
            }
        }

        public void RaiseNotification<T>(T notification)
        {
            foreach (var subscriber
                in _subscribers[typeof(T)].OfType<ISubscriber<T>>())
            {
               subscriber.Handle(notification);
            }
        }


    }


    class DataBase
    {
        private static List<Person> students = new List<Person>
            {
                new Person("Tomasz","Sikor","Adres1"),
                new Person("Jerzy", "Tomaszewski", "Adres2")
            };

        private static List<Person> tutors = new List<Person>
            {
                new Person("Jan","Kochanowski","Adres3"),
                new Person("Tomasz", "Makowski", "Adres4")
            };

        public static List<Person> getStudents() {
            return students;
        }

        public static List<Person> getTutors()
        {

            return tutors;
        }

        public static void addStudent(Person person) {
            students.Add(person);
       
                }

        public static void addTutor(Person person)
        {
            tutors.Add(person);

        }

        public static void removeStudent(Person person)
        {
            students.Remove(person);

        }

        public static void removeTutor(Person person)
        {
            tutors.Remove(person);

        }

    }

    class Person {
        private string _firstName;
        private string _lastName;
        private string _addres;

        public Person(string firstname, string lastname, string addres) {
            this._firstName = firstname;
            this._lastName = lastname;
            this._addres = addres;
        }

        public string getFirstName() {
            return this._firstName;
        }
        public string getLastName()
        {
            return this._lastName;
        }

        public string getAddres()
        {
            return this._addres;
        }

        public override string ToString() {
            return _firstName + " " + _lastName;
        }
    }
}
