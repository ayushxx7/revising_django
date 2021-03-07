# Django Shell Queries

## Enter Django Shell

```
py manage.py shell
```

### Getting list of all Contacts

```
Contact.objects.all()
```

### Getting the first/last contact

```
Contact.objects.all()[0] # using list slicing
Contact.objects.first() # inbuilt method to get first element
Contact.objects.last() # inbuilt method to get first element last element
```

### Filtering objects based on name

```
Contact.objects.filter(name="ayush")
```

### Getting the name, email and date of a contact

```
obj = Contact.objects.filter(name='ayush')
obj.name
obj.email
obj.date
```

### Changing values of an object

```
obj = Contact.objects.filter(name='ayush')
obj.email = "changed@email.com"
obj.save()
```

### Saving a new contact

```
# Method 1 - using save
contact = Contact(name='Test', email='hello@email.com', date='2020-10-10')
contact.save()

# Method 2 - using create

Contact.objects.create(name='Ayush M', email='em@ail.com', date='2020-01-01')
```

### Partial matching using startswith

```
Contact.objects.filter(name__startswith='Ayush')
```

## References

- [Django Tutorial in Hindi by @CodeWithHarry](https://www.youtube.com/watch?v=JxzZxdht-XY)
- [Django Queries](https://docs.djangoproject.com/en/3.1/topics/db/queries/)
