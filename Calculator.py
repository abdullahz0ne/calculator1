using System;

class Calculator
{
    public static double Divide(double a, double b)
    {
        if (b == 0)
        {
            Console.WriteLine("Error: Cannot divide by zero.");
            return double.NaN;
        }
        return a / b;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Quotient: " + Divide(10, 2));
    }
}

