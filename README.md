[![Python application test with Github Actions](https://github.com/arunkkumar1/scaffolding_template/actions/workflows/basic-continuous-integration.yml/badge.svg)](https://github.com/arunkkumar1/scaffolding_template/actions/workflows/basic-continuous-integration.yml)



# Python Scaffolding Template

This repo contains core components and a starting structure recommended for a python project, including development and CI/CD. All commands in this scafolding were executed in github codespaces

## Create a virtual env:
Needed to use a  consistent virtual environment every time:

Steps: 
	1. Create a virtual environment:
    >virtualenv ~/.venv
	
	2. Activate virtual env and confirm current python is in newly created virtual env

    >source ~/.venv/bin/activate
	>which python
	
	3. To add this setting everytime a new terminal is started edit bashrc file
    vim ~/.bashrc

	4. navigate to bottom of file using 'shift + g' then insert using 'shift + I'
    #source virtual environment
    >source ~/.venv/bin/activate

	5. Exit vim by 'escape + :wq"

With this, every time a new terminal is created, it will have same virtual environment

## Create a project scaffolding
Needed to setup all required components/libraries/test dependencies/formatting etc for the project. Refer github repo for templates: arunkkumar1/scaffolding_template (github.com)

	1. Create Makefile
    >touch Makefile
	2. Create requirements file, which will contain list of packages needed to be installed
    >touch requirements.txt
	3. Create your application file and test file
    >touch hello.py
    >touch test_hello.py
	4. Execute installs
    >make install
	5. Verify pytest was installed
    >pytest --help
	
## Build code

	1. Write *.py python code
	2. Interactive debugging via ipython
	3. Write test code
	4. Test via make test
	5. Lint code via make lint (this will check for best practices/poor syntax even if its not an error) 
	6. Format the code via make format

## Refine environment packages

Check current versions of packages and update requirements.txt with those versions

>pip freeze | less

## Push the code to repo


>git status
>git add *
>git commit -m "adding initial layout of python project"
>git push

## Setup build system (CI/CD)

	1. Navigate to github > actions
	2. Select 'set up a workflow yourself
	3. And create yml file with defined workflow
		a. This will execute the build pipeline every time a code is pushed to repo
	4. Check build status and ensure successful completion
    5. After build successfully completes, create status badge and paste it to readme file 


