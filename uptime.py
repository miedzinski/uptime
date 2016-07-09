#!/usr/bin/env python3
import argparse
import datetime
import os.path
import sqlite3


def save(connection):
    query = '''
    REPLACE INTO
        uptime (day, time)
    VALUES (
        date('now'),
        coalesce((SELECT time FROM uptime WHERE day=date('now')), 0) + ?
    )
    '''

    with connection:
        connection.execute(query, (get_uptime(), ))


def show(connection, start, end, hours):
    query = '''
    SELECT
      day,
      time
    FROM
      uptime
    WHERE
      day BETWEEN coalesce(?, 0) AND coalesce(?, 9999)
    ORDER BY
      day
    '''

    rows = connection.execute(query, (start, end))
    uptimes = [
        (day, datetime.timedelta(seconds=uptime))
        for day, uptime in rows
    ]

    table = '\n'.join('%s\t%s' % row for row in uptimes)
    total = sum((row[1] for row in uptimes), datetime.timedelta(0))
    expected = datetime.timedelta(hours=len(uptimes) * hours)

    print(table, end='\n\n')
    print('total %s, expected %s' % (total, expected))


def setup(connection):
    query = '''
    CREATE TABLE IF NOT EXISTS
      uptime (
        day TEXT NOT NULL PRIMARY KEY,
        time INTEGER NOT NULL DEFAULT 0
    )
    '''

    with connection:
        connection.execute(query)


def parse_date(string):
    try:
        return datetime.datetime.strptime(string, '%Y-%m-%d').date()
    except TypeError:
        return None


def get_uptime():
    with open('/proc/uptime') as f:
        return int(float(f.readline().split()[0]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=('show', 'save', 'setup'))
    parser.add_argument('-d', '--database', default='~/.uptime.db')
    parser.add_argument('-s', '--start', type=parse_date, metavar='YYYY-MM-DD')
    parser.add_argument('-e', '--end', type=parse_date, metavar='YYYY-MM-DD')
    parser.add_argument('--hours', default=8)

    args = parser.parse_args()

    db_path = os.path.expanduser(args.database)
    connection = sqlite3.connect(db_path)

    if args.action == 'show':
        show(connection, args.start, args.end, args.hours)
    elif args.action == 'save':
        save(connection)
    elif args.action == 'setup':
        setup(connection)


if __name__ == '__main__':
    main()
