# Llava server

##About
This repo contains a minimal setup to run the multimodal llava 1.5 model locally on CPU in a docker container. Of note, the server is setup to match the API of OpenAI models. Thus, if you have code that interacts with GPT-V, but you want to replace it with llava - ALL YOU HAVE TO DO is change the "endpoint" and "key" in your openai calls. Use the "test_llava.py" file as a reference.

###Getting Started
Begin by building the docker image:

```bash
docker build -t llama_server:latest .
```

Start a container, making sure to map port 8000 (I eventually plan to make the port configurable, but for now, it's not):

```bash
docker run -p 8000:8000 llama_server:latest
```

To test/verify whether the server is running properly, run (outside of the docker container):

```bash
python test_llava.py -i <path/to/image> -t <text_prompt>
```


###Notes
This llava 1.5 server runs on CPU only! It is possible to run on GPU with some minor modifications that I haven't worked through yet

This uses a specific quantized version of llava 1.5 that should have an okay tradeoff between speed and quality. To change the llava version used, adjust the wget command in the Dockerfile and the filename in run_server.sh. Refer to this [repo](https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main) to download different weights.


