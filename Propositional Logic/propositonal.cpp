#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <iterator>
#include <vector> // Add this line for <vector> include

std::string replaceAll(std::string str, const std::string& from, const std::string& to) {
    size_t start_pos = 0;
    while ((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
    }
    return str;
}

bool evaluateExpression(const std::string& expression, const std::map<char, bool>& truthValues, std::string& error) {
    try {
        std::string expr = expression;
        for (const auto& pair : truthValues) {
            expr = replaceAll(expr, std::string(1, pair.first), pair.second ? "true" : "false");
        }

        // Use a simple logic parser to evaluate the expression
        std::string result = std::to_string(std::stoi(expr));
        return result == "1";
    } catch (const std::exception& e) {
        error = e.what();
        return false;
    }
}

int main() {
    std::string expression;
    std::cout << "Enter a propositional logic expression (e.g., (~P v Q) ^ R -> S v (~R ^ Q)):" << std::endl;
    std::getline(std::cin, expression);

    std::map<char, bool> truthValues;
    std::cout << "Enter the truth values for each variable (true or false, separated by spaces):" << std::endl;
    std::string truthInput;
    std::getline(std::cin, truthInput);
    std::istringstream iss(truthInput);

    // Adjust vector initialization to use full constructor syntax
    std::vector<std::string> truthTokens((std::istream_iterator<std::string>{iss}), std::istream_iterator<std::string>{});

    std::string vars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (size_t i = 0; i < vars.size() && i < truthTokens.size(); ++i) {
        truthValues[vars[i]] = (truthTokens[i] == "true");
    }

    std::string error;
    bool result = evaluateExpression(expression, truthValues, error);

    if (!error.empty()) {
        std::cout << "Error: " << error << std::endl;
    } else {
        std::cout << "Result: " << (result ? "true" : "false") << std::endl;
    }

    return 0;
}
