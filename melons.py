"""Classes for melon orders."""
from random import randint
from datetime import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code):

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False

        if self.qty > 100:
            raise(TooManyMelonsError)

    def get_total(self):
        """Calculate price, including tax."""
        fee = 0

        base_price = self.get_base_price()

        if self.species.title() == "Christmas":
            base_price = 1.5*base_price

        if self.order_type == "international" and self.qty < 10:
            fee = 3

        total = (1 + self.tax) * self.qty * base_price + fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True      


    def get_base_price(self):
        """Calculate base price

        Randomly choose base price as integer between 5 and 9 
        and implement rush hour pricing.

        """

        base_price = randint(5,9)

        now = datetime.now()

        if now.weekday() < 5 and now.hour >= 8 and now.hour <= 11:
            base_price += 3

        return base_price




class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order by the US Government"""
    tax = 0
    passed_inspection = False
    order_type = "domestic"

    def mark_inspection(self, passed):

        self.passed_inspection = passed        


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08  


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class TooManyMelonsError(ValueError):
    """Exception raised for too many melons"""

    def __init__(self):
        self.expression = "TooManyMelonsError"
        self.message = "No more than 100 melons!"
