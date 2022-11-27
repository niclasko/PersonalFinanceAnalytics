## Personal Finance Analytics

<b>NOTE:</b> This solution requires Power BI. Download from https://powerbi.microsoft.com/en-us/downloads/. Also, this solution is based on transaction data from the Norwegian bank Storebrand so assumes you are a bank customer with them.

1. Run ./setup.bat
2. Download transactions as Excel files from your accounts at https://nettbank.storebrand.no/. Save to ./artefacts/data
    ![Export data](./artefacts/screenshots/export_data.png)
3. cd ./scripts
4. python ./prepare_data.py
5. Open the Power BI template file ./powerbi/expenses.pbit
6. Enter absolute path to ./artefacts/exports when prompted.
7. Finally you should see your dashboard:
    ![Dashboard](./artefacts/screenshots/dashboard.png)