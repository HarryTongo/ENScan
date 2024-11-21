import json

import pandas as pd
import requests
from sqlalchemy.orm import Session
from models import ExterpriseInfo, Branch, Icp, Invest, Partner, Wechat, App, Weibo


def load_data_from_api(name: str, invest: str, field: str, depth: str, holds: str, supplier: str, branch: str):
    base_url = "http://127.0.0.1:31000/api/info"
    params = {"name": name, "invest": invest, "field": field, "depth": depth, "holds": holds, "supplier": supplier,
              "branch": branch}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from API: {response.status_code}, {response.text}")


def write_to_excel(data: dict, filename: str, name: str):
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        if 'enterprise_info' in data['data']:
            enterprise_info_df = pd.DataFrame(data['data']['enterprise_info'])
            enterprise_info_df['扫描集团'] = name
            enterprise_info_df.to_excel(writer, sheet_name='enterprise_info', index=False)

        if 'branch' in data['data']:
            branch_df = pd.DataFrame(data['data']['branch'])
            branch_df['扫描集团'] = name
            branch_df.to_excel(writer, sheet_name='branch', index=False)

        if 'icp' in data['data']:
            icp_df = pd.DataFrame(data['data']['icp'])
            icp_df['扫描集团'] = name
            icp_df.to_excel(writer, sheet_name='icp', index=False)

        if 'invest' in data['data']:
            invest_df = pd.DataFrame(data['data']['invest'])
            invest_df['扫描集团'] = name
            invest_df.to_excel(writer, sheet_name='invest', index=False)

        if 'partner' in data['data']:
            partner_df = pd.DataFrame(data['data']['partner'])
            partner_df['扫描集团'] = name
            partner_df.to_excel(writer, sheet_name='partner', index=False)

        if 'wechat' in data['data']:
            wechat_df = pd.DataFrame(data['data']['wechat'])
            wechat_df['扫描集团'] = name
            wechat_df.to_excel(writer, sheet_name='wechat', index=False)

        if 'app' in data['data']:
            app_df = pd.DataFrame(data['data']['app'])
            app_df['扫描集团'] = name
            app_df.to_excel(writer, sheet_name='app', index=False)

        if 'weibo' in data['data']:
            weibo_df = pd.DataFrame(data['data']['weibo'])
            weibo_df['扫描集团'] = name
            weibo_df.to_excel(writer, sheet_name='weibo', index=False)


def insert_enterprise_info(db: Session, data: dict, parameter):
    enterprise_data = data['data']['enterprise_info']

    for enterprise in enterprise_data:
        new_enterprise = ExterpriseInfo(
            address=enterprise.get('address'),
            email=enterprise.get('email'),
            extra=enterprise.get('extra'),
            _from=enterprise.get('from'),
            incorporation_date=enterprise.get('incorporation_date'),
            legal_person=enterprise.get('legal_person'),
            name=enterprise.get('name'),
            phone=enterprise.get('phone'),
            pid=enterprise.get('pid'),
            reg_code=enterprise.get('reg_code'),
            registered_capital=enterprise.get('registered_capital'),
            scope=enterprise.get('scope'),
            status=enterprise.get('status'),
            parameter=parameter
        )
        db.add(new_enterprise)
    db.commit()  # 提交事务


def insert_branch(db: Session, data: dict, parameter):
    branch_data = data['data']['branch']

    for branch in branch_data:
        new_branch = Branch(
            extra=branch.get('extra'),
            _from=branch.get('from'),
            legal_person=branch.get('legal_person'),
            name=branch.get('name'),
            pid=branch.get('pid'),
            status=branch.get('status'),
            parameter=parameter
        )
        db.add(new_branch)
    db.commit()


def insert_icp(db: Session, data: dict, parameter):
    icp_data = data['data']['icp']

    for icp in icp_data:
        new_icp = Icp(
            company_name=icp.get('company_name'),
            domain=icp.get('domain'),
            extra=icp.get('extra'),
            _from=icp.get('from'),
            icp=icp.get('icp'),
            website=icp.get('website'),
            website_name=icp.get('website_name'),
            parameter=parameter
        )
        db.add(new_icp)
    db.commit()


def insert_invest(db: Session, data: dict, parameter):
    invest_data = data['data']['invest']

    for invest in invest_data:
        new_invest = Invest(
            extra=invest.get('extra'),
            _from=invest.get('from'),
            legal_person=invest.get('legal_person'),
            name=invest.get('name'),
            pid=invest.get('pid'),
            scale=invest.get('scale'),
            status=invest.get('status'),
            parameter=parameter
        )
        db.add(new_invest)
    db.commit()


def insert_partner(db: Session, data: dict, parameter):
    partner_data = data['data']['partner']

    for partner in partner_data:
        new_partner = Partner(
            extra=partner.get('extra'),
            _from=partner.get('from'),
            name=partner.get('name'),
            pid=partner.get('pid'),
            reg_cap=partner.get('reg_cap'),
            scale=partner.get('scale'),
            parameter=parameter
        )
        db.add(new_partner)
    db.commit()


def insert_wechat(db: Session, data: dict, parameter):
    wechat_data = data['data']['wechat']

    for wechat in wechat_data:
        new_wechat = Wechat(
            avatar=wechat.get('avatar'),
            description=wechat.get('description'),
            extra=wechat.get('extra'),
            _from=wechat.get('from'),
            name=wechat.get('name'),
            qrcode=wechat.get('qrcode'),
            wechat_id=wechat.get('wechat_id'),
            parameter=parameter
        )
        db.add(new_wechat)
    db.commit()


def insert_app(db: Session, data: dict, parameter):
    app_data = data['data']['app']

    for app in app_data:
        new_app = App(
            bundle_id=app.get('bundle_id'),
            category=app.get('category'),
            description=app.get('description'),
            extra=app.get('extra'),
            _from=app.get('from'),
            link=app.get('link'),
            logo=app.get('logo'),
            market=app.get('market'),
            name=app.get('name'),
            update_at=app.get('update_at'),
            version=app.get('version'),
            parameter=parameter
        )
        db.add(new_app)
    db.commit()


def insert_weibo(db: Session, data: dict, parameter):
    weibo_data = data['data']['weibo']

    for weibo in weibo_data:
        new_weibo = Weibo(
            avatar=weibo['avatar'],
            description=weibo['description'],
            extra=weibo['extra'],
            _from=weibo['from'],
            name=weibo['name'],
            profile_url=weibo['profile_url'],
            parameter=parameter
        )
        db.add(new_weibo)
    db.commit()
