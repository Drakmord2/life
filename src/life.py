
from app.config import cfg
from app.dependencies import DI
from app.app import App


if __name__ == "__main__":
    container = DI()
    container.set('config', cfg)

    app = App(container)
    app.on_execute()
