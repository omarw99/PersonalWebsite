from flask import Flask, flash, jsonify, render_template, request, redirect, session, url_for
import webbrowser
from deploymentmodel import *

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/project")
def project():
	return render_template("project.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route('/project_result', methods=["GET"])
def project_result():
    name = request.args.get("stockName")
    ticker = request.args.get("ticker")

    prevRevenue = float(request.args.get("prevRevenue"))
    currRevenue = float(request.args.get("currRevenue"))
    cogs = float(request.args.get("cogs"))
    ebitda = float(request.args.get("ebitda"))
    ebit = float(request.args.get("ebit"))
    interestExpense = float(request.args.get("interestExpense"))
    netIncome = float(request.args.get("netIncome"))

    cash = float(request.args.get("cash"))
    accountsReceivable = float(request.args.get("accountsReceivable"))
    inventory = float(request.args.get("inventory"))
    currAssets = float(request.args.get("currAssets"))
    totalAssets = float(request.args.get("totalAssets"))
    accountsPayable = float(request.args.get("accountsPayable"))
    currLiabilities = float(request.args.get("currLiabilities"))
    totalLiabilities = float(request.args.get("totalLiabilities"))
    preferredDividends = float(request.args.get("preferredDividends"))
    totalEquity = float(request.args.get("totalEquity"))

    capex = float(request.args.get("capex"))

    outstandingShares = float(request.args.get("outstandingShares"))
    dividendPerShare = float(request.args.get("dividendPerShare"))
    currPrice = float(request.args.get("currPrice"))
    sector = request.args.get("sector")

    listOfVars = [prevRevenue, currRevenue, cogs, ebitda, ebit, interestExpense, netIncome, cash, accountsReceivable, 
    inventory, currAssets, totalAssets, accountsPayable, currLiabilities, totalLiabilities, preferredDividends, totalEquity,
    capex, outstandingShares, dividendPerShare, currPrice, sector]

    result = run_model(listOfVars)

    return render_template("projectResponse.html", name=name, result=result)
    
if __name__ == "__main__":
    app.run(debug=True)