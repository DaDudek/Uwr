using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        private EventAggregator eventAggregator;
        private string option;
        public Form1(EventAggregator eventAgr)
        {
            this.eventAggregator = eventAgr;
            InitializeComponent();
            List<Person> Tutors = DataBase.getTutors();

            foreach (Person tutor in Tutors)
            {
                this.treeView1.Nodes[0].Nodes.Add(tutor.ToString());
            }


            List<Person> Students = DataBase.getStudents();

            foreach (Person student in Students)
            {
                this.treeView1.Nodes[1].Nodes.Add(student.ToString());
            }
        }

        public TreeView getTree() {
            return this.treeView1;
        }

        public DataGridView getTable() {
            return this.dataGridView1;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            if (treeView1.SelectedNode.Text == "Wykładowcy")
            {
                this.button1.Text = "Dodaj";
                this.eventAggregator.RaiseNotification<CategoryChooseNotification>(new CategoryChooseNotification("Wykładowcy"));
            }
            else if (treeView1.SelectedNode.Text == "Studenci")
            {
                this.button1.Text = "Dodaj";
                this.eventAggregator.RaiseNotification<CategoryChooseNotification>(new CategoryChooseNotification("Studenci"));
            }
            else {
                this.button1.Text = "Zmień";
                List<Person> Tutors = DataBase.getTutors();
                List<Person> Students = DataBase.getStudents();
                List<Person> all = Tutors.Concat(Students).ToList();
                string text = treeView1.SelectedNode.Text;
                string[] words = text.Split(' ');
                Person _person = null;

                 foreach (Person person in all) {
                    if (person.getFirstName() == words[0] && person.getLastName() == words[1]) {
                        _person = person;
                    }
                 }
                this.eventAggregator.RaiseNotification<UserChooseNotification>(
                    new UserChooseNotification(_person));
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "Dodaj")
            {
                Form2 form2 = new Form2(eventAggregator, treeView1.SelectedNode.Text);
                form2.ShowDialog();
            }
            else if (button1.Text == "Zmień")
            {
                string firstName = dataGridView1.Rows[0].Cells[0].Value.ToString();
                string lastName = dataGridView1.Rows[0].Cells[1].Value.ToString();
                string addres = dataGridView1.Rows[0].Cells[2].Value.ToString();
                Person personToRemove = null;
                bool fromTutors = false;

                List<Person> Tutors = DataBase.getTutors();
                foreach (Person person in Tutors) {
                    if (person.getAddres() == addres && person.getFirstName() == firstName && person.getLastName() == lastName) {
                        option = "Wykładowca";
                        personToRemove = person;
                        fromTutors = true;
                    }
                }

                List<Person> Students = DataBase.getStudents();
                foreach (Person person in Students)
                {
                    if (person.getAddres() == addres && person.getFirstName() == firstName && person.getLastName() == lastName)
                    {
                        option = "Student";
                        personToRemove = person;

                    }
                }

                if (fromTutors)
                {
                    DataBase.removeTutor(personToRemove);
                }
                else {
                    DataBase.removeStudent(personToRemove);
                }


                dataGridView1.ReadOnly = false;
                button1.Text = "Zapisz";
            }
            else if (button1.Text == "Zapisz") {
                string firstName = dataGridView1.Rows[0].Cells[0].Value.ToString();
                string lastName = dataGridView1.Rows[0].Cells[1].Value.ToString();
                string addres = dataGridView1.Rows[0].Cells[2].Value.ToString();
                Person person = new Person(firstName, lastName, addres);
                if (option == "Student")
                {
                    DataBase.addStudent(person);
                }
                else if (option == "Wykładowca") {
                    DataBase.addTutor(person);
                }
                eventAggregator.RaiseNotification<ModifyUserNotification>(new ModifyUserNotification(person));
                dataGridView1.ReadOnly = true;
                button1.Text = "Zmień";


            }
        }
    }
}
