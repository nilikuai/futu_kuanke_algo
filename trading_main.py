#  Copyright (c)  billpwchan - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#   Proprietary and confidential
#   Written by Bill Chan <billpwchan@hotmail.com>, 2020

import glob

import trading_engine


def daily_update_data(futu_trade):
    # Daily Update HSI Constituents & Customized Stocks
    file_list = glob.glob(f"./data/HSI.Constituents/HSI_constituents_*.json")
    hsi_constituents = trading_engine.get_hsi_constituents(file_list[0])
    file_list = glob.glob(f"./data/Customized/Customized_Stocks_*.json")
    customized_stocks = trading_engine.get_customized_stocks(file_list[0])
    for stock_code in hsi_constituents:
        futu_trade.update_1D_data(stock_code)
        futu_trade.update_1M_data(stock_code)
    for stock_code in customized_stocks:
        futu_trade.update_1D_data(stock_code)
        futu_trade.update_1M_data(stock_code)


def daily_update_stocks():
    trading_engine.update_hsi_constituents()
    trading_engine.update_customized_stocks()


def main():
    # Initialization Connection
    futu_trade = trading_engine.FutuTrade()
    try:
        # daily_update_data(futu_trade=futu_trade)
        futu_trade.stock_price_subscription(['HK.00001', 'HK.00003'])

        print("Hello")



    finally:
        ret, data = futu_trade.quote_ctx.query_subscription()
        trading_engine.display_result(ret, data)
        ret, data = futu_trade.quote_ctx.get_history_kl_quota(get_detail=True)  # 设置True代表需要返回详细的拉取历史K 线的记录
        trading_engine.display_result(ret, data)
        # futu_trade.quote_ctx.close()


if __name__ == '__main__':
    main()
