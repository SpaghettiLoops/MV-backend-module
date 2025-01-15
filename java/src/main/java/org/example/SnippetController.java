package org.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// This class handles HTTP requests and interacts with the service.

@RestController
@RequestMapping("/snippets")
public class SnippetController {

    private final SnippetService snippetService;

    @Autowired
    public SnippetController(SnippetService snippetService) {
        this.snippetService = snippetService;
    }

    @GetMapping
    public List<Snippet> getAllSnippets(@RequestParam(required = false) String lang) {
        if (lang != null) {
            return snippetService.getAllSnippets().stream()
                    .filter(snippet -> snippet.getLanguage().equalsIgnoreCase(lang))
                    .toList();
        }
        return snippetService.getAllSnippets();
    }

    @GetMapping("/{id}")
    public Snippet getSnippetById(@PathVariable int id) {
        return snippetService.getSnippetById(id);
    }
}


