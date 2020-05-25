# URL Shortener

## Launching the project

Run `git clone https://github.com/alexfurmenkov/URL-Shortener.git`

### Docker
1. Run `docker-compose up` if building for the first time or `docker-compose up --build` to rebuild
2. Wait.
3. **Run migrations in the running "web" container**

    _Using PyCharm:_
   
    Services -> Docker -> shortener -> web-> /shortener_web_1
    
    Click "Exec"
    
    Run the following commands:
    
    `python /code/manage.py makemigrations shortener`
    
    `python /code/manage.py migrate`
    
    _Using terminal:_
    
    Run `docker ps`
    
    Copy CONTAINER ID of shortener_web_1 image
    
    Run `docker exec -it <CONTAINER ID> bash`
    
    Run `python /code/manage.py makemigrations shortener`
    
    Run `python /code/manage.py migrate`

### Terminal
1. Set DOCKER = False in src/shortener/settings.py

2. Make sure you have MySQL DB called `url_shortener` created locally

3. run `python3 -m venv venv` if using Linux or `py -m venv venv` if using Windows

4. run `source venv/bin/activate` if using Linux or `.\venv\Scripts\activate` if using Windows

5. run `pip install -r requirements/requirements.txt`

6. run `python src/manage.py makemigrations shortener`

7. run `python src/manage.py migrate`

8. run `python src/manage.py runserver localhost:8000`


## **Navigate to http://localhost:8000 to use the app or to http://localhost:8000/docs/ to see the docs.**