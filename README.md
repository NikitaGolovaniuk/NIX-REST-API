# REST-API service for movie library management

## Foreword
The requirements listed below are recommended to be completed in parallel with the study of the main material on Flask and NGINX. For example, you learned how to create models - apply this knowledge to the project by creating the necessary models, then create migrations to the models and apply them.
During your progress, you will find that the knowledge gained is not enough to apply it to the project, but do not worry, very soon (as you study the following points) this will change.

## Functional requirements

1. Searching for movies should return partial matches.
2. To display search results, you must use pagination (by default - 10 results per page).
3. Movie Operations:
- only authorized user can add
- only the authorized user who added it or the administrator can delete it
- only the authorized user who added it or the administrator can edit
- anyone can ask
4. Movies can be filtered by:
- genres
- range of release years
- director
5. Movies can be sorted by:
- rating
- release date
6. Movie Attributes:
- title
- genres
- release date
- producer
- description (optional field)
- rating (0-10)
- poster
- the user who added the movie
7. When deleting a director, the movie should NOT be deleted, instead director = 'unknown' should be set.
8. Loading data into the database should be accompanied by common sense validations (for example, the year of release should be a number, not a string).
9. On errors, adequate messages and error codes should be issued so that the API user can understand what is causing the error.
10. Authorization must be present (it is recommended to use Flask-Login).

## Project requirements

1. The basis of the application is the Flask Framework.
2. The main functionality should be covered by tests.
3. A mandatory item is the use of Docker Compose.
4. PostgreSQL must be used as the database.
5. The database must be normalized and be in at least 3rd normal form.
6. When writing code, code-style must be respected.
7. The use of type hint is actively encouraged.
8. It is preferable to use one of these tools as a virtual environment: pipenv / poetry / pyenv.
9. Requests to your backend must be proxied through Nginx.
10. When developing, use any static code analyzer of your choice: pylint / prospector / black, etc.
11. During development, Git Flow is necessarily used, the project is divided into Pull Requests, a plan of tasks that you will do and draw up in the form of a PR is pretended in advance.
12. The project must be accompanied by logging.
13. The project must be documented using swagger.
