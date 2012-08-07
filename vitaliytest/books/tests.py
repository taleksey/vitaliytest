"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from books.models import Author,Book

class SimpleTest(TestCase):
    def test_basic_login(self):
        """
        Tests that user login
        """
        c = Client()
        c.login(username='a', password='123456')

    def test_basic_author(self):
        """
        Test add author
        """
        create_author = Author(FIO="Ernest Miller Hemingway", birthday = "1899-07-21")
        create_author.save()

    def test_basic_book(self):
        """
        Test add book and author for this book
        """
        ernest_author = Author.objects.create(FIO="Ernest Miller Hemingway", birthday = "1899-07-21")
        create_book = Book.objects.create(title="The Old Man And The Sea", yearbook="2012-07-07", short_describe="The Old Man and the Sea is the story of an epic battle between an old, experienced fisherman and a large marlin.")
        create_book.author.add(ernest_author)

        create_book = Book.objects.create(title=" A Farewell to Arms", yearbook="2012-01-31", short_describe="A Farewell to Arms focuses on a romance between Henry and a British nurse, Catherine Barkley, against the backdrop of World War I, cynical soldiers, fighting and the displacement of populations.")
        create_book.author.add(ernest_author)

        create_book = Book.objects.create(title="Islands in the Stream", yearbook="2012-02-25", short_describe="The first act, \"Bimini\", begins with an introduction to the character of Thomas Hudson, a classic Hemingway stoic male figure. Hudson is a renowned American painter who finds tranquility on the island of Bimini, in the Bahamas, a far cry from his usual adventurous lifestyle. Hudson's strict routine of work is interrupted when his three sons arrive for the summer and is the setting for most of the act.")
        create_book.author.add(ernest_author)
