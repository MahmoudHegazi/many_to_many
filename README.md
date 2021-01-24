# many_to_many

#### no need to add forgien key in product cus many to many 

Order has product other Orders can has same product


```python
# if you have table not assisoted
insert_stmnt = association_table.insert().values(list_id=edit_todo.list_id,todo_id=edit_todo.id)
```
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
