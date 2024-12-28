# Flask Blog

A simple yet powerful blogging application built using Flask, a lightweight Python web framework. This project demonstrates how to create a blog with user authentication, post creation, and content management.

#### TODO: 
- add type hints and annotations to code (✔️); 
- modify HTML and CSS layout for more modern look;
- add info in About (✔️), Latest Posts, Announcements etc pages;

---

## Features

- **User Authentication**: Registration, Login, Logout, and Profile Management.
- **Post Management**: Create, edit, and delete blog posts.
- **Markdown Support**: Write and format content using Markdown syntax.
- **Responsive Design**: Modern and user-friendly interface.
- **Database Integration**: Manage user and post data efficiently with SQLAlchemy.
- **Flash Messaging**: Real-time notifications for user actions.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alespool/Flask_Blog.git
   cd Flask_Blog
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add the following:
     ```env
     FLASK_APP=run.py
     FLASK_ENV=development
     SECRET_KEY=your_secret_key
     SQLALCHEMY_DATABASE_URI=sqlite:///site.db
     ```
   - Otherwise create them form your CMD terminal.

5. Boot up the app:
    - In the CMD write `python run.py` when located within the folder;
    - OR assign the app path to an environment variable and run that.

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage

- **Homepage**: View recent blog posts.
- **Authentication**: Register for an account or log in to access additional features.
- **Post Creation**: Create new blog posts with a rich-text editor supporting Markdown.
- **Profile Management**: Edit your user profile and manage your posts.

---

## Project Structure

```
Flask_Blog/
├── flaskblog/
│   ├── main/
│   │   ├── __init__.py
│       └── ...
│   ├── posts/
│   │   ├── __init__.py
│       └── ...
│   ├── users/
│   │   ├── __init__.py
│       └── ...
│   ├── errors/
│   │   ├── __init__.py
│       └── ...
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── errors/
│   │   ├── layout.html
│   │   ├── ...
│   └── static/
│   │   ├── profile_pics/
│       ├── main.css
│       └── ...
├── venv/
├── instance
│   ├── site.db
├── run.py
└── requirements.txt
```

---

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Let me know if you'd like to customize this further or add any specific sections!