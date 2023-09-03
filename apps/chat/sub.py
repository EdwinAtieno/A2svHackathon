import subprocess
import shlex


def run_llama_model(input_text):
    llama_cpp_path = '../llama2/llama.cpp/'

    command = f"{llama_cpp_path} -m ./models/7B/ggml-model-q4_0.bin -n 1024 --repeat_penalty 1.0 --color -i -r 'User:' -f -"

    with subprocess.Popen(
        shlex.split(command),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ) as process:
        process.stdin.write(input_text + "\n")
        process.stdin.flush()

        response = process.stdout.readline().strip()

    return response
