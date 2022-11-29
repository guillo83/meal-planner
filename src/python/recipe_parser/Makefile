install:
	# install command
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	# format code
	black *.py mylib/*.py
lint:
	#flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python3 -m pytest -vv --cov=mylib test_logic.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker
	# docker images | awk '{print $3}' | awk 'NR==2'
	# docker run -p 127.0.0.1:8080:8080 5c5b225f5789
deploy:
	#deploy
	aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 759974195639.dkr.ecr.us-west-2.amazonaws.com
	docker build -t recipe-parse-deploy .
	docker tag recipe-parse-deploy:latest 759974195639.dkr.ecr.us-west-2.amazonaws.com/recipe-parse-deploy:latest
	docker push 759974195639.dkr.ecr.us-west-2.amazonaws.com/recipe-parse-deploy:latest
all: install lint test deploy