import argparse
import json

from db import engine, get_db
from models import Base
from sqlalchemy.orm import Session
from data_loader import load_data_from_api, write_to_excel


# 初始化数据库，创建表
def init_db():
    Base.metadata.create_all(bind=engine)


# def main():
#     # 设置命令行参数
#     parser = argparse.ArgumentParser(description="从 APi 获取数据并存储到数据库中")
#     parser.add_argument('--name', required=True, help='企业名称+&字段')
#     args = parser.parse_args()
#
#     # 初始化数据库
#     init_db()
#
#     # 加载 JSON 数据
#     data = load_data_from_api(args.name)
#     # 加载数据库会话
#     db: Session = next(get_db())
#
#     # 插入数据
#     try:
#         try:
#             insert_branch(db, data, args.name)
#         except Exception as e:
#             print(f"Error inserting branch data: {e}")
#             db.rollback()
#
#         try:
#             insert_enterprise_info(db, data, args.name)
#         except Exception as e:
#             print(f"Error inserting enterprise info data: {e}")
#             db.rollback()
#
#         try:
#             insert_icp(db, data, args.name)
#         except Exception as e:
#             print(f"Error inserting ICP data: {e}")
#             db.rollback()
#
#         try:
#             insert_invest(db, data, args.name)
#         except Exception as e:
#             print(f"Error inserting invest data: {e}")
#             db.rollback()
#
#         try:
#             insert_partner(db, data, args.name)
#         except Exception as e:
#             print(f"Error inserting partner data: {e}")
#             db.rollback()
#
#         try:
#             insert_wechat(db, data, args.name)
#         except Exception as e:
#             print(f"Error inserting wechat data: {e}")
#             db.rollback()
#
#         try:
#             insert_app(db, data, args.name)
#         except Exception as e:
#             print(f"Error inserting app data: {e}")
#             db.rollback()
#
#         try:
#             insert_weibo(db, data, args.name)
#         except Exception as e:
#             print(f"Error inserting weibo data: {e}")
#
#         print("数据加载完成.")
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#     finally:
#         db.close()

def main():
    # depth 递归搜索n层公司，第一层按照爱企查股权穿透图的一层。 holds:是否控股  invest:投资比例 field: 需要获取的字段信息
    # --name xxx  --depth x  --holds true  --invest 50  --field enterprise_info,icp,partner,wechat,weibo
    parser = argparse.ArgumentParser(description="从 APi 获取数据并存储到 Excel表格中")
    # --name 为必填参数
    parser.add_argument('--name', required=True, help='企业名称')
    parser.add_argument('--invest', required=False, help='投资比列')
    parser.add_argument('--field', required=False,
                        help='填写需要获取的字段信息，如: enterprise_info,branch,icp,invest,partner,wechat,app,weibo')
    parser.add_argument('--depth', required=False, help='递归搜索n层公司，如:1 or 2 or 3')
    parser.add_argument('--holds', required=False, help='控股公司百分比')
    parser.add_argument('--supplier', required=False, help='查询供应商信息')
    parser.add_argument('--branch', required=False, help='查询分支机构信息, 如: true')
    args = parser.parse_args()

    # 加载 JSON数据
    data = load_data_from_api(args.name, args.invest, args.field, args.depth, args.holds, args.supplier, args.branch)

    # 将数据写入Excl
    excel_filename = f"result/{args.name}.xlsx"
    write_to_excel(data, excel_filename, args.name)

    print("数据加载完成，已输出到 Excel.")


if __name__ == '__main__':
    main()
