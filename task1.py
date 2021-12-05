from __future__ import annotations

import time
from enum import Enum


class ProductType(Enum):
    MEDIUM_WHITE_CHAIR = 1
    BIG_UNCOLORED_CHAIR = 2
    LITTLE_YELLOW_CHAIR = 3
    TRENDY_PURPLE_CHAIR = 4
    FANCY_BLUE_CHAIR = 5


class Color:
    def __init__(self):
        self.R = None
        self.G = None
        self.B = None


class Chair:
    def __init__(self):
        self.type = None
        self.price = 0
        self.color = None
        self.legs_count = 0
        self.length = 0

    def __str__(self):
        return str(self.type) + " " + str(self.price) + "$ " \
               + str(self.length) + "cm with " + str(self.legs_count) + " legs. " \
               + "RGB(" + str(self.color.R) + "," + str(self.color.G) + "," + str(self.color.B) + ")"


# builder and director desc https://refactoring.guru/ru/design-patterns/builder
class Builder:
    def reset(self) -> Builder:
        pass

    def set_price(self, price: int) -> Builder:
        pass

    def set_type(self, product_type: ProductType) -> Builder:
        pass

    def set_color(self, color: Color) -> Builder:
        pass

    def set_legs_count(self, legs_count: int) -> Builder:
        pass

    def set_length(self, length: int) -> Builder:
        pass

    def build(self) -> Chair:
        pass


class MexicanChairBuilder(Builder):
    def __init__(self):
        self._chair = Chair()

    def reset(self) -> Builder:
        self._chair = Chair()
        return self

    def set_price(self, price: int) -> Builder:
        self._chair.price = price
        return self

    def set_type(self, product_type: ProductType) -> Builder:
        self._chair.type = product_type
        return self

    def set_color(self, color: Color) -> Builder:
        self._chair.color = color
        return self

    def set_legs_count(self, legs_count: int) -> Builder:
        self._chair.legs_count = legs_count
        return self

    def set_length(self, length: int) -> Builder:
        self._chair.length = length
        return self

    def build(self) -> Chair:
        return self._chair


class Director:
    def __init__(self, builder: Builder):
        self._builder = builder

    def make(self, product_type: ProductType) -> Chair:
        self._builder.reset()
        length = 120
        color = Color()
        legs = 4
        price = 1000

        if product_type == ProductType.FANCY_BLUE_CHAIR:
            price = 99999
            legs = 5
            color.B = 255
            color.R = 0
            color.R = 0

        elif product_type == ProductType.TRENDY_PURPLE_CHAIR:
            color.R = 230
            color.G = 230
            color.B = 250
            legs = 1
            price = 9999

        elif product_type == ProductType.LITTLE_YELLOW_CHAIR:
            color.R = 255
            color.G = 255
            color.B = 0
            length = 80

        elif product_type == ProductType.MEDIUM_WHITE_CHAIR:
            color.R = 255
            color.G = 255
            color.B = 255
            length = 140

        elif product_type == ProductType.BIG_UNCOLORED_CHAIR:
            length = 200

        return self._builder.set_color(color).set_legs_count(legs)\
            .set_price(price).set_type(product_type).set_length(length).build()


# singleton, abstract factory https://refactoring.guru/ru/design-patterns/abstract-factory
class AbstractFactory:
    def produce(self):
        pass

class ChairFactory(AbstractFactory):
    _fact = None

    def __init__(self, director: Director):
        self._director = director

    @classmethod
    def get_instance(cls) -> AbstractFactory:
        if cls._fact is None:
            cls._fact = ChairFactory(
                Director(
                    MexicanChairBuilder()
                ))

        return cls._fact

    def produce(self):
        while True:
            yield [
                self._director.make(ProductType.MEDIUM_WHITE_CHAIR),
                self._director.make(ProductType.BIG_UNCOLORED_CHAIR),
                self._director.make(ProductType.LITTLE_YELLOW_CHAIR),
                self._director.make(ProductType.TRENDY_PURPLE_CHAIR),
                self._director.make(ProductType.FANCY_BLUE_CHAIR)
            ]
            time.sleep(10)


if __name__ == '__main__':
    mexican_chair_factory = ChairFactory.get_instance()
    for products in mexican_chair_factory.produce():
        print("Made", len(products), "chairs:")
        for chair in products:
            print(">", chair)


