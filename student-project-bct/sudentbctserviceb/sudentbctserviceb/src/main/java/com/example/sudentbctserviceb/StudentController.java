package com.example.sudentbctserviceb;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.sudentbctserviceb.model.Student;
//import com.example.sudentbctserviceb.model.Student;
@RestController
@RequestMapping("/api/students")
public class StudentController {

    @Autowired
    private com.example.sudentbctserviceb.StudentRepository repo;

    @PostMapping
    public Student saveStudent(@RequestBody Student student) {
        return repo.save(student);
    }
}