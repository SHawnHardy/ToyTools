# @Author: Hengyu Shang(shanghengyu997@outlook.com)
# @License: MIT License
# @Version: v0.1
import argparse
import datetime
import os

import akshare as ak
import yaml

try:
    from yaml import CLoader as YamlLoader
except ImportError:
    from yaml import Loader as YamlLoader


def parse_args():
    parser = argparse.ArgumentParser(description='get stocks price')
    parser.add_argument('--date', default=None, help='date')
    return parser.parse_args()


if __name__ == '__main__':
    cfg = os.path.realpath(
        os.path.join(__file__, '../../../configs/stocks.yml')
    )
    with open(cfg, 'r', encoding='utf8') as cfg:
        cfg = yaml.load(cfg, YamlLoader)

    args = parse_args()
    if args.date is None:
        args.date = datetime.date.today()
    else:
        args.date = datetime.date.fromisoformat(args.date)

    print('=== fund ===')
    for fund in cfg['fund']:
        try:
            fund_open_fund_info_em_df = ak.fund_open_fund_info_em(
                fund=fund, indicator="单位净值走势"
            )
            print(
                fund_open_fund_info_em_df.loc[
                    fund_open_fund_info_em_df['净值日期'] == args.date,
                    '单位净值'].astype('str').values[0]
            )
        except:
            print(f'ERROR: {fund}')

    print('=== etf ===')
    for etf in cfg['etf']:
        try:
            fund_etf_hist_sina = ak.fund_etf_hist_sina(symbol=etf)
            print(
                fund_etf_hist_sina.loc[fund_etf_hist_sina['date'] == args.date,
                                       'close'].astype('str').values[0]
            )
        except:
            print(f'ERROR: {etf}')
