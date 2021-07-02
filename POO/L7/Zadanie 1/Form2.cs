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
    public partial class Form2 : Form
    {
        private EventAggregator eventAggregator;
        private string option;
        public Form2(EventAggregator eventAgr,string opt)
        {
            this.eventAggregator = eventAgr;
            this.option = opt;
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string firstName = this.firstName.Text;
            string lastName = this.lastName.Text;
            string adress = this.adres.Text;
            Person person = new Person(firstName,lastName,adress);
            if (option == "Wykładowcy") {
                DataBase.addTutor(person);
            }
            else if (option == "Studenci")
            {
                DataBase.addStudent(person);
            }
            eventAggregator.RaiseNotification<AddUserNotification>(new AddUserNotification(person,option));
            this.Close();
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
