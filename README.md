# 🧮 Scientific Calculator

A full-stack **Scientific Calculator** built using **React + Vite** for the frontend and **Python + Flask** for the backend.

The project is designed to behave like a modern **Casio-style scientific calculator**, while also implementing a custom expression tokenizer, parser, calculator engine, memory system, calculation history, keyboard support, and scientific functions.

---

## 📸 Overview

This project is more than a basic calculator.

The application is divided into two major parts:

- **Frontend** → React + Vite
- **Backend** → Python + Flask

The frontend provides the calculator interface, while the backend is responsible for expression processing, mathematical operations, parsing, memory, history, and scientific calculations.

---

# ✨ Features

## 🔢 Basic Arithmetic

The calculator supports:

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`
- Floor division `//`
- Modulo `%`
- Power `^`
- Power `**`
- Parentheses
- Decimal numbers
- Unary `+` and `-`

Examples:

```text
2 + 3
10 - 4
5 * 6
20 / 4
10 // 3
10 % 3
2 ^ 5
(2 + 3) * 4
```

---

# 🔬 Scientific Functions

The calculator supports common scientific operations.

### Basic scientific operations

- Square root `√`
- Square `x²`
- Cube `x³`
- Reciprocal `1/x`
- Factorial `!`
- Percentage `%`

### Logarithmic functions

- Natural logarithm `ln`
- Base-10 logarithm `log`
- Logarithm with custom base
- Exponential `exp`

### Trigonometric functions

- `sin`
- `cos`
- `tan`

### Inverse trigonometric functions

- `asin`
- `acos`
- `atan`

### Hyperbolic functions

- `sinh`
- `cosh`
- `tanh`

### Inverse hyperbolic functions

- `asinh`
- `acosh`
- `atanh`

---

# 📐 Angle Modes

The calculator supports three angle modes:

```text
DEG
RAD
GRAD
```

### DEG

Degrees:

```text
sin(30) = 0.5
```

### RAD

Radians:

```text
sin(π/6) = 0.5
```

### GRAD

Gradians are also supported.

The angle mode can be changed directly from the calculator interface.

---

# 🔢 Combinatorics

The calculator supports:

### Combination

```text
nCr
```

Example:

```text
5 nCr 2
```

Result:

```text
10
```

### Permutation

```text
nPr
```

Example:

```text
5 nPr 2
```

Result:

```text
20
```

---

# 🧠 Mathematical Constants

The calculator supports common mathematical constants.

### Pi

```text
π
```

Example:

```text
2π
```

### Euler's Number

```text
e
```

Example:

```text
2e
```

### Previous Answer

```text
Ans
```

Example:

```text
5 + 5
Ans * 2
```

---

# ✖️ Implicit Multiplication

The expression parser supports multiplication without explicitly entering `*`.

Examples:

```text
2(3 + 4)
```

is interpreted as:

```text
2 * (3 + 4)
```

Other examples:

```text
2π
2e
2sin(30)
3Ans
```

This makes the calculator behave more naturally like a scientific calculator.

---

# 💾 Memory Functions

The calculator supports standard calculator memory operations.

| Button | Description |
|--------|-------------|
| `M+` | Add current value to memory |
| `M-` | Subtract current value from memory |
| `MR` | Recall memory |
| `MC` | Clear memory |

Example:

```text
10
M+

5
M+

MR
```

The recalled value will be:

```text
15
```

---

# 📝 Calculation History

The calculator maintains a history of successful calculations.

Example:

```text
2 + 3        = 5
10 * 4       = 40
sin(30)      = 0.5
5 nCr 2      = 10
```

### History features

- Automatically saves successful calculations
- Displays expression and result
- Click an expression to reuse it
- Delete individual history entries
- Clear complete history

### Reuse History

Clicking:

```text
2 + 3
```

loads:

```text
2 + 3
```

back into the calculator display.

The expression can then be modified before calculating again.

---

# ⌨️ Keyboard Support

The calculator supports keyboard input.

| Keyboard Key | Action |
|--------------|--------|
| `0-9` | Numbers |
| `.` | Decimal |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Percentage |
| `^` | Power |
| `(` | Opening parenthesis |
| `)` | Closing parenthesis |
| `Enter` | Calculate |
| `=` | Calculate |
| `Backspace` | Delete |
| `Escape` | Clear |

---

# 🧹 Clear Operations

The calculator supports different types of clearing.

### C

Clears the current calculator input/result.

### AC

Performs a complete calculator reset.

It resets:

- Current expression
- Current result
- Calculation state
- Angle mode

Memory is kept separately.

---

# 🔄 Expression Processing

One of the main goals of this project is to understand how mathematical expressions are processed internally.

The project does **not simply rely on Python's `eval()`** to evaluate user expressions.

Instead, it uses a custom processing pipeline:

```text
User Expression
       ↓
   Tokenizer
       ↓
     Tokens
       ↓
     Parser
       ↓
 Calculator Engine
       ↓
Scientific Calculator
       ↓
     Result
```

---

# 🔤 Tokenizer

The tokenizer converts the input expression into meaningful tokens.

For example:

```text
2 + 3 * 4
```

is broken into tokens conceptually like:

```text
2.0
+
3.0
*
4.0
```

The tokenizer supports:

- Integers
- Floating-point numbers
- Decimal values
- Scientific notation
- Identifiers
- Mathematical constants
- Functions
- Operators
- Parentheses
- Commas
- `π`
- `e`
- `Ans`
- `//`
- `**`

---

# 🔢 Scientific Notation

Scientific notation is supported.

Examples:

```text
2e3
```

Result:

```text
2000
```

```text
2e-3
```

Result:

```text
0.002
```

```text
2e+3
```

Result:

```text
2000
```

The tokenizer also handles:

```text
2e
```

as implicit multiplication with Euler's constant:

```text
2 * e
```

---

# 🌳 Custom Parser

The parser evaluates mathematical expressions according to operator precedence.

The parser is divided into different levels.

```text
Expression
    │
    ├── Addition / Subtraction
    │
    └── Term
          │
          ├── Multiplication
          ├── Division
          ├── Floor Division
          ├── Modulo
          │
          └── Power
                │
                └── Postfix
                      │
                      ├── Factorial
                      ├── Percentage
                      │
                      └── Factor
```

This allows expressions such as:

```text
2 + 3 * 4
```

to correctly evaluate as:

```text
14
```

rather than:

```text
20
```

---

# 🔄 Operator Precedence

The parser follows mathematical precedence.

For example:

```text
2 + 3 * 4
```

First:

```text
3 * 4 = 12
```

Then:

```text
2 + 12 = 14
```

Parentheses can change the order:

```text
(2 + 3) * 4
```

Result:

```text
20
```

---

# ⚡ Right-Associative Power

Power operations are parsed from right to left.

For example:

```text
2 ^ 3 ^ 2
```

is interpreted as:

```text
2 ^ (3 ^ 2)
```

and not:

```text
(2 ^ 3) ^ 2
```

This is handled through recursive parsing of the power expression.

---

# 🔄 Postfix Operators

The parser supports postfix operators such as:

```text
!
%
```

Examples:

```text
5!
```

and:

```text
50%
```

The parser first evaluates the underlying value and then applies the postfix operation.

---

# 🐍 Backend Architecture

The backend is written in Python using Flask.

```text
backend/
├── app.py
├── calculator.py
├── scientific_calculator.py
├── tokenizer.py
├── parser.py
└── engine.py
```

---

# 📁 Backend Components

## `calculator.py`

Contains the base `Calculator` class.

The class provides basic mathematical operations and uses Python special methods / dunder methods.

Examples:

```python
__add__
__sub__
__mul__
__truediv__
__floordiv__
__mod__
__pow__
```

It also supports:

- Reverse arithmetic
- Comparisons
- Unary operations
- Numeric conversions
- Validation

---

# `scientific_calculator.py`

Contains the `ScientificCalculator` class.

It extends the base `Calculator` class using inheritance.

It adds scientific functionality such as:

```text
sqrt
sin
cos
tan
asin
acos
atan
ln
log
exp
factorial
percent
ncr
npr
sinh
cosh
tanh
asinh
acosh
atanh
```

The class also handles:

```text
DEG
RAD
GRAD
```

angle modes.

---

# `tokenizer.py`

Responsible for converting a mathematical expression into tokens.

It handles:

- Numbers
- Decimal numbers
- Scientific notation
- Identifiers
- Functions
- Constants
- Operators
- Parentheses
- Commas

---

# `parser.py`

Responsible for understanding the structure of the expression.

It handles:

- Operator precedence
- Parentheses
- Unary operators
- Functions
- Function arguments
- Power expressions
- Postfix operations
- Implicit multiplication
- Recursive expression parsing

---

# `engine.py`

The `CalculatorEngine` acts as the central backend controller.

It manages:

- Current value
- Previous answer
- Angle mode
- Memory
- Calculation history
- Expression evaluation
- Function dispatch
- Mathematical constants

Conceptually:

```text
CalculatorEngine
       │
       ├── current
       ├── ans
       ├── memory
       ├── history
       └── angle_mode
```

---

# 🌐 Flask API

The Flask backend provides REST API endpoints for the React frontend.

---

## Calculate

### Request

```http
POST /calculate
```

### JSON

```json
{
    "expression": "2 + 3 * 4",
    "angle_mode": "DEG"
}
```

### Response

```json
{
    "result": 14
}
```

---

# 📜 Get History

### Request

```http
GET /history
```

### Response

```json
[
    {
        "expression": "2 + 3",
        "result": 5
    },
    {
        "expression": "10 * 4",
        "result": 40
    }
]
```

---

# 🗑️ Clear History

### Request

```http
DELETE /history
```

### Response

```json
{
    "message": "History cleared"
}
```

---

# ❌ Delete History Item

### Request

```http
DELETE /history/<index>
```

Example:

```http
DELETE /history/0
```

### Response

```json
{
    "message": "History item deleted"
}
```

---

# 🏗️ Frontend Architecture

The frontend is built using React and Vite.

The UI is divided into reusable components.

```text
src/
└── components/
    │
    ├── Calculator/
    │   ├── Calculator.jsx
    │   └── Calculator.css
    │
    ├── Display/
    │   ├── Display.jsx
    │   └── Display.css
    │
    ├── Keypad/
    │   ├── Keypad.jsx
    │   ├── Keypad.css
    │   │
    │   ├── ControlPad/
    │   │   ├── ControlPad.jsx
    │   │   └── ControlPad.css
    │   │
    │   ├── MainPad/
    │   │   ├── MainPad.jsx
    │   │   ├── MainPad.css
    │   │   │
    │   │   ├── NumberPad/
    │   │   │   ├── NumberPad.jsx
    │   │   │   └── NumberPad.css
    │   │   │
    │   │   └── OperatorPad/
    │   │       ├── OperatorPad.jsx
    │   │       └── OperatorPad.css
    │   │
    │   └── ScientificPad/
    │       ├── ScientificPad.jsx
    │       └── ScientificPad.css
    │
    ├── Button/
    │   ├── Button.jsx
    │   └── Button.css
    │
    └── History/
        ├── History.jsx
        └── History.css
```

---

# ⚛️ React Components

## `Calculator`

The main calculator component.

Responsible for managing major application state such as:

- Expression
- Result
- Calculation state
- Angle mode
- History

It also communicates with the Flask backend.

---

## `Display`

Responsible for displaying:

- Current expression
- Current result

---

## `Keypad`

Acts as the main controller for calculator button interactions.

It coordinates:

- Number input
- Operators
- Scientific functions
- Keyboard input
- Memory operations
- Angle mode
- Calculation
- Clear operations

---

## `ControlPad`

Contains calculator control buttons such as:

- Clear
- Backspace
- Angle mode
- Other calculator controls

---

## `MainPad`

Contains the main calculator input area.

It contains:

- NumberPad
- OperatorPad

---

## `NumberPad`

Contains numeric buttons:

```text
0
1
2
3
4
5
6
7
8
9
.
```

---

## `OperatorPad`

Contains arithmetic operators:

```text
+
-
*
/
%
^
(
)
=
```

---

## `ScientificPad`

Contains scientific calculator functions.

Examples:

```text
sin
cos
tan
asin
acos
atan
ln
log
exp
sqrt
x²
x³
1/x
nCr
nPr
M+
M-
MR
MC
π
e
Ans
!
```

---

## `Button`

A reusable button component used throughout the calculator.

Instead of creating separate button logic for every key, the same component receives:

```jsx
value
onClick
```

This keeps the UI reusable and easier to maintain.

---

## `History`

Displays previous calculations.

It supports:

- Viewing history
- Reusing expressions
- Deleting individual entries
- Clearing all history

---

# 🔄 Frontend ↔ Backend Flow

When the user enters:

```text
sin(30) + 5^2
```

the frontend sends:

```text
POST /calculate
```

with:

```json
{
    "expression": "sin(30) + 5^2",
    "angle_mode": "DEG"
}
```

The backend then performs:

```text
Flask
  ↓
CalculatorEngine
  ↓
Tokenizer
  ↓
Parser
  ↓
ScientificCalculator
  ↓
Result
```

The result is returned as JSON:

```json
{
    "result": 25.5
}
```

React then displays the result.

---

# 📝 History Flow

After a successful calculation:

```text
User calculates
       ↓
Backend evaluates expression
       ↓
Result generated
       ↓
Expression + result added to history
       ↓
React requests /history
       ↓
History displayed
```

For deleting one item:

```text
Click ✕
   ↓
DELETE /history/<index>
   ↓
Backend removes item
   ↓
React fetches updated history
   ↓
UI updates
```

For clearing all history:

```text
Click Clear
     ↓
DELETE /history
     ↓
Backend clears history
     ↓
React updates state
```

---

# 🧰 Tech Stack

## Frontend

- React
- Vite
- JavaScript
- CSS
- Fetch API

## Backend

- Python
- Flask
- Flask-CORS

## Concepts Used

- Object-Oriented Programming
- Inheritance
- Encapsulation
- Method overriding
- Operator overloading
- Python dunder methods
- REST API
- JSON
- Recursive parsing
- Tokenization
- Operator precedence
- State management
- Component-based architecture
- Frontend-backend communication

---

# 🚀 Installation and Setup

## Prerequisites

Make sure the following are installed:

- Python 3
- Node.js
- npm
- Git

---

# 🐍 Backend Setup

Go to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install flask flask-cors
```

Start the Flask server:

```bash
python app.py
```

The backend will run at:

```text
http://127.0.0.1:5000
```

---

# ⚛️ Frontend Setup

Open another terminal.

Go to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Vite will provide a local URL, normally:

```text
http://localhost:5173
```

Open the URL in your browser.

---

# 📁 Complete Project Structure

```text
scientific-calculator/
│
├── backend/
│   ├── app.py
│   ├── calculator.py
│   ├── scientific_calculator.py
│   ├── tokenizer.py
│   ├── parser.py
│   └── engine.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   │
│   │   │   ├── Calculator/
│   │   │   │   ├── Calculator.jsx
│   │   │   │   └── Calculator.css
│   │   │   │
│   │   │   ├── Display/
│   │   │   │   ├── Display.jsx
│   │   │   │   └── Display.css
│   │   │   │
│   │   │   ├── Keypad/
│   │   │   │   ├── Keypad.jsx
│   │   │   │   ├── Keypad.css
│   │   │   │   │
│   │   │   │   ├── ControlPad/
│   │   │   │   │   ├── ControlPad.jsx
│   │   │   │   │   └── ControlPad.css
│   │   │   │   │
│   │   │   │   ├── MainPad/
│   │   │   │   │   ├── MainPad.jsx
│   │   │   │   │   ├── MainPad.css
│   │   │   │   │   │
│   │   │   │   │   ├── NumberPad/
│   │   │   │   │   │   ├── NumberPad.jsx
│   │   │   │   │   │   └── NumberPad.css
│   │   │   │   │   │
│   │   │   │   │   └── OperatorPad/
│   │   │   │   │       ├── OperatorPad.jsx
│   │   │   │   │       └── OperatorPad.css
│   │   │   │   │
│   │   │   │   └── ScientificPad/
│   │   │   │       ├── ScientificPad.jsx
│   │   │   │       └── ScientificPad.css
│   │   │   │
│   │   │   ├── Button/
│   │   │   │   ├── Button.jsx
│   │   │   │   └── Button.css
│   │   │   │
│   │   │   └── History/
│   │   │       ├── History.jsx
│   │   │       └── History.css
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# 🧪 Example Expressions

The calculator supports expressions such as:

```text
2 + 3
```

```text
10 * 5
```

```text
2 + 3 * 4
```

```text
(2 + 3) * 4
```

```text
2 ^ 3
```

```text
2 ^ 3 ^ 2
```

```text
2π
```

```text
2e
```

```text
sin(30)
```

```text
cos(60)
```

```text
sqrt(25)
```

```text
5!
```

```text
5 nCr 2
```

```text
5 nPr 2
```

```text
Ans + 10
```

```text
2(3 + 4)
```

```text
2sin(30)
```

---

# ⚠️ Error Handling

The backend validates invalid mathematical operations and expressions.

Examples include:

- Division by zero
- Invalid modulo operations
- Invalid power operations
- Invalid factorial values
- Invalid logarithm arguments
- Invalid inverse trigonometric inputs
- Invalid hyperbolic function inputs
- Missing parentheses
- Missing function arguments
- Too many function arguments
- Invalid operators
- Invalid mathematical expressions

Errors are returned by Flask and displayed by the React frontend.

---

# 🎯 Project Goals

The main goals of this project are:

1. Build a functional scientific calculator.
2. Understand how mathematical expression evaluation works.
3. Learn how tokenizers work.
4. Learn how parsers work.
5. Implement operator precedence.
6. Practice Python Object-Oriented Programming.
7. Understand inheritance and operator overloading.
8. Build a REST API using Flask.
9. Build a component-based frontend using React.
10. Connect React with a Python backend.
11. Implement features found in real scientific calculators.
12. Gradually improve the project into a complete calculator application.

---

# 📚 What I Learned From This Project

This project provides practical experience with several important concepts.

### Python

- Classes
- Objects
- Inheritance
- Dunder methods
- Operator overloading
- Exception handling
- Mathematical libraries
- Modular project structure

### Parsing

- Lexical analysis
- Tokenization
- Recursive parsing
- Operator precedence
- Associativity
- Unary operators
- Postfix operators
- Function parsing
- Implicit multiplication

### Flask

- REST APIs
- HTTP methods
- JSON requests
- JSON responses
- CORS
- Backend state management

### React

- Components
- Props
- State
- Event handling
- `useEffect`
- API requests
- Component composition
- Reusable UI components

### Full-Stack Development

The project demonstrates how:

```text
React Frontend
      ↕
REST API
      ↕
Flask Backend
      ↕
Custom Calculator Engine
      ↕
Parser + Tokenizer
```

can work together as a complete application.

---

# 🔮 Future Improvements

The project can be extended with:

- Persistent calculation history
- Database-backed history
- User accounts
- Multiple calculator modes
- Complex number calculations
- Matrix calculations
- Vector calculations
- Statistics mode
- Equation solving
- Numerical integration
- Numerical differentiation
- Unit conversion
- Currency conversion
- Better mobile responsiveness
- Themes
- Dark/light mode
- Calculation history search
- Export history
- Import/export calculations
- Automated backend tests
- Frontend testing
- Better error messages
- Production deployment

---

# 🛡️ Design Philosophy

The project focuses on understanding the underlying concepts rather than simply relying on existing expression-evaluation libraries.

Instead of:

```python
eval(expression)
```

the project uses:

```text
Expression
    ↓
Tokenizer
    ↓
Parser
    ↓
Calculator Engine
    ↓
Scientific Calculator
```

This makes the project useful for learning how programming languages and mathematical expression evaluators process input internally.

---

# 📌 Current Status

The project currently supports:

- Basic arithmetic
- Scientific calculations
- Trigonometry
- Inverse trigonometry
- Hyperbolic functions
- Logarithms
- Exponential functions
- Factorial
- Percentage
- nCr
- nPr
- DEG/RAD/GRAD
- π and e
- Ans
- Memory operations
- Keyboard input
- Parentheses
- Implicit multiplication
- Scientific notation
- Calculation history
- History reuse
- Individual history deletion
- Clear history
- React frontend
- Flask backend
- Custom tokenizer
- Custom parser
- REST API

---

# 👨‍💻 Author

## Vikas Kasaudhan

**B.Tech — Computer Science**

**NIT Durgapur**

---

# ⭐ Acknowledgement

This project was developed as a practical learning project to explore:

```text
Python
+
Object-Oriented Programming
+
Algorithms
+
Parsing
+
Flask
+
REST APIs
+
React
+
Full-Stack Development
```

---

## ⭐ If You Like This Project

Feel free to explore the source code, experiment with the parser and calculator engine, and extend the project with additional mathematical and scientific functionality.
