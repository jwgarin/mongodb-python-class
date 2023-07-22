# mongodb-python-class
## Class
### Attributes
`connection_string`

auth string to connect to db

### Methods
`get → dict`

returns empty if not exists and returns the data if exists

`insert → None`

insert then check a file record to the collection

`delete → bool`

deletes and check a file if deleted in the collection

returns False if not deleted

`update → None`
updates the file in collection