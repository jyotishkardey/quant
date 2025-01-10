#pip install import-ipynb
import import_ipynb
import mutual_fund_analyzer
import shutil
import os

def delete_old_memory():
    # Path to the directory you want to delete
    folder_path = 'tmp'

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Delete the folder and its contents
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' has been deleted.")
    else:
        print(f"Folder '{folder_path}' does not exist.")

#Delet old memory before training. So that it works on fresh data
delete_old_memory()

#Train Model
mutual_fund_analyzer.csv_agent.run("Analyze fund_analysis.csv and give me names of 3 funds which gave greater return than NIFTY Total Market most of the times."
        "If no fund outperformed tell that top 3 funds does not exits since no fund  gave greater return than NIFTY Total Market",
 stream=True)


mutual_fund_analyzer.csv_agent.cli_app()
