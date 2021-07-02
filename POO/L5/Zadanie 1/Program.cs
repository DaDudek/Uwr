using System;
using System.IO;
using System.Net;
using System.Net.Mail;
using System.Net.Mime;

namespace POO_5._1
{
	class SmtpFacade {
		public void Send
			(string From, string To, string Subject,
			string Body, Stream Attachment, string AttachmentMimeType) {
			Console.WriteLine("start");
			String password = "twoje hasło";

			var mailMessage = new MailMessage
			{
				From = new MailAddress(From),
				Subject = Subject,
				Body = Body,
				IsBodyHtml = true,
			};
			mailMessage.To.Add(To);

			var attachment = new Attachment(Attachment, AttachmentMimeType);
			mailMessage.Attachments.Add(attachment);

			var smtpClient = new SmtpClient("smtp.gmail.com")
			{
				Port = 587,
				Credentials = new NetworkCredential(From, password),
				EnableSsl = true,
			};

			smtpClient.Send(mailMessage);
			Console.WriteLine("koniec");
		}
	}

	class Program
	{
		static void Main(string[] args)
		{
			SmtpFacade smtpFacade = new SmtpFacade();
			String path = @"C:\Users\HP\Desktop\POO\POO - lista 5\Zadanie 1\t.txt";
			smtpFacade.Send("huhcia3@gmail.com", "huhcia3@gmail.com", "test", "test123", 
				new FileStream(path, FileMode.Open, FileAccess.Read), MediaTypeNames.Text.Plain);
			Console.WriteLine("Hello World!");
		}
	}
}
