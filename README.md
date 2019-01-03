# thee-flying-chicken
HackIowa Mentorship Repository  
  
    
## Project Package Management
[Conda](https://conda.io/docs/) via miniconda or anaconda   
Create your local environment from the env.yml file
```bash
conda env create -f tfc.yml
```
Then activate the environment
```bash
conda activate tfc
```

## Project Configuration
main project paths will be stored in the config.json file, which is part of the git ignore, but can be generated via the following command:
```bash
cd thee-flying-chicken # you need to run this command from thee-flying-chicken directory
python scripts/py/reset_config.py
```







