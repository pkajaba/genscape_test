#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='my_repository', url='postgresql+psycopg2://testusr:password@127.0.0.1:5432/testdb', debug='False')
