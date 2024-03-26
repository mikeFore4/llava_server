FROM python:3.10

WORKDIR /usr/src/app

RUN mkdir ggml_llava-v1.5-7b
RUN cd ggml_llava-v1.5-7b && \
	wget -O ggml-model-q4_k.gguf https://huggingface.co/mys/ggml_llava-v1.5-7b/resolve/main/ggml-model-q4_k.gguf?download=true && \
	wget -O mmproj-model-f16.gguf https://huggingface.co/mys/ggml_llava-v1.5-7b/resolve/main/mmproj-model-f16.gguf?download=true && \
	cd ..

RUN pip install llama-cpp-python
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY run_server.sh .

EXPOSE 8000

CMD ["bash", "./run_server.sh"]

