import { useState } from "react";
import Display from "../Display/Display";
import Keypad from "../Keypad/Keypad";
import "./Calculator.css";
import History from "../History/History";


function Calculator() {
    const [expression, setExpression] = useState("");
    const [result, setResult] = useState("");
    const [calculationDone, setCalculationDone] = useState(false)
    const [angleMode, setAngleMode] = useState("DEG")
    const [history, setHistory] = useState([]);

    const handleClear = () => {
        setExpression("");
        setResult("")
    }


    const fetchHistory = async () => {
        try {
            const response = await fetch(
                "http://127.0.0.1:5000/history"
            );

            const data = await response.json();

            if (response.ok) {
                setHistory(data);
            }
        } catch (error) {
            console.error("Failed to fetch history:", error);
        }
    };


    const clearHistory = async () => {
        try {
            const response = await fetch(
                "http://127.0.0.1:5000/history",
                {
                    method: "DELETE",
                }
            );

            if (response.ok) {
                setHistory([]);
            }
        } catch (error) {
            console.error("Failed to clear history:", error);
        }
    };



    const deleteHistory = async (index) => {
        try {
            const response = await fetch(
                `http://127.0.0.1:5000/history/${index}`,
                {
                    method: "DELETE",
                }
            );

            if (response.ok) {
                fetchHistory();
            }
        } catch (error) {
            console.error("Failed to delete history item:", error);
        }
    };

    const handleMemory = async (operation) => {
            let value = null;

            if (operation === "M+" || operation === "M-") {
                value = Number(result);

                if (Number.isNaN(value)) {
                    return;
                }
            }

            try {
                const response = await fetch(
                    "http://127.0.0.1:5000/memory",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            operation: operation,
                            value: value,
                        }),
                    }
                );

                const data = await response.json();

                if (!response.ok) {
                    setResult(data.error);
                    return;
                }

                if (operation === "MR") {
                    setExpression(String(data.result));
                    setResult("");
                    setCalculationDone(false);
                }

            } catch (error) {
                console.error(error);
                setResult("Server error");
            }
        };



    const handleBackspace = () => {
        if (calculationDone) {
            setExpression(String(result).slice(0, -1));
            setResult("");
            setCalculationDone(false);
            return;
        }

        setExpression((previous) => previous.slice(0, -1));
        };

    const handleCalculate = async (expressionToCalculate = expression) => {
        console.log("Calculating:", expression);

        try {
            const response = await fetch(
                "http://127.0.0.1:5000/calculate",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        expression: expressionToCalculate,
                        angle_mode: angleMode,
                    }),
                }
            );

            const data = await response.json();

            if (!response.ok) {
                setResult(data.error);
                return;
            }

            setResult(data.result);
            fetchHistory();

        } catch (error) {
            console.error("Server error:", error);
            setResult("Server error");
        }
    };

    return (
        <div className="calculator">

            <Display
                expression={expression}
                result={result}
            />

            <Keypad
                expression={expression}
                result={result}
                setExpression={setExpression}
                setResult={setResult}
                calculationDone={calculationDone}
                setCalculationDone={setCalculationDone}
                angleMode={angleMode}
                setAngleMode={setAngleMode}
                handleCalculate={handleCalculate}
                handleClear={handleClear}
                handleBackspace={handleBackspace}
                handleMemory = {handleMemory}
            />
            <History
                history = {history}
                clearHistory={clearHistory}
                setExpression = {setExpression}
                deleteHistory = {deleteHistory}
            />

        </div>
    );
}

export default Calculator;
