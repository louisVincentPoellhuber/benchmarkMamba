# benchmarkMamba

This is the directory we'll be using to benchmark Mamba. 

## Install
We should start by creating a virtual environment, so that the code can be easily reproduced. We can do it either [directly in VSCode](https://code.visualstudio.com/docs/python/environments) or [with a terminal](https://docs.python.org/3/tutorial/venv.html).

I added a `.env` file containing the following environment variables:

- `LOCAL_DATA_PATH`: The path on your computer to the data, so we can test locally before testing on SSH. 
- `HF_TOKEN`: Your huggingface API token. I imagine we're gonna need it. 
