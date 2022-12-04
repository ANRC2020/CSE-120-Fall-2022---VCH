using System; 
using System.IO;
using System.Diagnostics;  

namespace responses {
    class Program {
        static void Main(string[] args) {
            
            Console.WriteLine("This is from C#: ");

            for (int i = 0; i < args.Length; i++) // Loop through array
            {
                Console.WriteLine(args[i]);
            }a

            Console.WriteLine("Finished. ");
        }
    }
}