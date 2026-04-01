package com.example.sudentbctserviceb;

//public class StudentRepository {
//}


import org.springframework.data.jpa.repository.JpaRepository;
import com.example.sudentbctserviceb.model.Student;
//import com.example.sudentbctserviceb.model.Student;

public interface StudentRepository extends JpaRepository<Student, Long> {

}