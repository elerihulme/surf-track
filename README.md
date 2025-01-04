# Gower Surf Track website

**Deployed website: [Link to website](https://surf-track-e46e8d35b2da.herokuapp.com/)**


![Main image](documentation/features/header-image.png)

## About

Gower Surf Track is a community-driven platform for surfers to log, rate, and share their surf experiences. Users can record their surf sessions, track wave conditions, and view surf data from other community members. The site offers insights into surf spots and creates a surf journal to monitor progress over time.

---

## UX

The Surf Track platform is designed with a clean, intuitive interface to provide surfers with an easy and enjoyable experience when logging their surf sessions. The goal is to ensure seamless navigation, allowing users to quickly add, view, and manage their surf logs. By incorporating feedback from the surf community, the platform addresses user needs such as tracking surf conditions, rating surf spots, and sharing insights with other surfers. The responsive design ensures the platform is accessible across all devices, enhancing the experience whether accessed from a phone on the beach or a desktop at home.

### Target Audience

- Surfers of all levels (beginners to advanced)

- Surf enthusiasts looking to track their progress

- People interested in surf forecasting and ocean conditions

### User Stories

#### Site User
| Issue ID    | User Story |
|-------------|-------------|
| [#1](https://github.com/elerihulme/surf-track/issues/1) | As a site user I can view a list of all uploaded surf sessions so that I can discover new spots and learn about surf conditions |
| [#2](https://github.com/elerihulme/surf-track/issues/2) | As a site user I can log surf sessions so that I can track my progress |
| [#4](https://github.com/elerihulme/surf-track/issues/4) | As a site user I can edit or delete my sessions so that I can keep my data accurate and up to date |
| [#5](https://github.com/elerihulme/surf-track/issues/5) | As a site user I can sign up and log in so that I can view the sessions of the community |
| [#11](https://github.com/elerihulme/surf-track/issues/11) | As a site user I can select a session so that I can view the session in more detail |
| [#12](https://github.com/elerihulme/surf-track/issues/12) | As a site user I can view a paginated list of sessions so that I can select which session I want to view |
| [#13](https://github.com/elerihulme/surf-track/issues/13) | As a site user I can learn about the platform's features so that I understand the benefits of joining |

#### Site Owner

| Issue ID    | User Story |
|-------------|-------------|
| [#6](https://github.com/elerihulme/surf-track/issues/6) | As a site owner I can view all the surf sessions and users so that I can monitor activity on the platform |

---

## Future Development

- Filtering sessions to find relevant data easier
- Specific details for each surf location 
- Site admin can remove users and sessions

---


## Technologies used
- ### Languages:
    
    + [Python 3.8.5](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    + [Bootstrap](https://getbootstrap.com/): library used for structure, styling and responsive design.

- ### Databases:

    + [SQLite](https://www.sqlite.org/): was used as a development database.
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.


- ### Other tools:

    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Gunicorn](https://gunicorn.org/): the web server used to run the website.
    + [Psycopg2](https://www.psycopg.org/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [Gitpod](https://www.gitpod.io/): the IDE used to develop the website.
    + [Heroku](https://www.heroku.com/): the platform used to deploy the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.
    + [Lucid Chart](https://www.lucidchart.com/) was used to create the Entity-Relationship Diagram.

---

## Features

### Home Page

### My Sessions Page

### Log Session Page

### Register PAge

### Login Page

### Logout Page

---
## Design


### Color Scheme



### Typography


### Wireframes

#### Mobile

- [Home. Mobile Screen](documentation/wireframes/home-mobile-wireframe.png)
- [Home, Details Modal. Mobile Screen](documentation/wireframes/home-detail-mobile-wireframe.png)
- [My Sessions. Mobile Screen](documentation/wireframes/my-sessions-mobile-wireframe.png)
- [My Sessions, Details modal. Mobile Screen](documentation/wireframes/my-sessions-details-mobile-wireframe.png)
- [Log a Session. Mobile Screen](documentation/wireframes/log-a-session-mobile-wireframe.png)

#### Desktop

- [Home. Desktop Screen](documentation/wireframes/home-desktop-wireframe.png)
- [Home, Details Modal. Desktop Screen](documentation/wireframes/home-details-desktop-wireframe.png)
- [My Sessions. Desktop Screen](documentation/wireframes/my-sessions-desktop-wireframe.png)
- [My Sessions, Details modal. Desktop Screen](documentation/wireframes/my-sessions-details-desktop-wireframe.png)
- [Log a Session. Desktop Screen](documentation/wireframes/log-a-session-desktop-wireframe.png)


---

## Agile Methodology

- Development followed Agile practices using GitHub Issues and Projects.

### GitHub Project Management



---

## Information Architecture

### Database

- **SQLite** - Development.  
- **PostgreSQL** - Production.  


### Entity-Relationship Diagram

[ERD](documentation/database/erd.png)

### Data Modeling

#### Session Model
| Name           | Field Type            | Validation                                                  |
| -------------- | --------------------- | ----------------------------------------------------------- |
| user           | ForeignKey            | User, on_delete=models.CASCADE, related_name="surf_sessions"|
| date           | DateField             | default=datetime.date.today                                 |
| time           | TimeField             | default=datetime.time(0, 0)                                 |
| location       | IntegerField          | choices=LOCATION, default=0                                 |
| wave_height    | PositiveIntegerField  |                                                             |
| wind_direction | IntegerField          | choices=WIND, default=0                                     |
| wind_speed     | PositiveIntegerField  |                                                             |
| tide           | IntegerField          | choices=TIDE, default=0                                     |
| surfboard_used | CharField             | blank=True                                                  |
| notes          | TextField             | blank=True                                                  |
| rating         | IntegerField          | choices=RATING, default=0                                   |

---
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.

---

## Deployment

- The app was deployed to [Heroku](https://www.heroku.com/)

After account setup the deployment steps are as follows:

### 1. Create a New Heroku App:
- Select **New** in the top-right corner of your Heroku Dashboard.
- Choose **Create new app** from the dropdown menu.
- Enter a unique app name and select the region (EU or USA).
- Click **Create App**.

### 2. Connect to GitHub:
- In the app dashboard, navigate to the **Deploy** tab.
- Under the **Deployment method** section, select **GitHub**.
- Click **Connect to GitHub** and authorize Heroku to access your GitHub account.
- Search for your repository and click **Connect**.

### 3. Set Environment Variables (Config Vars):
- Go to the **Settings** tab and click **Reveal Config Vars**.
- Add the following key-value pairs:

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `SECRET_KEY` | user's own value |

### 4. Prepare Django for Heroku Deployment:

- Create an env.py file

- Install the required packages:
  pip install gunicorn django-heroku psycopg2

- Update requirements.txt

- Add Heroku to allowed_hosts

- Create a Procfile in your project"s root directory and add:
    web: gunicorn <your_project_name>.wsgi


### 5. Push to GitHub

### 6. Deploy


---

## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Render](https://render.com/): for providing a free hosting.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [googlefonts](https://fonts.google.com/): for providing free fonts.
- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en): for providing a free platform to test website responsiveness
- [GoFullPage](https://gofullpage.com/): for allowing to create free full web page screenshots;
- [Coolors](https://coolors.co/): for providing a free platform to generate your own palette.

## Acknowledgments

- [Julia Konovalova](https://github.com/IuliiaKonovalova) was a great mentor throughout this project, guiding me to help shape the project and bring it to life.
- [Code Institute](https://codeinstitute.net/) for the knowledge to complete a project like this and to the tutors and slack community for their support and help.
- My friends and family for their feedback and help in testing the site.

---
