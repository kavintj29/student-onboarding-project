package com.example.sudentbctserviceb;

import com.example.sudentbctserviceb.model.Student;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class Studentservice {
    @Autowired
    StudentRepository studentRepository;

    //curd opration
    //save
    public Student save(Student student) {
        return studentRepository.save(student);

    }
    //saveall
    public List<Student> saveAll(List<Student> students) {
        return studentRepository.saveAll(students);
    }
    //findall

    public List<Student> findAll() {
        return studentRepository.findAll();
    }
    //findbyid
    public Student findid(Long id) {


        return studentRepository.findById(id).orElseThrow(() ->new RuntimeException(("id not foun")));
    }
}
