package com.example.sudentbctserviceb;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.example.sudentbctserviceb.model.Student;

import java.util.List;

@RestController
@RequestMapping("/api/students")
public class StudentController {

    @Autowired
    Studentservice studentservice;

    @PostMapping
    public ResponseEntity<List<Student>> saveAll(@RequestBody List<Student> students) {
        return new ResponseEntity<>(studentservice.saveAll(students), HttpStatus.CREATED);
    }

    @GetMapping
    public ResponseEntity<List<Student>> getAll() {
        return new ResponseEntity<>(studentservice.findAll(), HttpStatus.OK);
    }

    @GetMapping("/find/{id}")
    public ResponseEntity<Student> findById(@PathVariable Long id) {
        return new ResponseEntity<>(studentservice.findid(id),HttpStatus.OK);
    }
}