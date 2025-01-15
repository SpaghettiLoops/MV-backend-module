package org.example;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;

import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

//This class handles loading and manipulating data from data.json CRUD operations.

@Service
public class SnippetService {

    private final List<Snippet> snippets = new ArrayList<>();

    public SnippetService() {
        loadSnippets();
    }

    private void loadSnippets() {
        try {
            InputStream inputStream = getClass().getClassLoader().getResourceAsStream("data.json");
            if (inputStream == null) {
                throw new FileNotFoundException("data.json not found in resources");
            }

            ObjectMapper objectMapper = new ObjectMapper();
            List<Snippet> loadedSnippets = objectMapper.readValue(inputStream, new TypeReference<List<Snippet>>() {});
            snippets.addAll(loadedSnippets);
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("Failed to load snippets from data.json", e);
        }
    }

    public List<Snippet> getAllSnippets() {
        return snippets;
    }

    public Snippet getSnippetById(int id) {
        return snippets.stream()
                .filter(snippet -> snippet.getId() == id)
                .findFirst()
                .orElse(null);
    }
}