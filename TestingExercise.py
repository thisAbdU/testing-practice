import unittest

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotal(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def addProduct(self, product):
        self.cart.append(product)

    def getCartTotal(self):
        total = 0
        for item in self.cart:
            total += item.calculateTotal()
        return total

class TestShoppingCartIntegration(unittest.TestCase):
    def test_cart_total(self):
        # Create some products
        product1 = Product("Apple", 1.5, 2)
        product2 = Product("Banana", 0.75, 4)

        # Create a shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.addProduct(product1)
        cart.addProduct(product2)

        # Check if the total price of the cart is calculated correctly
        self.assertEqual(cart.getCartTotal(), 7.5)

if __name__ == '__main__':
    unittest.main()
