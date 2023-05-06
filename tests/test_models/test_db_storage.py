#!/usr/bin/python3
"""
test to check for the validity of create method
"""
import unittest
import MySQLdb


class TestCreateStatae(unittest.TestCase):
    """
    This module tests the behavioural functionality of the create method
    """

    def setUp(self):
        connDB = MySQLdb.connect(
            user='hbnb_test',
            passwd='hbnb_test_pwd',
            host='localhost',
            db='hbnb_test_db')
        self.cursor = self.connDB.cursor()

    def test_create(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initialData = cursor.fetchone()[0]
        # executing the console command 'create'
        "create State name = 'California'"
        # counting the number of rows in the state after addition of
        # California
        self.cursor.execute("SELECT COUNT(*) FROM states")
        finalData = cursor.fetchone()[0]
        # testing the difference in the before and after execution of the code
        # to be 1
        self.assertEqual(finalData - initialData, 1)

    def tearDown(self):
        self.cursor.execute("DELETE FROM states WHERE name='California'")
        self.cursor.close()
        self.db.close()
