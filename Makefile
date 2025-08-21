build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d 

down:
	docker compose down 

down -v:
	docker compose down -v 




# GIT functions
push-all:
	git add .
	git commit -m 'edits'
	git push origin -u main

push:
	git push origin -u main

commit:
	git add .
	git commit
	git push origin -u main