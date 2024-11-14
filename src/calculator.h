#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <string> // Ensure string is included

class Calculator {
public:
    // Constructor with a default name
    Calculator(const std::string &name = "Simple Calculator");

    // Function declarations
    double add(double a, double b);
    double subtract(double a, double b);
    double multiply(double a, double b);
    double divide(double a, double b);

private:
    std::string name; ///< Name of the calculator
};

#endif // CALCULATOR_H
