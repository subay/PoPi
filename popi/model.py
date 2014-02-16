from popi import app
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(app.config['DATABASE_URI'])
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db_if_needed():
    Base.metadata.create_all(bind=engine, checkfirst=True)


class Device(Base):
    __tablename__ = 'device_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    home_code = Column(String(5), default=None)
    device_code = Column(String(5), default=None)
    device_status = Column(Integer, default=None)

    def __init__(self, name, home_code, device_code, device_status):
        self.name = name
        self.home_code = home_code
        self.device_code = device_code
        self.device_status = device_status


if __name__ == '__main__':
    init_db_if_needed()
    #d = Device('name1', '111111', '112221', 'off')
    #db_session.add(d)
    #db_session.commit()
    #x = Device.query.filter_by(name='name1').first()
    #print x.name
    #db_session.delete(x)
    #db_session.commit()
    #for device in db_session.query(Device):
    #    print device.name

