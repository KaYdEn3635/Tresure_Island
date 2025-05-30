from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    step = request.form.get("step")
    choice1 = request.form.get("choice1", "").lower()
    choice2 = request.form.get("choice2", "").lower()
    choice3 = request.form.get("choice3", "").lower()

    if step == "1":
        if choice1 == "right":
            message = "You're dead as someone has shot you! Game over."
        elif choice1 == "left":
            return render_template('index.html', step="2")
        else:
            message = "For no reason (: You're dead."
    elif step == "2":
        if choice2 == "swim":
            message = "Game Over! You're dead. Sharks have eaten you."
        elif choice2 == "boat":
            message = "Game Over! You waited too long and wild animals got you."
        elif choice2 == "own boat":
            return render_template('index.html', step="3")
        else:
            message = "Game Over! You got lost in the forest and became dinner for wild animals."
    elif step == "3":
        if choice3 == "red":
            message = "That's it! You've won the treasure! Congratulations!"
        elif choice3 == "green":
            message = "Game Over! Snakes attacked you."
        elif choice3 == "blue":
            message = "Game Over! You're stuck forever. Bye!"
        elif choice3 == "black":
            message = "Game Over! Gorillas attacked you."
        elif choice3 == "white":
            message = "Game Over! You fell in a hole. Bye!"
        else:
            message = "You chose something mysterious and now you're dead! Bye..."
    return render_template('index.html', step="1", message=message)

if __name__ == '__main__':
    app.run(debug=True)
