#!python
import subprocess
import re
import sys
import os
import glob
from datetime import datetime
from transformers import GPT2Tokenizer

max_tokens=3000
prompt_text_size=500

def count_tokens(text):
    # Initialize the GPT-2 tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Tokenize the input text
    tokens = tokenizer.tokenize(text)
    return len(tokens)


def split_into_chunks(filename, prompt_size, chunk_size=max_tokens):
    with open(filename, 'r') as file:
        text = file.read()
        while(len(text)>0):
            rest=""
            tok_count=max_tokens+1
            max_size = max_tokens-prompt_size-prompt_text_size
            while (tok_count>max_size):
                tok_count=count_tokens(text)
                trim=((tok_count-max_size)*2)
                if (trim>0):
                    rest=text[-trim:]+rest
                    text=text[:-trim]
                tokens = re.findall(r'\S+|\n', text)
            for i in range(0, len(tokens), chunk_size):
                yield ' '.join(tokens[i:i+chunk_size])
            text=rest

def read_instruction(instruction_file):
    with open(instruction_file, 'r') as file:
        return file.read().strip()

def run_llama_on_chunk(chunk, model_file, instruction):
    prompt_text = f"""
### Instruction:

{instruction}

### Input:

{chunk}

### Response:
"""

    with open('prompt.txt', 'w') as file:
        file.write(prompt_text)
    
    command = f"./main -c {max_tokens} --temp 0.0 --top_p 0.0 --top_k 1.0 -n -1 -f prompt.txt -m {model_file}"
#    print(command)
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    response_start = process.stdout.find("### Response:") + len("### Response:")
    response = process.stdout[response_start:].strip()
    return response

def chat_mode_process(chunk, model_file, instruction):
    while True:
        output_chunk = run_llama_on_chunk(chunk, model_file, instruction)
        summary = run_llama_on_chunk(chunk, model_file, "summarize this diary entry and optional analyst commentary.")
        print("LLM Summary:\n", summary)
        print("LLM Output:\n", output_chunk)
        new_input = input("Your input (leave blank to exit): ")
        if new_input == "":
            break
        new_chunk = summary + " " + output_chunk + " " 
        chunk = new_chunk + new_input
        ntokens=4001
        while (ntokens>4000):
            ntokens=count_tokens(chunk)
            print("Tokens:"+str(ntokens));
            if (ntokens<4000):
                break
            chunk=chunk[(ntokens-4000)*2:]
            print("trimming...")
    return chunk

def main(input_pattern, model_file, instruction_file, chat_mode):

    instruction = read_instruction(instruction_file)
    input_files = sorted(glob.glob(input_pattern))
    prompt_size = count_tokens(instruction)
    if chat_mode:
        for input_file in input_files:
            for chunk in split_into_chunks(input_file,prompt_size):
                chat_mode_process(chunk, model_file, instruction)
    else:
        for input_file in input_files:
            for chunk in split_into_chunks(input_file,prompt_size):
                print ("LLM Output:\n"+run_llama_on_chunk(chunk, model_file,  instruction))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py '<input_pattern>' <model_file> <instruction_file> [--chat]")
        sys.exit(1)

    input_pattern = sys.argv[1]
    model_file = sys.argv[2]
    instruction_file = sys.argv[3]
    chat_mode = '--chat' in sys.argv
    main(input_pattern, model_file, instruction_file, chat_mode)
