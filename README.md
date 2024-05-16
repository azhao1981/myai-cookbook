
Welcome to MyAI Cookbook


```bash
git clone git@github.com:azhao1981/myai-cookbook.git
```
## uv
```bash
uv venv .myai-cookbook
```
https://github.com/astral-sh/uv

## jupyterlab

```powershell
Remove-Item Env:\CONDA_PREFIX
# uv.toml 不生效？ 的 ucloud和生效，用了国内源，哈哈
uv pip install jupyterlab -i "https://pypi.tuna.tsinghua.edu.cn/simple"
uv pip install python-dotenv -i "https://pypi.tuna.tsinghua.edu.cn/simple"
uv pip install ipywidgets -i "https://pypi.tuna.tsinghua.edu.cn/simple"

jupyter lab .
```

https://jupyter.org/install

## google gai

```bash
uv pip install -U google-generativeai -v
# 这个看来确实没有起作用
uv pip install -U google-generativeai -i "https://pypi.tuna.tsinghua.edu.cn/simple"
```

https://github.com/google-gemini/cookbook/blob/main/examples/Guess_the_shape.ipynb
## ref

https://github.com/fastai/fastbook
The fastai book, published as Jupyter Notebooks

## vscode settings 不生效

```json
"terminal.integrated.profiles.windows": {
    "Custom PowerShell": {
      "source": "PowerShell",
      "args": [
        "-NoExit",
        "-Command",
        "Remove-Item Env:\\CONDA_PREFIX; $profile"
      ]
    }
  },
```