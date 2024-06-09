# Appendix

## Install and setup pyenv and poetry

- [Arch Linux](#arch-linux)
- [MacOS](#macos)

### Arch Linux

1. Install pyenv

   ```shell
   yay -S pyenv
   ```
   Add the following lines to your shell configuration file

   ```shell
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```

2. Install python using pyenv

   ```shell
   pyenv install 3.12.2
   ```

3. Install poetry

   Switch current shell and check which python executable is using

   ```shell
   pyenv shell 3.12.2
   which python
   ```

   Should return something like `/home/user/.pyenv/shims/python`. then run the following command

   ```shell
   curl -sSL https://install.python-poetry.org | python -
   ```

### MacOS

1. Install pyenv

   ```shell
   brew install pyenv
   ```
   Add the following lines to your shell configuration file

   ```shell
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```

2. Install python using pyenv

   ```shell
   pyenv install 3.12.2
   ```

3. Install poetry

   Switch current shell and check which python executable is using

   ```shell
   pyenv shell 3.12.2
   which python
   ```

   Should return something like `/home/user/.pyenv/shims/python`. then run the following command

   ```shell
   brew install poetry
   ```