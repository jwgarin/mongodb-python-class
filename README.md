# mongodb-python-class
##Class
###Attributes
`connection_string`

auth string to connect to db

###Methods
`file_exist → bool`

checks a file if it exist in collection

`get_file → dict`

get a file record

`insert_file → bool`

check if file exists

if not exist

insert then check a file record to the collection

else

update the file record

returns False if not inserted

`delete_file → bool`

deletes and check a file if deleted in the collection

returns False if not deleted