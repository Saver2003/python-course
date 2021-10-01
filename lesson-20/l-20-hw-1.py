from typing import List


class Good:
    def __init__(self, title: str = '', price: float = 0, quantity: int = 0) -> None:
        self.title = title
        self.price = price
        self.quantity = quantity

    def get_common_price(self):
        return self.quantity * self.price

    def print_good(self):
        common = self.get_common_price()
        print(
            f'{self.title:<20}{self.price:>5.2f} *    {self.quantity:>2} =     {common:>6.2f}')


class DiscountGood(Good):
    def __init__(self, title: str = '', price: float = 0, quantity: int = 0, discount: int = 0) -> None:
        super().__init__(title=title, price=price, quantity=quantity)
        self.discount = discount

    def get_common_price(self):
        without_discount = super().get_common_price()

        if self.discount > 0:
            return without_discount - (without_discount * (self.discount / 100))
            ...
        else:
            return without_discount

    def print_good(self):
        if self.discount > 0:
            common = self.get_common_price()
            print(
                f'{self.title:<20}{self.price:>5.2f} *    {self.quantity:>2} =     {common:>6.2f}  (-{self.discount}%)')
        else:
            super().print_good()


class Cart:
    def __init__(self, goods: List[Good] = []) -> None:
        self.goods = goods

    def get_all_price(self):
        price = []
        for good in self.goods:
            price.append(good.get_common_price())
        return sum(price)

    def print_goods(self):
        print('{:<20}{:>5}    {:<11}{:>6}   {}'.format(
            'Name', 'PPU', 'CNT', 'Price', 'Disc.'))
        print('======================================================')
        for good in self.goods:
            good.print_good()
        print('======================================================')
        print('{:<34}{:<6}{:<7.2f}'.format('Total', '=', self.get_all_price()))


# apple = Good('apple', 4, 2)

# apple.print_good()
# disc_apple = DiscountGood('green apple', 10, 2, 12)

# disc_apple.print_good()

goods = [
    Good('Bread', 17, 3),
    Good('Water', 19, 2),
    DiscountGood('Juice', 80, 1, 20),
    Good('Toilet paper', 19, 10),
    DiscountGood('Potatoes', 22, 3, 15)
]


cart = Cart(goods)

cart.get_all_price()

cart.print_goods()
