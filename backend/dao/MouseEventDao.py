import mongodb


def store(mouse_event):
    mongodb.db.event.insert(mouse_event)
