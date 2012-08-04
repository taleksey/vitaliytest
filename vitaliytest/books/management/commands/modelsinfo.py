from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

class Command(BaseCommand):
    args = 'authors or books'
    help = 'Show list of book or authors'

    def handle(self, *args, **options):
        from books.models import Author,Book
        lines =[]
        first_argument = ''

        try:
            first_argument = args[0]
        except IndexError:
            raise CommandError('Your must select type one of key: authors|books')

        if args[0] == 'authors':
            author_all = Author.objects.all()
            for author in author_all:
                lines.append("Author name %s" % author.FIO)
        elif args[0] == 'books':
            book_all = Book.objects.all()
            for book in book_all:
                lines.append("Book name %s" % book.title)
        else:
            raise CommandError('Your are kay is not correct key must be only authors|books')

        return "\n".join( lines )

