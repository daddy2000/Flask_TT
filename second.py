from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///new', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'),primary_key=True,autoincrement=True)
    name = Column(String(50))

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# session.add_all([User(name=username) for username in ('小明','王磊','李磊')])
# session.commit()

def get_result(rs):
    print('-'*20)
    for user in rs:
        print(user.name)

rs = session.query(User).all()
get_result(rs)
rs = session.query(User).filter(User.id.in_([2,]))
get_result(rs)
rs = session.query(User).filter(and_(User.id>2,User.id<4))
get_result(rs)