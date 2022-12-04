#!/usr/bin/python3
""" Delete state objects using sqlalchemy """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker, Session
    from model_state import Base, State

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    s = Session()

    s.query(State).fislter(State.name.like('%a%')).\
        delete(synchronize_session=False)

    s.commit()
