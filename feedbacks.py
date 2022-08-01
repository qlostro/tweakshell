def add_feedback(user, sm, feedback):
    with open('feedback.txt', 'a') as f:
        f.write(f'\n {sm}|{user}: {feedback} ')

def rfeedbacks():
    with open('feedback.txt', 'r') as f:
        feedback = f.read()
        return feedback

