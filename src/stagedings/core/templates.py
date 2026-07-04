from fastapi.templating import Jinja2Templates
from stagedings.core.paths import TEMPLATES_DIR

templates = Jinja2Templates(directory=TEMPLATES_DIR)