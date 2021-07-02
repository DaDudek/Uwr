using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    static class Program
    {
        /// <summary>
        /// Główny punkt wejścia dla aplikacji.
        /// </summary>
        [STAThread]
        static void Main()
        {
            EventAggregator eventAgregator = new EventAggregator();
            Form1 form1 = new Form1(eventAgregator);
            TreeListEditor treeListEditor = new TreeListEditor(form1.getTree());
            DataTableEditor dataTableEditor = new DataTableEditor(form1.getTable());

            eventAgregator.RegisterSubscriber<AddUserNotification>(treeListEditor);
            eventAgregator.RegisterSubscriber<ModifyUserNotification>(treeListEditor);


            eventAgregator.RegisterSubscriber<AddUserNotification>(dataTableEditor);
            eventAgregator.RegisterSubscriber<ModifyUserNotification>(dataTableEditor);
            eventAgregator.RegisterSubscriber<CategoryChooseNotification>(dataTableEditor);
            eventAgregator.RegisterSubscriber<UserChooseNotification>(dataTableEditor);


            Application.EnableVisualStyles();
            //Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(form1);
        }
    }
}
