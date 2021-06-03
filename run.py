from app import create_app, create_db
from app.utils.decorators import get_http_exception_handler

app, manager = create_app(__name__)

# Override the HTTP exception handler.
app.handle_http_exception = get_http_exception_handler(app)

if __name__ == "__main__":
    with app.app_context():
        create_db()
    app.run(debug=True)