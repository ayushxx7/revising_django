# Django Shell Queries

## Enter Django Shell

```
py manage.py shell
```

### Getting list of all Contacts

```
Contact.objects.all()
```

### Getting the first contact

```
Contact.objects.all()[0]
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
contact = Contact(name='Test', email='hello@email.com', date='2020-10-10')
contact.save()
```
