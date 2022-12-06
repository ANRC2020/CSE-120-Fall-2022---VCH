using System; 
using System.IO;
using System.Diagnostics;  

namespace responses {
    class Program {
        static void Main(string[] args) {
            
            Console.WriteLine("This is from C#: ");
            // Console.WriteLine("Patient Name: " + args[0]);

            executePython();
            Console.WriteLine("Patient Name: " + args[0]);
        }
        public static void executePython() {
            String FileName = "sub.py";
            ProcessStartInfo ProcessInfo = new ProcessStartInfo("python3");
            ProcessInfo.UseShellExecute = false;
            ProcessInfo.RedirectStandardOutput = true;
            ProcessInfo.Arguments = FileName;

            Process myprocess = new Process(); 
            myprocess.StartInfo = ProcessInfo;
            myprocess.Start();

            StreamReader myStreamReader = myprocess.StandardOutput;
            String myString = myStreamReader.ReadLine();
            myprocess.WaitForExit();
            myprocess.Close();
            Console.WriteLine("Value recieved from script: " + myString);
        }
    }
}