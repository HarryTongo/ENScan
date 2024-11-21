from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Date

# 创建一个基类 Base。所有模型类（表）都需要继承该基类，Base 会提供 SQLAlchemy 的 ORM 特性，如表的映射和声明
Base = declarative_base()


class Branch(Base):
    __tablename__ = "enscan_branch"
    branch_id = Column(Integer, primary_key=True, index=True, nullable=False)
    extra = Column(String(255))
    _from = Column("from", String(255))
    legal_person = Column(String(255))
    name = Column(String(255))
    pid = Column(String(50))
    status = Column(String(255))
    parameter = Column(String(255))


class Icp(Base):
    __tablename__ = "enscan_icp"
    icp_id = Column(Integer, primary_key=True, index=True, nullable=False)
    company_name = Column(String(255))
    domain = Column(String(255))
    extra = Column(String(255))
    _from = Column("from", String(255))
    icp = Column(String(255))
    website = Column(String(255))
    website_name = Column(String(255))
    parameter = Column(String(255))


class Invest(Base):
    __tablename__ = "enscan_invest"
    invest_id = Column(Integer, primary_key=True, index=True, nullable=False)
    extra = Column(String(255))
    _from = Column("from", String(255))
    legal_person = Column(String(20))
    name = Column(String(255))
    pid = Column(String(255))
    scale = Column(String(255))
    status = Column(String(10))
    parameter = Column(String(255))


class Partner(Base):
    __tablename__ = "enscan_partner"
    partner_id = Column(Integer, primary_key=True, index=True, nullable=False)
    extra = Column(String(255))
    _from = Column("from", String(255))
    name = Column(String(255))
    pid = Column(String(255))
    reg_cap = Column(String(255))
    scale = Column(String(255))
    parameter = Column(String(255))


class Wechat(Base):
    __tablename__ = "enscan_wechat"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    avatar = Column(String(255))
    description = Column(String(255))
    extra = Column(String(255))
    _from = Column("from", String(255))
    name = Column(String(255))
    qrcode = Column(String(255))
    wechat_id = Column(String(255))
    parameter = Column(String(255))


# 定义一个 EnterpriseInfo 类，继承自 Base
class ExterpriseInfo(Base):
    # __tablename__ 是 SQLAlchemy 的特殊属性，用于指定该 ORM 类对应的数据库表名为 enterprise_info
    __tablename__ = "enscan_enterprise_info"

    # 定义了表中的 id 列。它是 Integer 类型,primary_key=True：标记该列为主键,index=True：表示在该列上创建索引，以提高查询性能,nullable=False：表示该列不能为空
    enterprise_info_id = Column(Integer, primary_key=True, index=True, nullable=False)
    # 定义了表中的 address 列，它是字符串类型，最大长度为 255 个字符
    address = Column(String(255))
    email = Column(String(255))
    extra = Column(String(255))
    # "from"指定表中的from为_from
    _from = Column("from", String(255))
    incorporation_date = Column(String(100))
    legal_person = Column(String(50))
    name = Column(String(255))
    phone = Column(String(255))
    pid = Column(String(100))
    reg_code = Column(String(255))
    registered_capital = Column(String(100))
    scope = Column(Text)
    status = Column(String(10))
    parameter = Column(String(255))


class App(Base):
    __tablename__ = "enscan_app"

    app_id = Column(Integer, primary_key=True, index=True, nullable=False)
    bundle_id = Column(String(255))
    category = Column(String(255))
    description = Column(Text)
    extra = Column(String(255))
    _from = Column("from", String(255))
    link = Column(String(255))
    logo = Column(String(255))
    market = Column(String(255))
    name = Column(String(255))
    update_at = Column(String(255))
    version = Column(String(255))
    parameter = Column(String(255))


class Weibo(Base):
    __tablename__ = "enscan_weibo"

    weibo_id = Column(Integer, primary_key=True, index=True, nullable=False)
    avatar = Column(String(255))
    description = Column(Text)
    extra = Column(String(255))
    _from = Column("from", String(255))
    name = Column(String(255))
    profile_url = Column(String(255))
    parameter = Column(String(255))
