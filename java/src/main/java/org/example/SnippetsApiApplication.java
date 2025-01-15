package org.example;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

// main class equivalent to app.js in javascript version

@SpringBootApplication
public class SnippetsApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(SnippetsApiApplication.class, args);
    }
}
