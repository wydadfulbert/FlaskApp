package com.example.rentalService.web;

import com.example.rentalService.data.Car;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class RentalWebService {

    List<Car> cars = new ArrayList<Car>();

    public RentalWebService() {
        Car car = new Car("11AA22", 1000);
        cars.add(car);
        car = new Car("22BB33", 3000);
        cars.add(car);
    }

    @GetMapping("/cars")
    public List<Car> getCars(){
        return cars;
    }

}
