using System;

class Calculator
{
    public static int Subtract(int a, int b)
    {
        return a - b;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Difference: " + Subtract(10, 4));
    }
}
