# Create Custom Models From Huggingface with Ollama

---  
page-title: Ollama + HuggingFace ✅🔥. Create Custom Models From Huggingface… | by Sudarshan Koirala | Feb, 2024 | Medium  
url: https://medium.com/@sudarshan-koirala/ollama-huggingface-8e8bc55ce572  
date: 2024-03-26 23:46:25  
---  
### A step-by-step guide to creating custom models from Huggingface using Ollama  
  
Ollama is an open-source tool that helps you get up and running with large language models, locally in very easy and simple steps. It's a great companion to Huggingface, which offers more than half a million models. In this post, we will learn how to create custom models from Huggingface using Ollama.  
  
Steps to create custom models:  
  
1. Make sure you have Ollama installed and running (no walking 😄).  
2. Go to the Huggingface website and download the model (e.g., GGUF model).  
3. Create a modelfile and input necessary things, such as the model's name and stop tokens.  
4. Create a model out of this modelfile and run it locally in the terminal using the `ollama create` and `ollama run` commands.  
  
Example: In this example, we are using the [TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF](https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF) model:  
  
```  
FROM "./capybarahermes-2.5-mistral-7b.Q4_K_M.gguf"  
PARAMETER stop "<|im_start|>"    
PARAMETER stop "<|im_end|>"  
  
TEMPLATE """    
<|im_start|>system    
{{ .System }}<|im_end|>    
<|im_start|>user    
{{ .Prompt }}<|im_end|>    
<|im_start|>assistant    
"""  
```  
  
To create and run the custom model, use the following commands:  
  
```bash  
ollama create my-own-model -f Modelfile  
ollama run my-own-model  
```  
  
Conclusion: By following these steps, you can create custom models from Huggingface using Ollama. This allows you to leverage the power of both platforms and tailor your language models to specific use cases or requirements.