# Задание 1

# Пример 1
class ContactForm:

    def __init__(self, client_phone):
        self.phone = client_phone
        self.title = ''
        self.message = ''

    @staticmethod
    def create_support(client_phone, message):
        contact_form = ContactForm(client_phone)
        contact_form.title = 'New support request'
        contact_form.message = message
        return contact_form

    @staticmethod
    def create_call_back(client_phone):
        contact_form = ContactForm(client_phone)
        contact_form.title = 'Please, call me back'
        return contact_form


call_back_form = ContactForm.create_call_back('375292208643')
support_form = ContactForm.create_support('375292208643', 'I can`t login. Help me!')


# Пример 2
class Circle:

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def from_radius(radius):
        circle = Circle(radius)
        return circle

    @staticmethod
    def from_perimeter(perimeter):
        radius = round(perimeter / 2 / 3.14, 2)
        circle = Circle(radius)
        return circle


circle1 = Circle.from_radius(5)
circle2 = Circle.from_perimeter(25)


# Пример 3
class JobProgress:

    def __init__(self, job_id):
        self.job_id = job_id

    @staticmethod
    def from_job_id(job_id):
        job_progress = JobProgress(job_id)
        return job_progress


job_progress = JobProgress.from_job_id(3)


# Задание 2

# абстрактная фабрика для создания клиента
CustomerFactory

# классы с конкретными реализациями
CustomerFactoryMts
CustomerFactorySberbank
CustomerFactoryAlfabank
