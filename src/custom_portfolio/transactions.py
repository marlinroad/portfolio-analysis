#%%
import pandas as pd

from common.constants import get_portfolio_config
from report.report import display_header, display_report


def build_transaction_table(df_transactions):
	transaction_table = df_transactions.assign(
		date=pd.to_datetime(df_transactions["date"]),
		price=-df_transactions["cashflow"] / df_transactions["shares"],
	)
	return (
		transaction_table.rename(
			columns={
				"date": "Date",
				"symbol": "Ticker",
				"shares": "Shares bought",
				"price": "Unit price",
			}
		)[["Date", "Ticker", "Shares bought", "Unit price"]]
		.sort_values("Date", kind="stable")
		.reset_index(drop=True)
	)

def style_transaction_table(transaction_table):
	return (
		transaction_table.style
		.format(
			{
				"Date": "{:%Y-%m-%d}",
				"Shares bought": "{:,.0f}",
				"Unit price": "${:,.2f}",
			}
		)
		.hide(axis="index")
	)

def display_portfolio_transactions():
	transaction_table = build_transaction_table(get_portfolio_config())
	display_header("Portfolio transactions")
	display_report(style_transaction_table(transaction_table))