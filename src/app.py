from infra.web.flask.app import CharacterCRUDApp


def main():
    """
    The main function
    """
    app = CharacterCRUDApp(__name__)
    app.run()


if __name__ == "__main__":
    main()
