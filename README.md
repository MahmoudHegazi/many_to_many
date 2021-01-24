# many_to_many


# example use in terminal

```
>>> db.create_all()
>>> order = Order(status='ready')
>>> db.session.add(order)
>>> db.session.commit()
>>> order = Order(status='ready')
>>> product = Product(name='great widget')
>>> order.products = [product]
>>> product.orders = [order]
>>> db.session.add(order)
>>> db.session.commit()



```
