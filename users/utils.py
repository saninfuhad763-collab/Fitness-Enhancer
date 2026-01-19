def is_premium(user):
    return hasattr(user, 'subscription') and user.subscription.plan == 'premium'
