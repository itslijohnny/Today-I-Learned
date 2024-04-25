# How to config ollama using OLLAMA_ORIGINS windows

  
When using the [Ollama](Ollama.md) plugin for [Obsidian](Obsidian.md) on Windows, you may encounter an issue where the provided instruction to run the command `OLLAMA_ORIGINS=app://obsidian.md*; ollama serve` does not work. This is because the syntax used in the original command is specific to Unix-based systems and is not compatible with Windows.  
  
To resolve this issue, you can use the following command in Windows:  
  
```bash  
$env:OLLAMA_ORIGINS="app://obsidian.md*"; ollama serve  
```  
  
This command sets the `OLLAMA_ORIGINS` environment variable to "app://obsidian.md*" and then runs the `ollama serve` command, allowing you to use the Ollama plugin with Obsidian on Windows successfully.