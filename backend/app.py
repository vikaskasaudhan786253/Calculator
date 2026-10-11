from flask import Flask, request, jsonify
from flask_cors import CORS

from engine import CalculatorEngine

app = Flask(__name__)
CORS(app)

engine = CalculatorEngine()

@app.route("/calculate", methods = ["POST"])
def calculate():
    data = request.get_json()

    expression = data.get("expression")
    angle_mode = data.get("angle_mode", "DEG")

    if not expression:
        return jsonify({
            "error": "Expression is required"
        }), 400
    try:
        result = engine.evaluate(expression, angle_mode)

        return jsonify({
            "result": result.num
        })
    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 400


@app.route("/memory", methods=["POST"])
def memory():
    data = request.get_json()

    operation = data.get("operation")
    value = data.get("value")

    try:
        if operation == "M+":
            engine.memory_add()

        elif operation == "M-":
            engine.memory_subtract()

        elif operation == "MR":
            return jsonify({
                "result": engine.memory_recall().num
            })

        elif operation == "MC":
            engine.memory_clear()

        else:
            return jsonify({
                "error": "Invalid memory operation"
            }), 400

        return jsonify({
            "result": engine.memory.num
        })

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 400



@app.route("/history", methods=["GET"])
def get_history():
    return jsonify(engine.history)


@app.route("/history", methods=["DELETE"])
def clear_history():
    engine.clear_history()
    return jsonify({"message": "History cleared"})


@app.route("/history/<int:index>", methods=["DELETE"])
def delete_history(index):
    try:
        engine.delete_history(index)
        return jsonify({"message": "History item deleted"})
    except IndexError as error:
        return jsonify({"error": str(error)}), 400

if __name__ == "__main__":
    app.run(debug = True)
