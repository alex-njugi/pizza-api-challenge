from server.app import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    print("🌱 Seeding data...")

    # Clear old data
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Create restaurants
    r1 = Restaurant(name="Luigi's", address="123 Pasta Lane")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Cheesy Blvd")

    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni")

    # Join table
    rp1 = RestaurantPizza(price=12, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=15, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=10, restaurant=r2, pizza=p1)

    # Add and commit
    db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
    db.session.commit()

    print("✅ Done seeding!")
