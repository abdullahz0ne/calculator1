using System;

class Calculator
{
    public static int Add(int a, int b)
    {
        return a + b;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Sum: " + Add(5, 3));
    }
}
