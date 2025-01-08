const express = require('express');
const app = express();

const data = [
    {
      "id": 1,
      "language": "Python",
      "code": "print('Hello, World!')"
    },
    {
      "id": 2,
      "language": "Python",
      "code": "def add(a, b):\n    return a + b"
    },
    {
      "id": 3,
      "language": "Python",
      "code": "class Circle:\n    def __init__(self, radius):\n        self.radius = radius\n\n    def area(self):\n        return 3.14 * self.radius ** 2"
    },
    {
      "id": 4,
      "language": "JavaScript",
      "code": "console.log('Hello, World!');"
    },
    {
      "id": 5,
      "language": "JavaScript",
      "code": "function multiply(a, b) {\n    return a * b;\n}"
    },
    {
      "id": 6,
      "language": "JavaScript",
      "code": "const square = num => num * num;"
    },
    {
      "id": 7,
      "language": "Java",
      "code": "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"
    },
    {
      "id": 8,
      "language": "Java",
      "code": "public class Rectangle {\n    private int width;\n    private int height;\n\n    public Rectangle(int width, int height) {\n        this.width = width;\n        this.height = height;\n    }\n\n    public int getArea() {\n        return width * height;\n    }\n}"
    }
  ]

app.post('/snippets', (req, res) => {
  const newSnippet = req.body;
    data.push(newSnippet);
})

app.get('/snippets', (req, res) => {
    res.json(data);
})

app.get('/snippets/:id', (req, res) => { 
    const id = req.params.id;
    const snippet = data.find(snippet => snippet.id == id);
    res.json(snippet);
})

app.get('snippets/:language', (req, res) => { 
    const language = req.params.language;
    const snippets = data.find(snippet => snippet.language == language);
    res.json(snippets);
})


app.listen(3000, () => {
  console.log('Server is running on port 3000');
})

