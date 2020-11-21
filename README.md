# Product_NCR_API
An API for managing Customer Product Non-conformances and completion of root cause of product issues. 

## Usage:
  - List of customer related product issues ```GET /product_ncr```
  - Post customer product issue - ```POST /product_ncr/``` 
  - Lookup issue - ```GET /product_ncr/<id> ```
  - Update issue with investigation report (root cause)
  - Delete customer issue - ``` DELETE /product_ncr/<id>```

##  Implementation:
Django Restful API CRUD Operations with PostgreSQL database using HTTP Methods such as GET, POST, PUT and DELETE

###  Get the Code:
```
$ git clone https://github.com/MrEcho92/Product_NCR_API.git

```
