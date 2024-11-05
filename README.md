# st2scl

## Car rental service

https://github.com/charroux/st2scl/tree/main/rentalService

```
curl --header "Content-Type: application/json" --request GET http://localhost:8080/cars
```

```
curl --header "Content-Type: application/json" --request PUT --data '{"begin":"4/11/2024","end":"20/11/2024"}' 'http://localhost:8080/cars/11AA22?rent=true'
```

### Coding rules

Exception HTTP Handler: https://github.com/charroux/st2scl/blob/main/rentalService/src/main/java/com/example/rentalService/web/CarNotFoundException.java

Logger: https://github.com/charroux/st2scl/blob/main/rentalService/src/main/java/com/example/rentalService/web/RentalWebService.java


