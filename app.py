from flask import Flask,jsonify,request,render_template
from storage import combined_query

user_input = input("Input Prompt: ")
final_output = combined_query(user_input)
print(final_output)

app = Flask(__name__)

@app.route("/ask")
def index():
    
    return jsonify({"Mesage": "Hey this is Vishal!"})

if __name__ == "__main__":
    app.run(debug=True)


# Structure
# {
#     promet: string;
# }

# Output
# {
#     "answer": string
# }






