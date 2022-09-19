from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_num():

    #a = int(request.args.get("a"))
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)

    return f"{result}"

@app.route("/sub")
def sub_num():

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)

    return f"{result}"

@app.route("/mult")
def mult_num():
  

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)

    return f"{result}"

@app.route("/div")
def div_num():
 

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)

    return f"{result}"

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operators[oper](a, b)

    return f"{result}"

