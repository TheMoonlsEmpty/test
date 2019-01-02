# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String, Integer
# from sqlalchemy .orm import sessionmaker
# engine = create_engine('mysql+pymysql://root:123456@192.168.0.16:3306/Y1803', echo=True)  # 创建数据库及引擎
# Base = declarative_base()    # 创建基类
#
#
# class Test(Base):
#     __tablename__ = 'zpp'     # 表名
#     id = Column(Integer, primary_key=True)       # Column 代表表中的每一列
#     name = Column(String(64))
#     age = Column(Integer)                 # 定义表格式
#
# Base.metadata.create_all(engine)    # 创建表
#
# Session = sessionmaker(bind=engine)  # 绑定
# session = Session()              # 创建会话
#
#
# # a = session.query(Test).get(1)     # 查
#
# session.add(Test(id=2, name='pp', age=12))  # 增       Test是引用上面class类
#
# # a = session.query(Test).get(1)
# # a.name = 'zpp'  # 改
#
# # a = session.query(Test).get(1)
#
# # session.delete(a)    # 删
#
# session.commit()      # 提交


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer

engine = create_engine('mysql+pymysql://root:123456@192.168.0.16:3306/test', echo=True)


Base = declarative_base()





class Student(Base):    # 必须继承declaraive_base得到的那个基类

    __tablename__ = 'Students'    # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    Sno = Column(String(10), primary_key=True)    # Column类创建一个字段
    Sname = Column(String(20), nullable=False, unique=True, index=True)    # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    Ssex = Column(String(2), nullable=False)
    Sage = Column(Integer, nullable=False)
    Sdept = Column(String(20))

    def __repr__(self):
        return "<Student>{}:{}".format(self.Sname, self.Sno)



Base.metadata.create_all(engine)    #这就是为什么表类一定要继承Base，因为Base会通过一些方法来通过引擎初始化数据库结构。不继承Base自然就没有办法和数据库发生联系了。

Session = sessionmaker(bind=engine)

session = Session()    #实例化了一个会话（或叫事务），之后的所有操作都是基于这个对象的

# student = Student(Sno='10001',Sname='Frnak',Ssex='M',Sage=22,Sdept='SFS')

session.add(Student(Sno='10003', Sname='Frnak', Ssex='M', Sage=22, Sdept='SFS'))
# session.add(student)

session.commit()    #不要忘了commit

# session.close()