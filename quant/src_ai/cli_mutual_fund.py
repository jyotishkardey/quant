#pip install import-ipynb
import import_ipynb
import mutual_fund_analyzer
result = mutual_fund_analyzer.csv_agent.print_response("Analyze fund_analysis.csv and give me names of 3 funds which gave greater return than NIFTY Total Market most of the times."
        "If no fund outperformed tell that top 3 funds does not exits since no fund  gave greater return than NIFTY Total Market",
 stream=True)