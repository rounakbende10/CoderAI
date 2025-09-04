# CoderAI 🚀

<div align="center">
  <img src="image.jpeg" alt="CoderAI Cover Image" width="800" height="400">
</div>

An AI-powered code generation system that transforms natural language prompts into complete web applications using a multi-agent architecture.

## 🌟 Features

- **Natural Language to Code**: Simply describe what you want, and CoderAI generates the complete application
- **Multi-Agent Architecture**: Specialized AI agents work together for planning, architecture, and coding
- **Full-Stack Generation**: Creates HTML, CSS, and JavaScript files with modern styling
- **Structured Output**: Uses Pydantic models for reliable, validated code generation
- **Error Handling**: Robust error handling with retry mechanisms and timeouts

## 🏗️ Architecture

CoderAI uses a three-agent system:

1. **Planner Agent** 📋
   - Analyzes user requirements
   - Creates comprehensive project plans
   - Defines tech stack and features

2. **Architect Agent** 🏛️
   - Breaks down plans into implementation tasks
   - Creates detailed file structures
   - Defines dependencies and integration points

3. **Coder Agent** 💻
   - Generates actual code files
   - Implements HTML, CSS, and JavaScript
   - Handles file I/O and project structure

## 🛠️ Tech Stack

- **Python 3.11+**
- **LangGraph** - Agent orchestration and workflow management
- **Groq** - High-performance LLM inference
- **Pydantic** - Data validation and structured outputs
- **LangChain** - LLM framework and tool integration

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- Groq API key

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd CoderAI
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Get a Groq API key**
   - Visit [Groq Console](https://console.groq.com/)
   - Sign up and create an API key
   - Add it to your `.env` file

## 🚀 Usage

### Basic Usage

Run the main application:
```bash
python main.py
```

Enter your prompt when prompted:
```
Enter your prompt: Build a colorful todo app with drag and drop functionality
```

### Advanced Usage

Run with custom recursion limit:
```bash
python main.py --recursion-limit 50
```

### Example Prompts

- "Create a simple calculator web application"
- "Build a colorful todo app in HTML, CSS, and JavaScript"
- "Generate a modern portfolio website with animations"
- "Create a weather dashboard with API integration"

## 📁 Project Structure

```
CoderAI/
├── agent/
│   ├── graph.py          # Main agent orchestration
│   ├── prompts.py        # Agent prompts and templates
│   ├── states.py         # Pydantic models for data structures
│   └── tools.py          # File I/O and utility tools
├── generated_project/    # Output directory for generated code
├── main.py              # Main application entry point
├── pyproject.toml       # Project dependencies
└── README.md           # This file
```

## 🔧 Configuration

### Model Configuration

You can modify the LLM model in `agent/graph.py`:
```python
llm = ChatGroq(model_name="deepseek-r1-distill-llama-70b")
```

Available models:
- `deepseek-r1-distill-llama-70b`
- `llama3-70b-8192`
- `openai/gpt-oss-120b`

### Project Output

Generated projects are saved to the `generated_project/` directory with the following structure:
```
generated_project/
├── index.html
├── style.css
└── script.js
```

## 🎯 Example Output

When you prompt: *"Build a colorful todo app"*

CoderAI generates:
- **HTML**: Semantic structure with accessibility features
- **CSS**: Modern styling with CSS3 features, gradients, and animations
- **JavaScript**: Interactive functionality with event handling

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   - Make sure you're running from the root directory
   - Check that all dependencies are installed

2. **API Rate Limits**
   - The system includes retry logic with exponential backoff
   - Consider using a different model if you hit limits frequently

3. **File Generation Issues**
   - Ensure the `generated_project/` directory exists
   - Check file permissions

### Debug Mode

Enable debug mode by setting environment variables:
```bash
export LANGCHAIN_DEBUG=true
export LANGCHAIN_VERBOSE=true
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration
- [Groq](https://groq.com/) for high-performance LLM inference
- [LangChain](https://github.com/langchain-ai/langchain) for the LLM framework

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the example prompts for inspiration

---

**Happy Coding! 🎉**

*Transform your ideas into reality with CoderAI*
