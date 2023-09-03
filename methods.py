

from models import Customer, Restaurant, Review, session

def get_customer_by_id(customer_id):
    return session.query(Customer).filter_by(id=customer_id).first()

def favorite_restaurant(customer):
    return session.query(Restaurant)\
        .join(Review)\
        .filter(Review.customer == customer)\
        .order_by(Review.star_rating.desc())\
        .first()

def add_review(customer, restaurant, rating):
    new_review = Review(star_rating=rating, customer=customer, restaurant=restaurant)
    session.add(new_review)
    session.commit()

def delete_reviews(customer, restaurant):
    session.query(Review).filter(Review.customer == customer, Review.restaurant == restaurant).delete()
    session.commit()

def fanciest_restaurant():
    return session.query(Restaurant).order_by(Restaurant.price.desc()).first()

def get_reviews_for_restaurant(restaurant):
    reviews = session.query(Review).filter_by(restaurant=restaurant).all()
    formatted_reviews = [f"Review for {restaurant.name} by {review.customer.first_name} {review.customer.last_name}: {review.star_rating} stars" for review in reviews]
    return formatted_reviews
