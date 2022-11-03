using System;

class response {
    static void printInfo(string name, int id) {
    Console.WriteLine(name);
    Console.WriteLine(id);
    }

    static Array generateArray() {
        
        int[] myNum = {10, 20, 30, 40}; 
        return myNum;
    }

    static public void Main(String[] args)
    {
        // dict = recieve();
        printInfo("name", 0);
        Array arr = generateArray();
        Console.WriteLine(arr);
        // send arr back to python program.
    }
}