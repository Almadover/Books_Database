import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_table, Publisher, Book, Sale, Shop, Stock

DSN = 'postgresql://postgres:touching@localhost:5432/books'
engine = sq.create_engine(DSN)
Session = sessionmaker(bind = engine)
session = Session()

create_table(engine)

pub1 = Publisher(name = "Пушкин", book = [Book(title = "Дубровский"),
                                          Book(title = "Капитанская дочка"),
                                          Book(title = "Сказка о царе Салтане"),
                                          Book(title = "Зимнее утро")])
pub2 = Publisher(name = "Лермонтов", book = [Book(title = "Мцыри"),
                                             Book(title = "Герой нашего времени"),
                                             Book(title = "Смерть поэта"),
                                             Book(title = "Демон")])
pub3 = Publisher(name = "Гоголь", book = [Book(title = "Тарас Бульба"),
                                          Book(title = "Ночь перед Рождеством"),
                                          Book(title = "Шинель")])
b1 = Book(title = "Руслан и Людмила", publisher = pub1)
b2 = Book(title = "Дума", publisher = pub2)
b3 = Book(title = "Портрет", publisher = pub3)

shop1 = Shop(name = "Лабиринт")
shop2 = Shop(name = "Читай город")

stock1 = Stock(book = b1, shop = shop1, count = 40)
stock2 = Stock(book = b2, shop = shop1, count = 50)
stock3 = Stock(book = b3, shop = shop2, count = 60)
stock4 = Stock(book = b2, shop = shop2, count = 70)

sale1 = Sale(price = 500, stock = stock1, data_sale = '11-12-2021', count = 20)
sale2 = Sale(price = 380, stock = stock2, data_sale = '25-08-2022', count = 30)
sale3 = Sale(price = 550, stock = stock3, data_sale = '01-04-2021', count = 40)
sale4 = Sale(price = 660, stock = stock4, data_sale = '14-02-2021', count = 50)





session.add_all([pub1, pub2, pub3, shop1, shop2, b1, b2, b3, stock1, stock2, 
                 stock3, stock4, sale1, sale2, sale3, sale4])
session.commit()

x = input('Введите значение: ')

q = session.query(Book.title, Shop.name, Sale.price, Sale.data_sale).join(Publisher).join(Stock).join(Shop).join(Sale)

if x.isdigit():
    q = q.filter(Publisher.id == x).all()
else:
    q = q.filter(Publisher.name == x).all()

for title, name, price, data_sale in q:
    print(f'{title} | {name} | {price} | {data_sale}')

# Не пойму, почему выводяться не все книги каждого автора?

session.close()