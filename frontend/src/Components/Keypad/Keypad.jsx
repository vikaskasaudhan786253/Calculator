import Button from "../Button/Button";
import "./Keypad.css";
import ControlPad from "./ControlPad/ControlPad";
import ScientificPad from "./ScientificPad/ScientificPad";
import MainPad from "./MainPad/MainPad";
import {useEffect, useState } from "react";


function Keypad({
    expression,
    result,
    setExpression,
    setResult,
    calculationDone,
    setCalculationDone,
    angleMode,
    setAngleMode,
    handleCalculate,
    handleClear,
    handleBackspace,
    handleMemory,
}) {

    const handleDecimal = () => {
            setExpression((previous) => {
                // Don't allow a second decimal in the current number
                const match = previous.match(/(\d*\.?\d*)$/);

                if (!match) {
                    return `${previous}0.`;
                }

                const currentNumber = match[1];

                if (currentNumber.includes(".")) {
                    return previous;
                }

                return `${previous}.`;
            });
        };


    useEffect(() => {
    const handleKeyDown = (event) => {
        const key = event.key;

        // Numbers
        if (/^[0-9]$/.test(key)) {
            handleClick(key);
            return;
        }

        // Decimal
        if (key === ".") {
            handleClick(".");
            return;
        }

        // Operators
        if (["+", "-", "*", "/", "%", "^"].includes(key)) {
            handleClick(key);
            return;
        }

        // Parentheses
        if (key === "(" || key === ")") {
            handleClick(key);
            return;
        }

        // Calculate
        if (key === "Enter" || key === "=") {
            handleClick("=");
            return;
        }

        // Backspace
        if (key === "Backspace") {
            handleClick("⌫");
            return;
        }

        // Clear
        if (key === "Escape") {
            handleClick("C");
        }
    };

    window.addEventListener("keydown", handleKeyDown);

    return () => {
        window.removeEventListener("keydown", handleKeyDown);
    };
}, [expression, result, calculationDone]);

    const applyFunctionToLastValue = (expression, functionName)=>{
        if(!expression){
            return ""
        }

        // If the expression ends with a parenthesized expression
        if (expression.endsWith(")")) {
            let depth = 0;

            for (let i = expression.length - 1; i >= 0; i--) {
                if (expression[i] === ")") {
                    depth++;
                } else if (expression[i] === "(") {
                    depth--;

                    if (depth === 0) {
                        // Find where the function name starts
                    let start = i - 1;

                    while (
                        start >= 0 &&
                        /[a-zA-Z0-9_]/.test(expression[start])
                    ) {
                        start--;
                    }

                    start++;

                    const before = expression.slice(0, start);
                    const value = expression.slice(start);

                    return `${before}${functionName}(${value})`;
                    }
                }
            }
        }


         // If the expression ends with Ans
    if (expression.endsWith("Ans")) {
            const start = expression.length - 3;

            const before = expression.slice(0, start);
            const value = expression.slice(start);

                return `${before}${functionName}(${value})`;
            }
        // Otherwise, look for a number at the end

        const match = expression.match(/(\d+(?:\.\d+)?)$/);
        if(!match){
            return expression;
        }

        const number = match[1]

        const start = expression.slice(0, -number.length);

        return `${start}${functionName}(${number})`
    }

    const handleClick = (value) => {

        if (["DEG", "RAD", "GRAD"].includes(value)) {
            setAngleMode((previous) => {
                if (previous === "DEG") {
                    return "RAD";
                }
                if (previous === "RAD") {
                    return "GRAD";
                }
                return "DEG";
            });
            return;
        }

        if(calculationDone){
            const operators = ["+", "-", "*", "/"]
            if(operators.includes(value)){
                setExpression(String(result));
                setResult("")
            }else if(["√", "x²", "x³", "1/x","!","%"].includes(value)){
                setExpression(String(result));
                setResult("")
            }
            else{
                setExpression("")
                setResult("")
            }
            setResult("")
            setCalculationDone(false)
        }

        if(value === "C"){
            handleClear();
            return;
        }

        if (value === "AC") {
            handleClear();
            setCalculationDone(false);
            setAngleMode("DEG");
            setExpression("");
            setResult("");
            return;
        }

        if(value === "⌫"){
            handleBackspace();
            return;
        }

        if (value === "!") {
            setExpression((previous) => {
                if (!previous) {
                    return "";
                }
                return `${previous}!`;
            });
            return;
        }

        if (value === "%") {
            setExpression((previous) => {
                if (!previous) {
                    return "";
                }

                return `${previous}%`;
            });

            return;
        }

        if (value === "=") {
            let finalExpression = expression;

            if (
                (expression.includes("ncr(") ||
                    expression.includes("npr(")) &&
                !expression.endsWith(")")
            ) {
                finalExpression = `${expression})`;
                setExpression(finalExpression);
            }

            handleCalculate(finalExpression);
            setCalculationDone(true);

            return;
        }

        if (value === "√") {
            setExpression((previous) =>
                applyFunctionToLastValue(previous, "sqrt")
            );
            return;
        }
        if (value === "x²") {
            setExpression((previous) =>
                applyFunctionToLastValue(previous, "square")
            );
            return;
        }
        if (value === "x³") {
            setExpression((previous) =>
                applyFunctionToLastValue(previous, "cube")
            );
            return;
        }
        if (value === "1/x") {
            setExpression((previous) =>
                applyFunctionToLastValue(previous, "reciprocal")
            );
            return;
        }

        // Ans
        if (value === "Ans") {
            setExpression((previous) => {
                if (!previous) {
                    return "Ans";
                }

                return `${previous}Ans`;
            });

            return;
        }

        if (["sin", "cos", "tan", "asin", "acos", "atan",
        "ln",
        "log",
        "exp",
        "sinh",
        "cosh",
        "tanh",
        "asinh",
        "acosh",
        "atanh"].includes(value)) {
            setExpression((previous) =>
            applyFunctionToLastValue(previous, value)
        );
            return;
        }


        if (["DEG", "RAD", "GRAD"].includes(value)) {
            setAngleMode((previous) => {
                if (previous === "DEG") {
                    return "RAD";
                }
                if (previous === "RAD") {
                    return "GRAD";
                }
                return "DEG";
            });
            return;
        }

        if (value === "nCr" || value === "nPr") {
            setExpression((previous) => {
                if (!previous) {
                    return "";
                }

                const match = previous.match(/(\d+(?:\.\d+)?)$/);

                if (!match) {
                    return previous;
                }

                const number = match[1];
                const start = previous.slice(0, -number.length);

                const functionName = value === "nCr" ? "ncr" : "npr";

                return `${start}${functionName}(${number},`;
            });

            return;
        }

        if (value === ".") {
            handleDecimal();
            return;
        }

        setExpression((previous) => previous + value);
    };

    return (
        <div className="keypad">

            <ControlPad handleClick = {handleClick}/>


            <MainPad handleClick={handleClick}/>


            <ScientificPad
                handleClick={handleClick}
                angleMode={angleMode}
                handleMemory = {handleMemory}
            />



            <div className="equals-button">
                <Button
                value="="
                onClick={handleClick}
            />
            </div>


        </div>
    );
}

export default Keypad;
