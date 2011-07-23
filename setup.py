from setuptools import setup, find_packages

setup(
    name = "Communes",
    version = "0.1.0",
    description = """
    A django app with the list of all French Communes with Postal code, Insee Code, Population, Latitude and Longitude
    """,
    author = "Platypus Creation",
    author_email = "contact@platypus-creation.com",
    url = "https://github.com/platypus-creation/django-communes",
    packages = find_packages(),
    include_package_data=True,    
)
