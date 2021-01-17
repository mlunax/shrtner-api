from repositories import RedirectRepository
from models import RedirectModel

m = RedirectModel("dupa", "https://duck.com", "123")
a = RedirectRepository()
print(a.get_url("dupsa"))