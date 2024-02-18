from flask import Flask, render_template, request, jsonify, redirect, url_for
from chatbot import advanced_chatbot
from weather import get_weather
from expense import ExpenseTracker
import traceback 
import datetime
from todo import Todo


app = Flask(__name__)
expense_tracker = ExpenseTracker()
todo_list = Todo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/todo')
def todo():
    tasks = todo_list.get_tasks()
    return render_template('todo.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    todo_list.add_task(task)
    return redirect(url_for('todo'))

@app.route('/delete_task/<int:index>')
def delete_task(index):
    todo_list.delete_task(index)
    return redirect(url_for('todo'))

@app.route('/complete_task/<int:index>')
def complete_task(index):
    todo_list.mark_completed(index)
    return redirect(url_for('todo'))

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        api_key = "c8ac599d5515a8f1e3c02b1f3aa66a77"  # Replace with your OpenWeatherMap API key
        city = request.form['city']
        
        weather_info = get_weather(api_key, city)

        if weather_info:
            temperature = weather_info['main']['temp']
            description = weather_info['weather'][0]['description']
            humidity = weather_info['main']['humidity']
            
            return render_template('weather.html', city=city, temperature=temperature, description=description, humidity=humidity)
        else:
            error_message = f"Failed to retrieve weather information for {city}. Please check your input."
            return render_template('weather.html', error_message=error_message)
    
    return render_template('weather.html', city=None, temperature=None, description=None, humidity=None, error_message=None)

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        date = datetime.date.today().strftime("%Y-%m-%d")
        expense_tracker.add_expense(amount, category, date)

    expenses_by_category = expense_tracker.get_expenses_by_category()
    return render_template('expenses.html', expenses_by_category=expenses_by_category)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.form['user_input']
        response = advanced_chatbot.respond(user_input)
        return jsonify({'response': response})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'response': 'An error occurred on the server.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
